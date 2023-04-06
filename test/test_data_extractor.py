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


class Test_NewsExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """


class Test_TedtalkExtractor:
    @pytest.mark.parametrize("", [])
    def test_extract(self):
        """ """
