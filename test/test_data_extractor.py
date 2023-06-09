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
                "./test/test_data/houzz/houzz_story_soup.html",
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
                "./test/test_data/houzz/houzz_story_soup.html",
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
        [("./test/test_data/houzz/houzz_story_meta_soup.html", "2023-03-23")],
    )
    def test_get_story_meta_posted(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_posted(story_meta)

        assert answer == expect

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                ["Lighting", "Decorating Guides"],
            )
        ],
    )
    def test_get_story_meta_tags(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_tags(story_meta)

        assert answer == expect

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                [
                    "Sofas",
                    "Lighting",
                    "Bathroom Vanity  Lighting",
                    "Chandeliers",
                    "Floor Lamps",
                    "Pendant Lighting",
                ],
            )
        ],
    )
    def test_get_story_meta_related_tags(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_related_tags(story_meta)
        answer = [ans.replace("\n                    ", "") for ans in answer]

        assert set(answer) == set(expect)

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                "No one lighting scheme will work for every room or area of your home.",
            )
        ],
    )
    def test_get_story_meta_main_content(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_main_content(story_meta)
        answer = answer.replace("\n                ", " ").replace("\n", "")

        assert expect in answer

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                "Bryan Anthony",
            )
        ],
    )
    def test_get_story_meta_author(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_author(story_meta)

        assert answer == expect

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                "Get professional advice for lighting your kitchen, bathroom, living room, office, patio and more",
            )
        ],
    )
    def test_get_story_meta_description(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_description(story_meta)
        answer = answer.replace("              ", " ").replace("\n", "")

        assert answer == expect

    @pytest.mark.parametrize(
        "story_meta_path, expect",
        [
            (
                "./test/test_data/houzz/houzz_story_meta_soup.html",
                "Pro Tips for Lighting 10 Rooms and Outdoor Areas",
            )
        ],
    )
    def test_get_story_meta_title(self, story_meta_path: str, expect: str):
        """ """
        HE = HouzzExtractor()
        story_meta = read_html_to_soup(story_meta_path)
        answer = HE.get_story_meta_title(story_meta)
        assert answer == expect

    @pytest.mark.parametrize(
        "url_dict, expect_story_path",
        [
            (
                {
                    "https://www.houzz.com/magazine/pro-tips-for-lighting-10-rooms-and-outdoor-areas-stsetivw-vs~136224262": {
                        "images": "https://st.hzcdn.com/fimgs/pictures/living-rooms/guest-cottage-kate-nelson-interiors-img~b2212fa80fb6c96a_4602-1-a60d5f1-w458-h268-b0-p0.jpg"
                    }
                },
                "./test/test_data/houzz/houzz_story_136224262.json",
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
        assert answer[0]["details"] == expect[0]["details"]
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

    @pytest.mark.parametrize(
        "channel_username, expect", [("CNN", "UUupvZG-5ko_eiXAupbDfxWw")]
    )
    def test_get_playlist_id(self, channel_username: str, expect: str):
        """ """
        NE = NewsExtractor()
        answer = NE.get_playlist_id(channel_username=channel_username)

        assert answer == expect

    @pytest.mark.parametrize(
        "playlist_id, results_per_page, pages, expect",
        [
            ("UUupvZG-5ko_eiXAupbDfxWw", 1, 3, 3),
            ("UUupvZG-5ko_eiXAupbDfxWw", 5, 5, 25),
            ("UUupvZG-5ko_eiXAupbDfxWw", 50, 2, 100),
        ],
    )
    def test_get_video_id_list(
        self, playlist_id: str, results_per_page: int, pages: int, expect: int
    ):
        """ """
        NE = NewsExtractor()
        totalResults, nextPageToken, video_id_list = NE.get_video_id_list(
            playlist_id=playlist_id, results_per_page=results_per_page, pages=pages
        )

        assert totalResults >= 10000
        assert type(nextPageToken) == str
        assert len(video_id_list) == expect

    @pytest.mark.parametrize(
        "meta_path, info_path",
        [
            (
                "./test/test_data/news/news_meta_uQkYUiSqUrY.json",
                "./test/test_data/news/news_info_uQkYUiSqUrY.json",
            ),
            (
                "./test/test_data/news/news_meta_FzwYMS2zzz0.json",
                "./test/test_data/news/news_info_FzwYMS2zzz0.json",
            ),
        ],
    )
    def test_parse_video_metadata(self, meta_path: str, info_path: str):
        """ """
        NE = NewsExtractor()
        metadata = read_json_data(meta_path)
        answer = NE.parse_video_metadata(metadata=metadata)
        expect = read_json_data(info_path)[0]

        assert answer == expect

    @pytest.mark.parametrize(
        "video_id_list, expect_news_info_path",
        [
            (["uQkYUiSqUrY"], "./test/test_data/news/news_info_uQkYUiSqUrY.json"),
            (["FzwYMS2zzz0"], "./test/test_data/news/news_info_FzwYMS2zzz0.json"),
        ],
    )
    def test_get_video_info(self, video_id_list: List[str], expect_news_info_path: str):
        """ """
        NE = NewsExtractor()
        expect = read_json_data(expect_news_info_path)
        answer = NE.get_video_info(video_id_list=video_id_list)

        # We did not assert to compare likes, comment count and views
        # Since they might change quite frequently
        assert answer[0]["uid"] == expect[0]["uid"]
        assert answer[0]["channel"] == expect[0]["channel"]
        assert answer[0]["tags"] == expect[0]["tags"]
        assert answer[0]["posted"] == expect[0]["posted"]
        assert answer[0]["link"] == expect[0]["link"]
        assert answer[0]["title"] == expect[0]["title"]
        assert answer[0]["details"] == expect[0]["details"]


class Test_TedtalkExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """
        TedtalkExtractor()

    @pytest.mark.parametrize(
        "url, expect", [("https://www.ted.com/talks?language=en&sort=newest", 146)]
    )
    def test_get_page_num(self, url: str, expect: int):
        """ """
        TE = TedtalkExtractor()
        answer = TE.get_page_num(url=url)

        assert answer >= expect

    @pytest.mark.parametrize(
        "talk_url, expect",
        [
            (
                "https://www.ted.com/talks/andrew_smith_why_do_we_eat_popcorn_at_the_movies?language=en",
                [
                    "Soft percussion and a toasty scent mark the violent transformation of tough seeds into cloud-like puffs.",
                    [
                        "culture",
                        "education",
                        "food",
                        "history",
                        "TED-Ed",
                        "animation",
                        "indigenous peoples",
                    ],
                    372043,
                ],
            )
        ],
    )
    def test_parse_extra_info(self, talk_url: str, expect: str):
        """ """
        TE = TedtalkExtractor()
        details, tags, views = TE.parse_extra_info(talk_url=talk_url)

        assert expect[0] in details
        assert tags == expect[1]
        assert int(views) >= expect[2]

    @pytest.mark.parametrize(
        "tedtalk_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_soup.html",
                "Soft percussion and a toasty scent mark the violent transformation of tough seeds into cloud-like puffs.",
            )
        ],
    )
    def test_parse_extra_info_details(self, tedtalk_soup_path: str, expect: str):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_soup_path)
        answer = TE.parse_extra_info_details(soup=tedtalk_soup)
        answer = answer.replace("\n                            ", " ")

        assert expect in answer

    @pytest.mark.parametrize(
        "tedtalk_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_soup.html",
                [
                    "culture",
                    "education",
                    "food",
                    "history",
                    "TED-Ed",
                    "animation",
                    "indigenous peoples",
                ],
            )
        ],
    )
    def test_parse_extra_info_tags(self, tedtalk_soup_path: str, expect: str):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_soup_path)
        answer = TE.parse_extra_info_tags(soup=tedtalk_soup)
        answer = [ans.replace("\n", "") for ans in answer]

        assert answer == expect

    @pytest.mark.parametrize(
        "tedtalk_soup_path, expect",
        [("./test/test_data/tedtalk/tedtalk_soup.html", "372052")],
    )
    def test_parse_extra_info_views(self, tedtalk_soup_path: str, expect: str):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_soup_path)
        answer = TE.parse_extra_info_views(soup=tedtalk_soup)
        answer = answer.replace("\n", "")

        assert answer == expect

    @pytest.mark.parametrize(
        "tedtalk_media_message_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_media_message_soup.html",
                {
                    "uid": "shannon_n_tessier_can_you_freeze_your_body_and_come_back_to_life",
                    "author": "Shannon N. Tessier",
                    "title": "Can you freeze your body and come back to life?",
                    "link": "https://www.ted.com/talks/shannon_n_tessier_can_you_freeze_your_body_and_come_back_to_life?language=en",
                    "posted": "2023-02-01",
                    "details": "In 1967, James Bedford had a plan to cheat death. He was the first person to be cryogenically frozen. This process promised to preserve his body until a theoretical future when humanity could cure any illness, and essentially, reverse death. So is it possible to freeze a human, preserve them indefinitely, and then thaw them out? Shannon N. Tessier explores the challenges of human cryopreservation. [Directed by Gavin Edwards, Movult, narrated by Pen-Pen Chen, music by Stephen LaRosa].",
                    "tags": [
                        "science",
                        "education",
                        "biology",
                        "medical research",
                        "TED-Ed",
                        "animation",
                        "human body",
                    ],
                    "views": "494399",
                },
            )
        ],
    )
    def test_parse_basic_info(self, tedtalk_media_message_soup_path: str, expect: str):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_media_message_soup_path)
        answer = TE.parse_basic_info(talk=tedtalk_soup)

        assert answer["uid"] == expect["uid"]
        assert answer["author"] == expect["author"]
        assert answer["link"] == expect["link"]
        assert answer["posted"] == expect["posted"]
        assert answer["tags"] == expect["tags"]

    @pytest.mark.parametrize(
        "tedtalk_media_message_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_media_message_soup.html",
                "Shannon N. Tessier",
            )
        ],
    )
    def test_parse_basic_info_author(
        self, tedtalk_media_message_soup_path: str, expect: str
    ):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_media_message_soup_path)
        answer = TE.parse_basic_info_author(talk=tedtalk_soup)

        assert answer == expect

    @pytest.mark.parametrize(
        "tedtalk_media_message_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_media_message_soup.html",
                "Can you freeze your body and come back to life?",
            )
        ],
    )
    def test_parse_basic_info_title(
        self, tedtalk_media_message_soup_path: str, expect: str
    ):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_media_message_soup_path)
        answer = TE.parse_basic_info_title(talk=tedtalk_soup)
        answer = answer.replace("            ", " ")

        assert answer == expect

    @pytest.mark.parametrize(
        "tedtalk_media_message_soup_path, expect",
        [
            (
                "./test/test_data/tedtalk/tedtalk_media_message_soup.html",
                "https://www.ted.com/talks/shannon_n_tessier_can_you_freeze_your_body_and_come_back_to_life?language=en",
            )
        ],
    )
    def test_parse_basic_info_link(
        self, tedtalk_media_message_soup_path: str, expect: str
    ):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_media_message_soup_path)
        answer = TE.parse_basic_info_link(talk=tedtalk_soup)

        assert answer == expect

    @pytest.mark.parametrize(
        "tedtalk_media_message_soup_path, expect",
        [("./test/test_data/tedtalk/tedtalk_media_message_soup.html", "2023-02-01")],
    )
    def test_parse_basic_info_posted(
        self, tedtalk_media_message_soup_path: str, expect: str
    ):
        """ """
        TE = TedtalkExtractor()
        tedtalk_soup = read_html_to_soup(tedtalk_media_message_soup_path)
        answer = TE.parse_basic_info_posted(talk=tedtalk_soup)

        assert answer == expect

    @pytest.mark.parametrize("", [])
    def test_get_all_talks_current_page(self):
        """ """
        TE = TedtalkExtractor()
        url = "https://www.ted.com/talks?language=en&page=1&sort=newest"
        TE.get_all_talks_current_page(url=url)
        answer = len(TE.all_results)
        expect = 36

        assert answer == expect
