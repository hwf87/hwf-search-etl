import sys
import pytest
from typing import Any, List
from datetime import date

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

    @pytest.mark.parametrize(
        "lst, num, expect",
        [
            (["a", "b", "c"], 1, [["a"], ["b"], ["c"]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
            ([1, 2, 3], 2, [[1, 2], [3]]),
            ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4, 5]]),
        ],
    )
    def test_chunks(self, lst: List[Any], num: int, expect: List[List[Any]]):
        """ """
        EBC = ExtractorBaseConcrete()
        answer = EBC.chunks(lst, num)
        answer = [ans for ans in answer]

        assert answer == expect

    @pytest.mark.parametrize(
        "input, expect",
        [
            ("5 days ago", 5),
            ("yesterday", 1),
            ("2 hours ago", 0),
            ("1 hour ago", 0),
            ("ABC", 0),
        ],
    )
    def test_date_converter(self, input: str, expect: str):
        """ """
        EBC = ExtractorBaseConcrete()
        date_result = EBC.date_converter(input)
        result = date(
            int(date_result[0:4]), int(date_result[5:7]), int(date_result[8:10])
        )
        delta = date.today() - result
        answer = delta.days

        assert len(date_result) == 10
        assert answer == expect

    @pytest.mark.parametrize("", [])
    def test_multi_thread_process(self):
        """ """
        ExtractorBaseConcrete()

    @pytest.mark.parametrize(
        "queue_items, expect",
        [
            (["https://abc.com", "https://google.com"], ["abc.com", "google.com"]),
        ],
    )
    def test_consume_jobs(self, queue_items: List[Any], expect: bool):
        """ """
        EBC = ExtractorBaseConcrete()
        # add to queue
        for q in queue_items:
            EBC.jobs.put(q)
        # temp array and function
        EBC.temp = []

        def push_back_remove_https(url: str):
            url = url.replace("https://", "")
            EBC.temp.append(url)

        # execute
        EBC.consume_jobs(job_queue=EBC.jobs, func=push_back_remove_https)
        answer = EBC.temp

        assert answer == expect


class Test_TransformerBase:
    @pytest.mark.parametrize(
        "lst, num, expect",
        [
            (["a", "b", "c"], 1, [["a"], ["b"], ["c"]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
            ([1, 2, 3], 2, [[1, 2], [3]]),
            ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4, 5]]),
        ],
    )
    def test_chunks(self, lst: List[Any], num: int, expect: List[List[Any]]):
        """ """
        TBC = TransformerBaseConcrete()
        answer = TBC.chunks(lst, num)
        answer = [ans for ans in answer]

        assert answer == expect


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
