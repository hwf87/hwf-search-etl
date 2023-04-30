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

    def test_inference(self):
        """ """
        assert 1 == 1


class Test_NewsTransformer:
    @pytest.mark.parametrize("", [])
    def test_transform(self):
        """ """
        NewsTransformer()

    @pytest.mark.parametrize(
        "multi_sentence, test_data_path",
        [
            (
                ["Hello world", "Thank god is Friday!"],
                "./test/test_data/helloworld_tgif_embedding.json",
            )
        ],
    )
    def test_inference(self, multi_sentence: List[str], test_data_path: str):
        """ """
        NT = NewsTransformer()
        answer = NT.inference(batch_texts=multi_sentence)
        expect = read_json_data(test_data_path)["embeddings"]

        assert answer[0] == expect[0]
        assert answer[1] == expect[1]


class Test_TedtalkTransformer:
    @pytest.mark.parametrize("", [])
    def test_transform(self):
        """ """
        TedtalkTransformer()

    @pytest.mark.parametrize("", [])
    def test_inference(self):
        """ """
        TedtalkTransformer()
