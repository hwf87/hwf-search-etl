#-*- coding: UTF-8 -*-

from abc import ABC, abstractmethod
from utils.utils import exception_handler

# Get data from sources
class ExtractorBase(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def extract(self):
        """
        """
        pass

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
    
    @exception_handler
    def check_index():
        """
        """
        pass

    @exception_handler
    def create_index():
        """
        """
        pass

    @exception_handler
    def bulk_insert():
        """
        """
        pass

    @exception_handler
    def get_batch():
        """
        """
        pass

