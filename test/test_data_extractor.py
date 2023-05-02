import sys
import pytest
from typing import List, Dict

sys.path.append("..")
from src.houzz.houzz_data_extractor import HouzzExtractor
from src.news.news_data_extractor import NewsExtractor
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor
from test.utils import read_html_to_soup, read_json_data


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

    @pytest.mark.parametrize(
        "houzz_story_path, expect",
        [
            (
                "./test/test_data/houzz_story_soup.html",
                "https://st.hzcdn.com/fimgs/e2b1ef7d044aa6ad_0686-w458-h268-b0-p0--.jpg",
            )
        ],
    )
    def test_get_story_image_from_page(self, houzz_story_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story = read_html_to_soup(houzz_story_path)
        answer = HE.get_story_image_from_page(story=story)

        assert answer == expect

    @pytest.mark.parametrize(
        "url, expect_stroy_url_prefix, expect_image_url_prefix",
        [
            (
                "https://www.houzz.com/ideabooks/p/0",
                "https://www.houzz.com",
                "https://st.hzcdn.com/fimgs",
            )
        ],
    )
    def test_get_stories_from_page(
        self, url: str, expect_stroy_url_prefix: str, expect_image_url_prefix: str
    ):
        """ """
        HE = HouzzExtractor()
        HE.get_stories_from_page(url=url)
        stroy_url = list(HE.story_list[0].keys())[0]
        image_url = list(HE.story_list[0].values())[0]["images"]

        assert len(HE.story_list) == 11
        assert expect_stroy_url_prefix in stroy_url
        assert expect_image_url_prefix in image_url

    @pytest.mark.parametrize(
        "url, expect",
        [
            (
                "https://www.houzz.com/magazine/10-fresh-furniture-and-decor-trends-for-spring-stsetivw-vs~167402436",
                "167402436",
            ),
            (
                "https://www.houzz.com/magazine/pro-tips-for-lighting-10-rooms-and-outdoor-areas-stsetivw-vs~136224262",
                "136224262",
            ),
        ],
    )
    def test_get_unique_story_id(self, url: str, expect: str):
        """ """
        HE = HouzzExtractor()
        answer = HE.get_unique_story_id(url=url)
        assert answer == expect

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [("./test/test_data/houzz_story_meta_soup.html", "2023-05-02")],
    )
    def test_get_story_meta_posted(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)

        answer = HE.get_story_meta_posted(story_meta)
        assert answer == expect

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_tags(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_related_tags(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_main_content(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_author(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_description(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize("", [])
    def test_get_story_meta_title(self):
        """ """
        HouzzExtractor()

    @pytest.mark.parametrize(
        "url_dict, expect_story_path",
        [
            (
                {
                    "https://www.houzz.com/magazine/bathroom-of-the-week-warm-modern-style-in-a-midcentury-ranch-stsetivw-vs~166624763": {
                        "images": "https://st.hzcdn.com/fimgs/7a1134f6036bd9d5_6289-w458-h268-b0-p0--.jpg"
                    }
                },
                "./test/test_data/houzz_story_166624763.json",
            )
        ],
    )
    def test_get_detail_form_story_page(
        self, url_dict: Dict[str, Dict[str, str]], expect_story_path: str
    ):
        """ """
        HE = HouzzExtractor()
        HE.get_detail_form_story_page(url=url_dict)
        expect = read_json_data(expect_story_path)
        answer = HE.story_detail_list

        assert answer[0]["uid"] == expect[0]["uid"]
        assert answer[0]["title"] == expect[0]["title"]
        assert answer[0]["description"] == expect[0]["description"]
        assert answer[0]["author"] == expect[0]["author"]
        assert answer[0]["link"] == expect[0]["link"]
        assert answer[0]["tags"] == expect[0]["tags"]
        assert answer[0]["related_tags"] == expect[0]["related_tags"]
        assert answer[0]["posted"] == expect[0]["posted"]
        assert answer[0]["images"] == expect[0]["images"]


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
