import sys
import pytest

sys.path.append("..")
from src.CrawlerBase import ExtractorBase, TransformerBase, LoaderBase


class ExtractorBaseConcrete(ExtractorBase):
    def __init__(self):
        super().__init__()

    def extract(self):
        pass


class TransformerBaseConcrete(TransformerBase):
    def __init__(self):
        super().__init__()

    def transform(self):
        pass


class LoaderBaseConcrete(LoaderBase):
    def __init__(self):
        super().__init__()

    def transform(self):
        pass


class Test_ExtractorBase:
    @pytest.mark.parametrize(
        "url, expect",
        [
            ("https://www.google.com", "Google"),
            ("https://www.houzz.com", "Houzz"),
            ("https://www.ted.com/talks", "TED Talks"),
        ],
    )
    def test_bs4_parser(self, url, expect):
        """ """
        EBC = ExtractorBaseConcrete()
        soup = EBC.bs4_parser(url)
        answer = soup.head.title.text
        assert expect in answer

    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """
        ExtractorBaseConcrete()

    @pytest.mark.parametrize("", [])
    def test_date_converter(self):
        """ """
        ExtractorBaseConcrete()

    @pytest.mark.parametrize("", [])
    def test_multi_thread_process(self):
        """ """
        ExtractorBaseConcrete()

    @pytest.mark.parametrize("", [])
    def test_consume_jobs(self):
        """ """
        ExtractorBaseConcrete()


class Test_TransformerBase:
    @pytest.mark.parametrize("", [])
    def test_chunks(self):
        """ """
        TransformerBaseConcrete()


class Test_LoaderBase:
    @pytest.mark.parametrize("", [])
    def test_get_es_client(self):
        """ """
        LoaderBaseConcrete()

    @pytest.mark.parametrize("", [])
    def test_check_index(self):
        """ """
        LoaderBaseConcrete()

    @pytest.mark.parametrize("", [])
    def test_create_index(self):
        """ """
        LoaderBaseConcrete()
