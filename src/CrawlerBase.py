#-*- coding: UTF-8 -*-

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

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

# NER model for data Inference
class TransformerBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def transform():
        """
        """

# Sink data to Elasticsearch database
class LoaderBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def load():
        """
        """
    
    @log(logger)
    def check_index():
        """
        """
        pass

    @log(logger)
    def create_index():
        """
        """
        pass

    @log(logger)
    def bulk_insert():
        """
        """
        pass

    @log(logger)
    def get_batch():
        """
        """
        pass

