# -*- coding: UTF-8 -*-

import requests
import threading
from queue import Queue
from retry import retry
from bs4 import BeautifulSoup
from datetime import date, timedelta
from elasticsearch import Elasticsearch, helpers
from typing import Iterator, Callable, List, Any
from abc import ABC, abstractmethod
from utils.utils import get_logger, log
from utils.config_parser import (
    elasticsearch_host,
    elasticsearch_username,
    elasticsearch_password,
)

logger = get_logger(name=__name__)


# Get data from sources
class ExtractorBase(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.jobs = Queue()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

    @abstractmethod
    def extract(self):
        """ """
        pass

    @log(logger)
    @retry(tries=5, delay=3, backoff=2, max_delay=30)
    def bs4_parser(self, url: str) -> BeautifulSoup:
        """
        use beautiful soup to parse html text
        """
        res = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        return soup

    @log(logger)
    def chunks(self, lst: List[Any], n: int) -> List[list]:
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    @log(logger)
    def date_converter(self, input: str) -> str:
        """ """
        if input == "yesterday":
            date_result = date.today() - timedelta(days = 1)
        elif "days ago" in input:
            days_ago = int(input.split(" ")[0])
            date_result = date.today() - timedelta(days = days_ago)
        elif "hours ago" in input or "hour ago" in input:
            hours_ago = int(input.split(" ")[0])
            date_result = date.today() - timedelta(hours = hours_ago)
        else:
            date_result = date.today()
        return date_result

    @log(logger)
    def multi_thread_process(
        self, all_url_list: List[Any], process_func: Callable, thread_num: int = 10
    ):
        """ """
        for url_object in all_url_list:
            self.jobs.put(url_object)
        for thread_idx in range(0, thread_num):
            logger.info(f"Start Thraed NO.: {thread_idx+1}")
            worker = threading.Thread(
                target=self.consume_jobs,
                args=(
                    self.jobs,
                    process_func,
                ),
            )
            worker.start()
        self.jobs.join()

    @log(logger)
    def consume_jobs(self, job_queue: Queue, func: Callable) -> None:
        """ """
        while not job_queue.empty():
            url_object = job_queue.get()
            func(url=url_object)
            job_queue.task_done()


# NER/Sentence model for data Inference
class TransformerBase(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def transform(self):
        """ """

    @log(logger)
    def chunks(self, lst: List[Any], n: int) -> List[list]:
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]


# Load data to Elasticsearch database
class LoaderBase(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def load(self):
        """ """

    @abstractmethod
    def load_action_batch(self):
        """ """

    @log(logger)
    @retry(tries=5, delay=3, backoff=2, max_delay=60)
    def get_es_client(self) -> Elasticsearch:
        """ """
        es = Elasticsearch(
            elasticsearch_host,
            basic_auth=(elasticsearch_username, elasticsearch_password),
            verify_certs=False,
        )
        return es

    @log(logger)
    @retry(tries=5, delay=3, backoff=2, max_delay=60)
    def check_index(self, index_name: str, es: Elasticsearch) -> bool:
        """ """
        res = es.indices.exists(index=index_name)
        return res

    @log(logger)
    @retry(tries=5, delay=3, backoff=2, max_delay=60)
    def create_index(
        self, index_name: str, body: dict, es: Elasticsearch
    ) -> None:
        """ """
        res = es.indices.create(index=index_name, body=body)
        status_code = res.meta.status
        logger.info(f"Create index {index_name} => {status_code}")

    @log(logger)
    def bulk_insert(self, actions: Iterator, es: Elasticsearch) -> None:
        """ """
        batches = []
        for _, meta in helpers.streaming_bulk(
            client=es,
            actions=actions,
            chunk_size=100,
            max_chunk_bytes=104857600,
            max_retries=3,
            yield_ok=True,
            raise_on_error=False,
            ignore_status=(),
        ):
            batches.append(meta)
        logger.info(f"Success Count: {len(batches)}")
