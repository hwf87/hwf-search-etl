import sys
import pytest

sys.path.append("..")
from src.houzz.houzz_data_loader import HouzzLoader
from src.news.news_data_loader import NewsLoader
from src.tedtalk.tedtalk_data_loader import TedtalkLoader


class Test_HouzzLoader:
    def test_load(self):
        """ """
        HouzzLoader()
        assert 1 == 1

    @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        HouzzLoader()


class Test_NewsLoader:
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        NewsLoader()

    @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        NewsLoader()


class Test_TedtalkLoader:
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        TedtalkLoader()

    @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        TedtalkLoader()
