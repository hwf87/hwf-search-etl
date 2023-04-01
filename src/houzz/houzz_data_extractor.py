#-*- coding: UTF-8 -*-

import time
import threading
from tqdm import tqdm
from typing import Callable
from queue import Queue
from bs4 import BeautifulSoup
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
        self.story_list = []
        self.jobs = Queue()
    
    @log(logger)
    def extract(self) -> list:
        """
        main logic
        """
        # get total story count
        story_count = self.get_story_count(url = "https://www.houzz.com/ideabooks/p/0")
        # list done all url pages
        page_url_list = self.get_page_url_list(story_count = story_count)
        page_url_list = page_url_list[:30]
        # start multi-thread to prase story meta from each single collect page
        self.multi_thread_process(all_url_list = page_url_list, thread_num = 10)

        #TODO: parse story detail from each single story page 
        
        # save to file
        df = pd.DataFrame(self.story_list)
        df.to_excel("houzz_sample3.xlsx", index = False)

    def get_story_count(self, url: str) -> int:
        """
        """
        soup = self.bs4_parser(url = url)
        count = soup.find("span", class_="hz-browse-galleries__header-story-count").text
        count = int(count.split(" ")[0])

        return count
    
    def get_page_url_list(self, story_count: int, start_page: int = 0, end_page:int = None, story_per_page: int=11) -> list:
        """
        """
        base_uri = "https://www.houzz.com/ideabooks/p/"

        if end_page == None:
            end_page = int(story_count/story_per_page)+1
        
        page_url_list = []
        for current_page in range(start_page, end_page):
            page_idx = current_page * story_per_page
            page_url = base_uri + str(page_idx)
            page_url_list.append(page_url)

        return page_url_list
    
    def multi_thread_process(self, all_url_list: list, thread_num: int = 10) -> dict:
        """
        """
        for page_url in all_url_list:
            self.jobs.put(page_url)
        
        for thread_idx in range(0, thread_num):
            logger.info(f"Start Thraed NO.: {thread_idx+1}")
            worker = threading.Thread(target=self.consume_jobs, args=(self.jobs, self.get_stories_from_page))
            worker.start()
        
        self.jobs.join()

    def consume_jobs(self, job_queue: Queue, func: Callable) -> None:
        """
        """
        while not job_queue.empty():
            url = job_queue.get()
            func(url = url)
            job_queue.task_done()
    
    def get_story_meta_title(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            title = story.find("a", class_="gallery-text__title").text
        except Exception as e:
            logger.warning(e)
            title = ""
        return title
    
    def get_story_meta_link(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            link = story.find("a", class_="gallery-card__view-detail gallery-card__view-detail--full-story text-l")["href"]
        except Exception as e:
            logger.warning(e)
            link = ""
        return link
    
    def get_story_meta_image(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            image = story.find("img", class_="gallery-image__responsive")["src"]
        except Exception as e:
            logger.warning(e)
            image = ""
        return image
    
    def get_story_meta_category(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            category = story.find("a", class_="gallery-text__theme-link text-m").text
        except Exception as e:
            logger.warning(e)
            category = ""
        return category
    
    def get_story_meta_author(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            author = story.find("a", class_="gallery-text__author-name").text
        except Exception as e:
            logger.warning(e)
            author = ""
        return author
    
    def get_story_meta_description(self, story: BeautifulSoup) -> str:
        """
        """
        try:
            description = story.find("div", class_="gallery-text__description text-l").text
        except Exception as e:
            logger.warning(e)
            description = ""
        return description

    def get_stories_from_page(self, url: str):
        """
        URL:: https://www.houzz.com/ideabooks/p/{IDX}
        """
        logger.info(f"Job Waiting in Queue: {self.jobs.qsize()}")
        soup = self.bs4_parser(url = url)
        stories = soup.find_all("div", class_="gallery-card hz-browse-galleries-list__gallery")
        story_list_tmp = [
            {
                "category": self.get_story_meta_category(story),
                "author": self.get_story_meta_author(story),
                "description": self.get_story_meta_description(story),
                "title": self.get_story_meta_title(story),
                "link": self.get_story_meta_link(story),
                "image": self.get_story_meta_image(story),
            }
            for story in stories
        ]
        self.story_list += story_list_tmp
        
    def get_detail_form_story_page(self, story_url: str):
        """
        """
        url = "https://www.houzz.com/magazine/yard-of-the-week-2-new-cabanas-anchor-an-entertainment-space-stsetivw-vs~166190586"
        soup = self.bs4_parser(url = url)
        posted = soup.find("span", class_="hz-editorial-gallery-author-info__featured").text
        print(f"posted: {posted}")

        tags = soup.find_all("a", class_="hz-editorial-gallery-header-topics__topic__link hz-color-link hz-color-link--green hz-color-link--enabled")
        tags = [tag.text for tag in tags]
        print(f"tags: {tags}")
        
        # main_content = soup.find("div", class_="hz-editorial-gallery-main-content").text
        # print(f"main_content: {main_content}")

        related_tags = soup.find_all("div", class_="hz-editorial-gallery-related-categories__item__name")
        related_tags = [r_tag.text for r_tag in related_tags]
        print(f"related_tags: {related_tags}")
        

        

HE = HouzzExtractor()
soup = HE.extract()

# print(len(HE.story_list))
# df = pd.DataFrame(HE.story_list)
# df.to_excel("houzz_sample3.xlsx", index = False)
