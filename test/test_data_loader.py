import sys
import pytest

# from typing import Any, List, Dict

sys.path.append("..")
from src.houzz.houzz_data_loader import HouzzLoader
from src.news.news_data_loader import NewsLoader
from src.tedtalk.tedtalk_data_loader import TedtalkLoader


class Test_HouzzLoader:
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        HouzzLoader()

    # @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        # expect: List[Dict[Any, Any]]
        HL = HouzzLoader()
        op_type = "index"
        index_name = "mock_test"
        documents = [
            {
                "uid": "item-1234",
                "title": "Sample Item",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
            {
                "uid": "item-5678",
                "title": "Sample Item 2",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
        ]

        expect = [
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-1234",
                "_source": {
                    "uid": "item-1234",
                    "title": "Sample Item",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-5678",
                "_source": {
                    "uid": "item-5678",
                    "title": "Sample Item 2",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
        ]

        answer = HL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect


class Test_NewsLoader:
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        NewsLoader()

    # @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        # expect: List[Dict[Any, Any]]
        NL = NewsLoader()
        op_type = "index"
        index_name = "mock_test"
        documents = [
            {
                "uid": "item-1234",
                "title": "Sample Item",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
            {
                "uid": "item-5678",
                "title": "Sample Item 2",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
        ]

        expect = [
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-1234",
                "_source": {
                    "uid": "item-1234",
                    "title": "Sample Item",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-5678",
                "_source": {
                    "uid": "item-5678",
                    "title": "Sample Item 2",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
        ]

        answer = NL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect


class Test_TedtalkLoader:
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        TedtalkLoader()

    # @pytest.mark.parametrize("", [])
    def test_load_action_batch(self):
        """ """
        # expect: List[Dict[Any, Any]]
        TL = TedtalkLoader()
        op_type = "index"
        index_name = "mock_test"
        documents = [
            {
                "uid": "item-1234",
                "title": "Sample Item",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
            {
                "uid": "item-5678",
                "title": "Sample Item 2",
                "details": "This is a sample item",
                "posted": "2023-04-15",
                "tags": ["fastapi", "python", "web development"],
                "link": "https://example.com/sample-item",
                "highlight": {},
            },
        ]

        expect = [
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-1234",
                "_source": {
                    "uid": "item-1234",
                    "title": "Sample Item",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
            {
                "_op_type": "index",
                "_index": "mock_test",
                "_id": "item-5678",
                "_source": {
                    "uid": "item-5678",
                    "title": "Sample Item 2",
                    "details": "This is a sample item",
                    "posted": "2023-04-15",
                    "tags": ["fastapi", "python", "web development"],
                    "link": "https://example.com/sample-item",
                    "highlight": {},
                },
            },
        ]

        answer = TL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect
