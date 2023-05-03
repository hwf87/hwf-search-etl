import sys
import pytest
from typing import List

sys.path.append("..")
from src.houzz.houzz_data_transformer import HouzzTransformer
from src.news.news_data_transformer import NewsTransformer
from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer
from test.utils import read_json_data, get_round_embeddings


class Test_HouzzTransformer:
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
        HT = HouzzTransformer()
        answer = HT.transform(input_json_list=input_json_list)
        expect = read_json_data(test_data_path)

        # item 1
        answer_1_columns = list(answer[0].keys())
        expect_1_columns = list(expect[0].keys())
        answer_1_embedding = get_round_embeddings(
            embeddings=answer[0]["embeddings"], num=3
        )
        expect_1_embedding = get_round_embeddings(
            embeddings=expect[0]["embeddings"], num=3
        )

        # item 2
        answer_2_columns = list(answer[1].keys())
        expect_2_columns = list(expect[1].keys())
        answer_2_embedding = get_round_embeddings(
            embeddings=answer[1]["embeddings"], num=3
        )
        expect_2_embedding = get_round_embeddings(
            embeddings=expect[1]["embeddings"], num=3
        )

        assert answer_1_columns == expect_1_columns
        assert answer_2_columns == expect_2_columns
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding

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
        # round embedings digits
        answer_1_embedding = get_round_embeddings(embeddings=answer[0], num=3)
        answer_2_embedding = get_round_embeddings(embeddings=answer[1], num=3)
        expect_1_embedding = get_round_embeddings(embeddings=expect[0], num=3)
        expect_2_embedding = get_round_embeddings(embeddings=expect[1], num=3)

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding


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
        answer_1_columns = list(answer[0].keys())
        expect_1_columns = list(expect[0].keys())
        answer_1_embedding = get_round_embeddings(
            embeddings=answer[0]["embeddings"], num=3
        )
        expect_1_embedding = get_round_embeddings(
            embeddings=expect[0]["embeddings"], num=3
        )

        # item 2
        answer_2_columns = list(answer[1].keys())
        expect_2_columns = list(expect[1].keys())
        answer_2_embedding = get_round_embeddings(
            embeddings=answer[1]["embeddings"], num=3
        )
        expect_2_embedding = get_round_embeddings(
            embeddings=expect[1]["embeddings"], num=3
        )

        assert answer_1_columns == expect_1_columns
        assert answer_2_columns == expect_2_columns
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding

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

        # round embedings digits
        answer_1_embedding = get_round_embeddings(embeddings=answer[0], num=3)
        answer_2_embedding = get_round_embeddings(embeddings=answer[1], num=3)
        expect_1_embedding = get_round_embeddings(embeddings=expect[0], num=3)
        expect_2_embedding = get_round_embeddings(embeddings=expect[1], num=3)

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding


class Test_TedtalkTransformer:
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
        TT = TedtalkTransformer()
        answer = TT.transform(input_json_list=input_json_list)
        expect = read_json_data(test_data_path)

        # item 1
        answer_1_columns = list(answer[0].keys())
        expect_1_columns = list(expect[0].keys())
        answer_1_embedding = get_round_embeddings(
            embeddings=answer[0]["embeddings"], num=3
        )
        expect_1_embedding = get_round_embeddings(
            embeddings=expect[0]["embeddings"], num=3
        )

        # item 2
        answer_2_columns = list(answer[1].keys())
        expect_2_columns = list(expect[1].keys())
        answer_2_embedding = get_round_embeddings(
            embeddings=answer[1]["embeddings"], num=3
        )
        expect_2_embedding = get_round_embeddings(
            embeddings=expect[1]["embeddings"], num=3
        )

        assert answer_1_columns == expect_1_columns
        assert answer_2_columns == expect_2_columns
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding

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

        # round embedings digits
        answer_1_embedding = get_round_embeddings(embeddings=answer[0], num=3)
        answer_2_embedding = get_round_embeddings(embeddings=answer[1], num=3)
        expect_1_embedding = get_round_embeddings(embeddings=expect[0], num=3)
        expect_2_embedding = get_round_embeddings(embeddings=expect[1], num=3)

        assert len(answer) == 2
        assert len(answer[0]) == 384
        assert len(answer[1]) == 384
        assert answer_1_embedding == expect_1_embedding
        assert answer_2_embedding == expect_2_embedding
