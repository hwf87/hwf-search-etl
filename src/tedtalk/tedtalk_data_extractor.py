import sys
import time
from tqdm import tqdm
from retry import retry
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple

sys.path.append("../..")
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger
from utils.config_parser import tedtalk_base_url, month_map, fn_

logger = get_logger(name=__name__)


class TedtalkExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
        self.all_results = []

    @log(logger)
    def get_page_num(self, url: str) -> int:
        """
        get page number of input tedtalk url
        """
        soup = self.bs4_parser(url)
        pages = soup.find_all("a", class_="pagination__item pagination__link")
        page_num = pages[-1].text

        return int(page_num)

    @retry(tries=5, delay=3, backoff=2, max_delay=30)
    def parse_extra_info(self, talk_url: str) -> Tuple[str, list, str]:
        """
        RETURN: details, tags, views
        TO-DO: transcript, duration, likes, language
        """
        soup = self.bs4_parser(talk_url)
        details = self.parse_extra_info_details(soup=soup)
        tags = self.parse_extra_info_tags(soup=soup)
        views = self.parse_extra_info_views(soup=soup)

        return details, tags, views

    def parse_extra_info_details(self, soup: BeautifulSoup) -> str:
        """ """
        try:
            details = soup.find("div", class_="text-sm mb-0").text
        except Exception as e:
            logger.warning(e)
            details = ""
        return details

    def parse_extra_info_tags(self, soup: BeautifulSoup) -> List[str]:
        """ """
        try:
            tags = soup.find_all(
                "li", class_="mr-2 inline-block last:mr-0 css-wzaabn e1r7k7tp0"
            )
            tags = [t.text for t in tags]
        except Exception as e:
            logger.warning(e)
            tags = []
        return tags

    def parse_extra_info_views(self, soup: BeautifulSoup) -> str:
        """ """
        try:
            views = soup.find(
                "div", class_="flex flex-1 items-center overflow-hidden"
            ).text
            if "views" in views:
                views = views.split(" ")[0].replace(",", "")
            else:
                views = ""
        except Exception as e:
            logger.warning(e)
            views = ""
        return views

    @log(logger)
    def parse_basic_info(self, talk: BeautifulSoup) -> Dict[str, str]:
        """
        parse basic in for given talks raw meta
        """
        author = self.parse_basic_info_author(talk=talk)
        title = self.parse_basic_info_title(talk=talk)
        link = self.parse_basic_info_link(talk=talk)
        posted = self.parse_basic_info_posted(talk=talk)
        details, tags, views = self.parse_extra_info(talk_url=link)
        uid = link.split("/")[-1].split("?")[0]
        result = {
            fn_.uid: uid,
            fn_.author: author,
            fn_.title: title,
            fn_.link: link,
            fn_.posted: posted,
            fn_.details: details,
            fn_.tags: tags,
            fn_.views: views,
        }

        return result

    def parse_basic_info_author(self, talk: BeautifulSoup) -> str:
        """ """
        try:
            author = talk.find(class_="h12 talk-link__speaker").text.replace("\n", "")
        except Exception as e:
            logger.warning(e)
            author = ""
        return author

    def parse_basic_info_title(self, talk: BeautifulSoup) -> str:
        """ """
        try:
            title = talk.find(class_="ga-link").text.replace("\n", "")
        except Exception as e:
            logger.warning(e)
            title = ""
        return title

    def parse_basic_info_link(self, talk: BeautifulSoup) -> str:
        """ """
        try:
            link = tedtalk_base_url + talk.find("a", class_="ga-link")["href"]
        except Exception as e:
            logger.warning(e)
            link = ""
        return link

    def parse_basic_info_posted(self, talk: BeautifulSoup) -> str:
        """ """
        try:
            posted = talk.find(class_="meta__val").text.replace("\n", "")
            month, year = posted.split(" ")[0], posted.split(" ")[1]
            month = month_map.get(month)
            posted = f"{year}-{month}-01"
        except Exception as e:
            logger.warning(e)
            posted = ""
        return posted

    @log(logger)
    def get_all_talks_current_page(self, url: str) -> None:
        """
        get basic info of each talks in current page
        """
        logger.info(f"Job Waiting in Queue: {self.jobs.qsize()}")
        soup = self.bs4_parser(url)
        talks = soup.find_all("div", class_="media__message")
        for talk in tqdm(talks):
            time.sleep(3)
            self.all_results += [self.parse_basic_info(talk)]

    @log(logger)
    def extract(self) -> List[dict]:
        """
        main logic
        """
        # get total pages
        url = tedtalk_base_url + "/talks?language=en&sort=newest"
        pages = self.get_page_num(url=url)
        # pages = 3
        logger.info(f"PAGES: {pages}")

        # create page url list
        page_url_list = [
            f"{url}&page={str(current_page)}" for current_page in range(1, pages + 1)
        ]

        # multi thread process to parse tedtalk metadata
        thread_number = len(page_url_list)
        self.multi_thread_process(
            all_url_list=page_url_list,
            process_func=self.get_all_talks_current_page,
            thread_num=thread_number,
        )

        return self.all_results
