#-*- coding: UTF-8 -*-

import time
import threading
from tqdm import tqdm
import pandas as pd
from retry import retry

import sys
sys.path.append("../..")
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger

logger = get_logger(name=__name__)

class HouzzExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
        self.all_results = []
    
    @log(logger)
    def extract(self) -> list:
        """
        main logic
        """

    def test(self):
        """
        """
        url = "https://www.houzz.com/ideabooks/p/0"
        soup = self.bs4_parser(url = url)
        views = soup.find_all("a", class_="gallery-text__title")
        print(views)

HE = HouzzExtractor()
soup = HE.test()