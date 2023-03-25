#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
from src.CrawlerBase import TransformerBase
from utils.utils import exception_handler

class DcardTransformer(TransformerBase):
    def __init__(self):
        super().__init__()
       
    @exception_handler
    def transform(self):
        print("This is a test!")