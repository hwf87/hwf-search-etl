import sys
import pytest

sys.path.append("..")
from src.CrawlerBase import ExtractorBase, TransformerBase, LoaderBase


class Test_ExtractorBase:
    def test_bs4_parser(self):
        """ """
        ExtractorBase()
        assert 1 == 1

    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """
        ExtractorBase()

    @pytest.mark.parametrize("", [])
    def test_date_converter(self):
        """ """
        ExtractorBase()

    @pytest.mark.parametrize("", [])
    def test_multi_thread_process(self):
        """ """
        ExtractorBase()

    @pytest.mark.parametrize("", [])
    def test_consume_jobs(self):
        """ """
        ExtractorBase()


class Test_TransformerBase:
    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """
        TransformerBase()


class Test_LoaderBase:
    @pytest.mark.parametrize("", [])
    def test_get_es_client(self):
        """ """
        LoaderBase()

    @pytest.mark.parametrize("", [])
    def test_check_index(self):
        """ """
        LoaderBase()

    @pytest.mark.parametrize("", [])
    def test_create_index(self):
        """ """
        LoaderBase()
