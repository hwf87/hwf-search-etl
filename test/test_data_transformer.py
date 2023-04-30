import sys
import json
import pytest
from typing import List

sys.path.append("..")
from src.houzz.houzz_data_transformer import HouzzTransformer
from src.news.news_data_transformer import NewsTransformer
from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer


def read_json_data(path: str) -> json:
    f = open(path)
    json_data = json.load(f)
    return json_data


class Test_HouzzTransformer:
    def test_transform(self):
        """ """
        HouzzTransformer()
        assert 1 == 1

    @pytest.mark.parametrize(
        "multi_sentence, test_data_path",
        [
            (
                ["How are you today?", "I'm fine thank you!"],
                "./test/test_data/greeting_embedding.json",
            )
        ],
    )
    def test_inference(self, multi_sentence: List[str], test_data_path: str):
        """ """
        HT = HouzzTransformer()
        answer = HT.inference(batch_texts=multi_sentence)
        expect = read_json_data(test_data_path)["embeddings"]

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer[0] == expect[0]
        assert answer[1] == expect[1]


class Test_NewsTransformer:
    @pytest.mark.parametrize(
        "input_json_list, test_data_path",
        [
            (
                [
                    {
                        "uid": "item-1234",
                        "title": "Sample Item",
                        "details": "This is a happy item 1234",
                        "posted": "2023-04-15",
                        "tags": ["fastapi", "python", "web development"],
                        "link": "https://example.com/sample-item",
                        "highlight": {},
                    },
                    {
                        "uid": "item-5678",
                        "title": "Sample Item",
                        "details": "Hello, This is an unhappy item 5678",
                        "posted": "2023-04-15",
                        "tags": ["fastapi", "python", "web development"],
                        "link": "https://example.com/sample-item",
                        "highlight": {},
                    },
                ],
                "./test/test_data/sample_item.json",
            )
        ],
    )
    def test_transform(self, input_json_list: List[dict], test_data_path: str):
        """ """
        NT = NewsTransformer()
        answer = NT.transform(input_json_list=input_json_list)
        expect = read_json_data(test_data_path)

        # item 1
        # answer_1_embedding = answer[0]["embeddings"]
        # expect_1_embedding = expect[0]["embeddings"]
        answer_1_columns = list(answer[0].keys())
        expect_1_columns = list(expect[0].keys())

        # item 2
        # answer_2_embedding = answer[1]["embeddings"]
        # expect_2_embedding = expect[1]["embeddings"]
        answer_2_columns = list(answer[1].keys())
        expect_2_columns = list(expect[1].keys())

        # assert answer_1_embedding == expect_1_embedding
        assert answer_1_columns == expect_1_columns
        assert answer_2_columns == expect_2_columns

    @pytest.mark.parametrize(
        "multi_sentence, test_data_path",
        [
            (
                ["How are you today?", "I'm fine thank you!"],
                "./test/test_data/greeting_embedding.json",
            )
        ],
    )
    def test_inference(self, multi_sentence: List[str], test_data_path: str):
        """ """
        NT = NewsTransformer()
        answer = NT.inference(batch_texts=multi_sentence)
        expect = read_json_data(test_data_path)["embeddings"]

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer[0] == expect[0]
        assert answer[1] == expect[1]


class Test_TedtalkTransformer:
    @pytest.mark.parametrize("", [])
    def test_transform(self):
        """ """
        TedtalkTransformer()

    @pytest.mark.parametrize(
        "multi_sentence, test_data_path",
        [
            (
                ["How are you today?", "I'm fine thank you!"],
                "./test/test_data/greeting_embedding.json",
            )
        ],
    )
    def test_inference(self, multi_sentence: List[str], test_data_path: str):
        """ """
        TT = TedtalkTransformer()
        answer = TT.inference(batch_texts=multi_sentence)
        expect = read_json_data(test_data_path)["embeddings"]

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer[0] == expect[0]
        assert answer[1] == expect[1]
