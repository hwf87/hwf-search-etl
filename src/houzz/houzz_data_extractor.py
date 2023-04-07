# -*- coding: UTF-8 -*-

import sys
from typing import List

sys.path.append("../..")
from bs4 import BeautifulSoup
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger
from utils.config_parser import houzz_story_base_url, month_map, fn_

logger = get_logger(name=__name__)


class HouzzExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
        self.story_list = []
        self.story_detail_list = []

    @log(logger)
    def extract(self) -> List[dict]:
        """
        main logic
        """
        # get total story count
        start_page = 0
        story_count = self.get_story_count(
            url=houzz_story_base_url + str(start_page)
        )

        # list done all url pages
        page_url_list = self.get_page_url_list(
            story_count=story_count, 
            start_page=start_page
            , end_page=500
        )

        # start multi-thread to prase story url from each single collect page
        self.multi_thread_process(
            all_url_list=page_url_list,
            process_func=self.get_stories_from_page,
            thread_num=10,
        )

        # start multi-thread to parse story detail from each single story page
        story_url_list = [
            url for url in set(self.story_list) if "https://" in url
        ]
        self.multi_thread_process(
            all_url_list=story_url_list,
            process_func=self.get_detail_form_story_page,
            thread_num=10,
        )

        return self.story_detail_list

    @log(logger)
    def get_story_count(self, url: str) -> int:
        """ """
        soup = self.bs4_parser(url=url)
        count = soup.find(
            "span", class_="hz-browse-galleries__header-story-count"
        ).text
        count = int(count.split(" ")[0])

        return count

    @log(logger)
    def get_page_url_list(
        self,
        story_count: int,
        start_page: int = 0,
        end_page: int = None,
        story_per_page: int = 11,
    ) -> List[str]:
        """ """
        if end_page is None:
            end_page = int(story_count / story_per_page) + 1

        page_url_list = []
        for current_page in range(start_page, end_page):
            page_idx = current_page * story_per_page
            page_url = houzz_story_base_url + str(page_idx)
            page_url_list.append(page_url)

        return page_url_list

    def get_story_link_from_page(self, story: BeautifulSoup) -> str:
        """ """
        try:
            link = story.find(
                "a",
                class_="gallery-card__view-detail gallery-card__view-detail--full-story text-l",
            )["href"]
            link = link.replace(" ", "")
        except Exception as e:
            logger.warning(e)
            link = ""
        return link

    def get_stories_from_page(self, url: str) -> None:
        """
        URL:: https://www.houzz.com/ideabooks/p/{IDX}
        """
        logger.info(f"Job Waiting in Queue: {self.jobs.qsize()}")
        soup = self.bs4_parser(url=url)
        stories = soup.find_all(
            "div", class_="gallery-card hz-browse-galleries-list__gallery"
        )
        story_list_tmp = [
            self.get_story_link_from_page(story) for story in stories
        ]
        self.story_list += story_list_tmp

    def get_story_meta_posted(self, story: BeautifulSoup) -> str:
        """ """
        try:
            posted = story.find(
                "span", class_="hz-editorial-gallery-author-info__featured"
            ).text
            if "ago" in posted or "yesterday" in posted:
                posted = self.date_converter(input=posted)
            else:
                day, month, year = posted.split(" ")[1].replace(",", ""), posted.split(" ")[0], posted.split(" ")[2]
                month = month_map.get(month[:3], "")
                posted = f"{year}-{month}-{day}"
        except Exception as e:
            logger.warning(e)
            posted = ""
        return posted

    def get_story_meta_tags(self, story: BeautifulSoup) -> List[str]:
        """ """
        try:
            tags = story.find_all(
                "a",
                class_="hz-editorial-gallery-header-topics__topic__link hz-color-link hz-color-link--green hz-color-link--enabled",
            )
            tags = [tag.text for tag in tags]
        except Exception as e:
            logger.warning(e)
            tags = ""
        return tags

    def get_story_meta_related_tags(self, story: BeautifulSoup) -> List[str]:
        """ """
        try:
            related_tags = story.find_all(
                "div",
                class_="hz-editorial-gallery-related-categories__item__name",
            )
            related_tags = [r_tag.text for r_tag in related_tags]
        except Exception as e:
            logger.warning(e)
            related_tags = ""
        return related_tags

    def get_story_meta_main_content(self, story: BeautifulSoup) -> str:
        """ """
        try:
            main_content = story.find(
                "div", class_="hz-editorial-gallery-main-content"
            ).text
        except Exception as e:
            logger.warning(e)
            main_content = ""
        return main_content

    def get_story_meta_author(self, story: BeautifulSoup) -> str:
        """ """
        try:
            author = story.find(
                "a",
                class_="hz-editorial-gallery-author-info__name hz-color-link hz-color-link--none hz-color-link--enabled",
            ).text
        except Exception as e:
            logger.warning(e)
            author = ""
        return author

    def get_story_meta_description(self, story: BeautifulSoup) -> str:
        """ """
        try:
            description = story.find(
                "h2", class_="hz-editorial-gallery__subtitle"
            ).text
        except Exception as e:
            logger.warning(e)
            description = ""
        return description

    def get_story_meta_title(self, story: BeautifulSoup) -> str:
        """ """
        try:
            title = story.find(
                "h1", class_="hz-editorial-gallery__title"
            ).text
        except Exception as e:
            logger.warning(e)
            title = ""
        return title

    def get_unique_story_id(self, url: str) -> str:
        """ """
        story_id = url.split("~")[-1]
        return story_id

    @log(logger)
    def get_detail_form_story_page(self, url: str) -> None:
        """ """
        logger.info(f"Job Waiting in Queue: {self.jobs.qsize()}")
        soup = self.bs4_parser(url=url)
        story_detail = {
            fn_.uid: self.get_unique_story_id(url=url),
            fn_.title: self.get_story_meta_title(story=soup),
            fn_.description: self.get_story_meta_description(story=soup),
            fn_.author: self.get_story_meta_author(story=soup),
            fn_.link: url,
            fn_.details: self.get_story_meta_main_content(story=soup),
            fn_.tags: self.get_story_meta_tags(story=soup),
            fn_.related_tags: self.get_story_meta_related_tags(story=soup),
            fn_.posted: self.get_story_meta_posted(story=soup),
        }
        self.story_detail_list.append(story_detail)
