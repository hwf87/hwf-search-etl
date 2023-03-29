#-*- coding: UTF-8 -*-

import requests
from retry import retry
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch, helpers
from typing import Iterator
from abc import ABC, abstractmethod
from utils.utils import get_logger, log

logger = get_logger(name=__name__)

# Get data from sources
class ExtractorBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def extract(self):
        """
        """
        pass

    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=30)
    def bs4_parser(self, url: str) -> BeautifulSoup:
        """
        use beautiful soup to parse html text
        """
        res = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        return soup

    @log(logger)
    def chunks(self, lst, n) -> list:
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

# NER model for data Inference
class TransformerBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def transform(self):
        """
        """
    
    @log(logger)
    def chunks(self, lst, n) -> list:
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

# Sink data to Elasticsearch database
class LoaderBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def load(self):
        """
        """
    
    @abstractmethod
    def load_action_batch(self):
        """
        """

    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def get_es_client(self, host: str) -> Elasticsearch:
        """
        """
        # host = "http://127.0.0.1:9200"
        es = Elasticsearch(host, verify_certs = False)
        return es
    
    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def check_index(self, index_name: str, es: Elasticsearch) -> bool:
        """
        """
        res = es.indices.exists(index = index_name)
        return res

    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def create_index(self, index_name: str, body: dict, es: Elasticsearch) -> None:
        """
        """
        res = es.indices.create(index = index_name, body = body)
        status_code = res.meta.status
        logger.info(f"Create index {index_name} => {status_code}")

    @log(logger)
    def bulk_insert(self, actions: Iterator, es: Elasticsearch) -> None:
        """
        """
        batches = []
        for _, meta in helpers.streaming_bulk(
            client = es,
            actions = actions,
            chunk_size = 100,
            max_chunk_bytes = 104857600,
            max_retries = 3,
            yield_ok = True,
            ignore_status=()
        ):
            batches.append(meta)
        logger.info(f"Success Count: {len(batches)}")

