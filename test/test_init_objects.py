import sys
import pytest

sys.path.append("..")
from init_objects import InitObject


class Test_InitObject:
    @pytest.mark.parametrize(
        "config_path, expect",
        [
            (
                "./config/class_object.yaml",
                {
                    "extract": {
                        "src.news.news_data_extractor": {"news": "NewsExtractor"},
                        "src.tedtalk.tedtalk_data_extractor": {
                            "tedtalk": "TedtalkExtractor"
                        },
                        "src.houzz.houzz_data_extractor": {"houzz": "HouzzExtractor"},
                    },
                    "transform": {
                        "src.news.news_data_transformer": {"news": "NewsTransformer"},
                        "src.tedtalk.tedtalk_data_transformer": {
                            "tedtalk": "TedtalkTransformer"
                        },
                        "src.houzz.houzz_data_transformer": {
                            "houzz": "HouzzTransformer"
                        },
                    },
                    "load": {
                        "src.news.news_data_loader": {"news": "NewsLoader"},
                        "src.tedtalk.tedtalk_data_loader": {"tedtalk": "TedtalkLoader"},
                        "src.houzz.houzz_data_loader": {"houzz": "HouzzLoader"},
                    },
                },
            )
        ],
    )
    def test_read_config(self, config_path: str, expect: dict):
        """ """
        IO = InitObject(class_config_path=config_path)
        answer = IO.class_config

        assert answer == expect

    @pytest.mark.parametrize(
        "key, expect",
        [
            (
                "extract",
                {
                    "news": "NewsExtractor",
                    "tedtalk": "TedtalkExtractor",
                    "houzz": "HouzzExtractor",
                },
            ),
            (
                "transform",
                {
                    "news": "NewsTransformer",
                    "tedtalk": "TedtalkTransformer",
                    "houzz": "HouzzTransformer",
                },
            ),
            (
                "load",
                {
                    "news": "NewsLoader",
                    "tedtalk": "TedtalkLoader",
                    "houzz": "HouzzLoader",
                },
            ),
        ],
    )
    def test_load_class(self, key: str, expect: dict):
        """ """
        IO = InitObject(class_config_path="./config/class_object.yaml")
        class_config_dict = IO.class_config[key]
        class_object_dict = IO._load_class(class_config_dict)
        answer = {k: v.__name__ for k, v in class_object_dict.items()}

        assert answer == expect

    @pytest.mark.parametrize(
        "key, expect",
        [
            (
                "extract",
                {
                    "news": "NewsExtractor",
                    "tedtalk": "TedtalkExtractor",
                    "houzz": "HouzzExtractor",
                },
            ),
            (
                "transform",
                {
                    "news": "NewsTransformer",
                    "tedtalk": "TedtalkTransformer",
                    "houzz": "HouzzTransformer",
                },
            ),
            (
                "load",
                {
                    "news": "NewsLoader",
                    "tedtalk": "TedtalkLoader",
                    "houzz": "HouzzLoader",
                },
            ),
        ],
    )
    def test_instance_class(self, key: str, expect: dict):
        """ """
        IO = InitObject(class_config_path="./config/class_object.yaml")
        class_config_dict = IO.class_config[key]
        class_object_dict = IO._load_class(class_config_dict=class_config_dict)
        instance_calss_dict = IO._instance_class(class_object_dict=class_object_dict)
        answer = {k: v.__class__.__name__ for k, v in instance_calss_dict.items()}

        assert answer == expect

    @pytest.mark.parametrize(
        "key, expect",
        [
            (
                "extract",
                {
                    "news": "NewsExtractor",
                    "tedtalk": "TedtalkExtractor",
                    "houzz": "HouzzExtractor",
                },
            ),
            (
                "transform",
                {
                    "news": "NewsTransformer",
                    "tedtalk": "TedtalkTransformer",
                    "houzz": "HouzzTransformer",
                },
            ),
            (
                "load",
                {
                    "news": "NewsLoader",
                    "tedtalk": "TedtalkLoader",
                    "houzz": "HouzzLoader",
                },
            ),
        ],
    )
    def test_create(self, key: str, expect: dict):
        """ """
        IO = InitObject(class_config_path="./config/class_object.yaml")
        instance_calss_dict = IO._create(key=key)
        answer = {k: v.__class__.__name__ for k, v in instance_calss_dict.items()}

        assert answer == expect
