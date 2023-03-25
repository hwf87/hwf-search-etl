#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
from src.CrawlerBase import LoaderBase
from utils.utils import exception_handler

class DcardLoader(LoaderBase):
    def __init__(self):
        super().__init__()
       
    @exception_handler
    def extract(self):
        print("This is a test!")