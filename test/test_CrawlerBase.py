import sys
import pytest

sys.path.append("..")
from src.CrawlerBase import ExtractorBase, TransformerBase, LoaderBase


class Test_ExtractorBase:
    def test_bs4_parser(self):
        """ """
        assert 1 == 1

    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """


class Test_TransformerBase:
    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """


class Test_LoaderBase:
    @pytest.mark.parametrize("", [])
    def test_get_es_client(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_check_index(self):
        """ """

    @pytest.mark.parametrize("", [])
    def test_create_index(self):
        """ """
