import sys
import pytest

sys.path.append("..")
from src.houzz.houzz_data_extractor import HouzzExtractor
from src.news.news_data_extractor import NewsExtractor
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor


class Test_HouzzExtractor:
    def test_extract(self):
        """ """
        assert 1 == 1

    @pytest.mark.parametrize("", [])
    def test_get_story_count(self):
        """ """
    
    @pytest.mark.parametrize("", [])
    def test_get_page_url_list(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_story_link_from_page(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_stories_from_page(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_unique_story_id(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_detail_form_story_page(self):
        """ """
        

class Test_NewsExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_playlist_id(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_video_id_list(self):
        """ """
        
    @pytest.mark.parametrize("", [])
    def test_parse_video_metadata(self):
        """ """
    
    @pytest.mark.parametrize("", [])
    def test_get_video_info(self):
        """ """


class Test_TedtalkExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_page_num(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_parse_extra_info(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_parse_basic_info(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_get_all_talks_current_page(self):
        """ """


