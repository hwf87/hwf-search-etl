#-*- coding: UTF-8 -*-

import requests
import threading
from typing import Callable
from queue import Queue
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
        self.jobs = Queue()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
    
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
    
    @log(logger)
    def multi_thread_process(self, all_url_list: list, process_func: Callable, thread_num: int = 10):
        """
        """
        for page_url in all_url_list:
            self.jobs.put(page_url) 
        for thread_idx in range(0, thread_num):
            logger.info(f"Start Thraed NO.: {thread_idx+1}")
            worker = threading.Thread(target=self.consume_jobs, args=(self.jobs, process_func,))
            worker.start()
        self.jobs.join()

    @log(logger)
    def consume_jobs(self, job_queue: Queue, func: Callable) -> None:
        """
        """
        while not job_queue.empty():
            url = job_queue.get()
            func(url = url)
            job_queue.task_done()

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

