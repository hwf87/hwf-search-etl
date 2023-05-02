import sys
import pytest
from typing import List
from bs4 import BeautifulSoup

sys.path.append("..")
from src.houzz.houzz_data_extractor import HouzzExtractor
from src.news.news_data_extractor import NewsExtractor
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor


def read_html_to_soup(file_path: str) -> BeautifulSoup:
    with open(file_path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "lxml")
    return soup


class Test_HouzzExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize(
        "url, expect", [("https://www.houzz.com/ideabooks/p/0", 1000)]
    )
    def test_get_story_count(self, url, expect):
        """ """
        HE = HouzzExtractor()
        answer = HE.get_story_count(url)
        assert answer >= expect

    @pytest.mark.parametrize(
        "story_count, start_page, end_page, expect",
        [
            (
                1000,
                0,
                3,
                [
                    "https://www.houzz.com/ideabooks/p/0",
                    "https://www.houzz.com/ideabooks/p/11",
                    "https://www.houzz.com/ideabooks/p/22",
                ],
            ),
            (
                1000,
                15,
                18,
                [
                    "https://www.houzz.com/ideabooks/p/165",
                    "https://www.houzz.com/ideabooks/p/176",
                    "https://www.houzz.com/ideabooks/p/187",
                ],
            ),
        ],
    )
    def test_get_page_url_list(
        self, story_count: int, start_page: int, end_page: int, expect: List[str]
    ):
        """ """
        HE = HouzzExtractor()
        answer = HE.get_page_url_list(
            story_count=story_count, start_page=start_page, end_page=end_page
        )

        assert answer == expect

    @pytest.mark.parametrize(
        "houzz_story_soup_path, expect",
        [
            (
                "./test/test_data/houzz_story_soup.html",
                "https://www.houzz.com/magazine/10-fresh-furniture-and-decor-trends-for-spring-stsetivw-vs~167402436",
            )
        ],
    )
    def test_get_story_link_from_page(self, houzz_story_soup_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_soup = read_html_to_soup(file_path=houzz_story_soup_path)
        answer = HE.get_story_link_from_page(story=story_soup)

        assert answer == expect

    @pytest.mark.parametrize("", [])
    def test_get_stories_from_page(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_unique_story_id(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_detail_form_story_page(self):
        """ """
        HouzzExtractor()


class Test_NewsExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """
        NewsExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_playlist_id(self):
        """ """
        NewsExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_video_id_list(self):
        """ """
        NewsExtractor()

    @pytest.mark.parametrize("", [])
    def test_parse_video_metadata(self):
        """ """
        NewsExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_video_info(self):
        """ """
        NewsExtractor()


class Test_TedtalkExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """
        TedtalkExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_page_num(self):
        """ """
        TedtalkExtractor()

    @pytest.mark.parametrize("", [])
    def test_parse_extra_info(self):
        """ """
        TedtalkExtractor()

    @pytest.mark.parametrize("", [])
    def test_parse_basic_info(self):
        """ """
        TedtalkExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_all_talks_current_page(self):
        """ """
        TedtalkExtractor()
