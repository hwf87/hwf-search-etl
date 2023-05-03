import sys
import pytest
from elasticmock import elasticmock

from typing import Any, List, Dict

sys.path.append("..")
from src.houzz.houzz_data_loader import HouzzLoader
from src.news.news_data_loader import NewsLoader
from src.tedtalk.tedtalk_data_loader import TedtalkLoader


class Test_HouzzLoader:
    @elasticmock
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        HL = HouzzLoader()
        es = HL.get_es_client()
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
        HL.load(documents=documents)

        # check load results
        index_exist = HL.check_index(index_name="houzz", es=es)
        doc_1_exist = es.get(index="houzz", id="item-1234")["found"]
        doc_2_exist = es.get(index="houzz", id="item-5678")["found"]

        assert index_exist is True
        assert doc_1_exist is True
        assert doc_2_exist is True

    @pytest.mark.parametrize(
        "op_type, index_name, documents, expect",
        [
            (
                "index",
                "mock_test",
                [
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
                ],
                [
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
                ],
            )
        ],
    )
    def test_load_action_batch(
        self,
        op_type: str,
        index_name: str,
        documents: List[Dict[Any, Any]],
        expect: List[Dict[Any, Any]],
    ):
        """ """
        HL = HouzzLoader()
        answer = HL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect


class Test_NewsLoader:
    @elasticmock
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        NL = NewsLoader()
        es = NL.get_es_client()
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
        NL.load(documents=documents)

        # check load results
        index_exist = NL.check_index(index_name="cnn", es=es)
        doc_1_exist = es.get(index="cnn", id="item-1234")["found"]
        doc_2_exist = es.get(index="cnn", id="item-5678")["found"]

        assert index_exist is True
        assert doc_1_exist is True
        assert doc_2_exist is True

    @pytest.mark.parametrize(
        "op_type, index_name, documents, expect",
        [
            (
                "index",
                "mock_test",
                [
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
                ],
                [
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
                ],
            )
        ],
    )
    def test_load_action_batch(
        self,
        op_type: str,
        index_name: str,
        documents: List[Dict[Any, Any]],
        expect: List[Dict[Any, Any]],
    ):
        """ """
        NL = NewsLoader()
        answer = NL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect


class Test_TedtalkLoader:
    @elasticmock
    @pytest.mark.parametrize("", [])
    def test_load(self):
        """ """
        TL = TedtalkLoader()
        es = TL.get_es_client()
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
        TL.load(documents=documents)

        # check load results
        index_exist = TL.check_index(index_name="tedtalk", es=es)
        doc_1_exist = es.get(index="tedtalk", id="item-1234")["found"]
        doc_2_exist = es.get(index="tedtalk", id="item-5678")["found"]

        assert index_exist is True
        assert doc_1_exist is True
        assert doc_2_exist is True

    @pytest.mark.parametrize(
        "op_type, index_name, documents, expect",
        [
            (
                "index",
                "mock_test",
                [
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
                ],
                [
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
                ],
            )
        ],
    )
    def test_load_action_batch(
        self,
        op_type: str,
        index_name: str,
        documents: List[Dict[Any, Any]],
        expect: List[Dict[Any, Any]],
    ):
        """ """
        TL = TedtalkLoader()
        answer = TL.load_action_batch(
            op_type=op_type, index_name=index_name, documents=documents
        )
        answer = [ans for ans in answer]

        assert answer == expect
