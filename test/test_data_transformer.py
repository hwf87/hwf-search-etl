import sys
import pytest

sys.path.append("..")
from src.houzz.houzz_data_transformer import HouzzTransformer
from src.news.news_data_transformer import NewsTransformer
from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer


class Test_HouzzTransformer:
    def test_transform(self):
        """ """
        HouzzTransformer()
        assert 1 == 1

    def test_inference(self):
        """ """
        assert 1 == 1


class Test_NewsTransformer:
    @pytest.mark.parametrize("", [])
    def test_transform(self):
        """ """
        NewsTransformer()

    @pytest.mark.parametrize("", [])
    def test_inference(self):
        """ """
        NewsTransformer()


class Test_TedtalkTransformer:
    @pytest.mark.parametrize("", [])
    def test_transform(self):
        """ """
        TedtalkTransformer()

    @pytest.mark.parametrize("", [])
    def test_inference(self):
        """ """
        TedtalkTransformer()
