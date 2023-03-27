#-*- coding: UTF-8 -*-

import time
import requests
import threading
from tqdm import tqdm
from retry import retry
from bs4 import BeautifulSoup
import pandas as pd

import sys
sys.path.append("../..")
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger

logger = get_logger(name=__name__)

class TedtalkExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.all_results = []
    
    @log(logger)
    def bs4_parser(self, url: str) -> BeautifulSoup:
        """
        use beautiful soup to parse html text
        """
        res = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        return soup
    
    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def get_page_num(self, url: str) -> int:
        """
        get page number of input tedtalk url
        """
        soup = self.bs4_parser(url)
        pages = soup.find_all("a", class_="pagination__item pagination__link")
        page_num = pages[-1].text
        
        return int(page_num)
    
    # @log(logger)
    # @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def parse_extra_info(self, talk_url: str) -> tuple:
        """
        RETURN: details, tags, views
        TO-DO: transcript, duration, likes, language
        """
        soup = self.bs4_parser(talk_url)
        details = soup.find("div", class_="text-sm mb-6").text
        tags = soup.find_all("li", class_="mr-2 inline-block last:mr-0 css-wzaabn e1r7k7tp0")
        tags = [t.text for t in tags]
        views = soup.find("div", class_="flex flex-1 items-center overflow-hidden").text
        views = views.split(" ")[0].replace(",", "")

        return details, tags, views

    @log(logger)
    @retry(tries=5, delay=3, backoff=2 ,max_delay=60)
    def parse_basic_info(self, talk: object) -> tuple:
        """
        parse basic in for given talks raw meta
        """
        author = talk.find(class_="h12 talk-link__speaker").text.replace("\n", "")
        title = talk.find(class_="ga-link").text.replace("\n", "")
        base_url = "https://www.ted.com"
        link = base_url + talk.find("a", class_="ga-link")['href']
        posted = talk.find(class_="meta__val").text.replace("\n", "")
        details, tags, views = self.parse_extra_info(talk_url = link)
        uid = link.split("/")[-1]
        result = {
            "uid": uid, 
            "author": author, 
            "title": title, 
            "link": link, 
            "posted": posted, 
            "details": details, 
            "tags": tags, 
            "views": views
        }

        return result
    
    @log(logger)
    def get_all_talks_current_page(self, url: str) -> None:
        """
        get basic info of each talks in current page
        """
        soup = self.bs4_parser(url)
        talks = soup.find_all("div", class_="media__message")
        for talk in tqdm(talks):
            # time.sleep(0.5)
            self.all_results += [self.parse_basic_info(talk)]
    
    @log(logger)
    def extract(self) -> list:
        """
        main logic
        """
        # get total pages
        url = "https://www.ted.com/talks?language=en&sort=newest"
        pages = self.get_page_num(url = url)
        logger.info(f"PAGES: {pages}")
        pages = 1
        threads = [
            threading.Thread(target=self.get_all_talks_current_page, args=(f"{url}&page={str(current_page)}",)) for current_page in range(1, pages+1)
        ]
        for tr in threads:
            tr.start()
        for tr in threads:
            tr.join()
        chunk_results = self.chunks(self.all_results, 1)

        return chunk_results


# dc = TedtalkExtractor()
# res = dc.extract()
# logger.info(f"LENGTH: {len(res)}")

# pd.DataFrame(res).dropna().to_excel("test_01.xlsx", index = False)