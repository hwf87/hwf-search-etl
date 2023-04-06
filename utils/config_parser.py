import os
import yaml
import sys

sys.path.append("..")


class FieldName:
    def __init__(self) -> None:
        self.uid = "uid"
        self.tags = "tags"
        self.link = "link"
        self.title = "title"
        self.views = "views"
        self.likes = "likes"
        self.posted = "posted"
        self.author = "author"
        self.details = "details"
        self.channel = "channel"
        self.embeddings = "embeddings"
        self.description = "description"
        self.related_tags = "related_tags"
        self.comment_count = "comment_count"


class FieldType:
    def __init__(self) -> None:
        self.alias = {"hwf": {}}
        self.text = {"type": "text"}
        self.keyword = {"type": "keyword"}
        self.dense_vector_384 = {"type": "dense_vector", "dims": 384}


# Common Field Name & Field Type
fn_ = FieldName()
ft_ = FieldType()

# Elasticsearch Index Schema
tedtalk_schema = {
    "aliases": ft_.alias,
    "mappings": {
        "properties": {
            fn_.uid: ft_.text,
            fn_.author: ft_.keyword,
            fn_.embeddings: ft_.dense_vector_384,
            fn_.title: ft_.text,
            fn_.details: ft_.text,
            fn_.link: ft_.text,
            fn_.tags: ft_.keyword,
            fn_.views: ft_.text,
            fn_.posted: ft_.text,
        }
    },
}

news_schema = {
    "aliases": ft_.alias,
    "mappings": {
        "properties": {
            fn_.uid: ft_.text,
            fn_.channel: ft_.keyword,
            fn_.embeddings: ft_.dense_vector_384,
            fn_.title: ft_.text,
            fn_.details: ft_.text,
            fn_.link: ft_.text,
            fn_.tags: ft_.keyword,
            fn_.views: ft_.text,
            fn_.likes: ft_.text,
            fn_.posted: ft_.text,
            fn_.comment_count: ft_.text,
        }
    },
}

houzz_schema = {
    "aliases": ft_.alias,
    "mappings": {
        "properties": {
            fn_.uid: ft_.text,
            fn_.author: ft_.keyword,
            fn_.description: ft_.text,
            fn_.embeddings: ft_.dense_vector_384,
            fn_.title: ft_.text,
            fn_.details: ft_.text,
            fn_.link: ft_.text,
            fn_.tags: ft_.keyword,
            fn_.related_tags: ft_.keyword,
            fn_.posted: ft_.text,
        }
    },
}

# Env variables
youtube_api_key = os.environ["YOUTUBE_API_KEY"]
elasticsearch_host = os.environ["ES_HOST"]
elasticsearch_username = os.environ["ES_USERNAME"]
elasticsearch_password = os.environ["ES_PASSWORD"]

# Common Config
with open("./config/config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    elasticsearch_index_name_news = config["elasticsearch"]["index_name"]["news"]
    elasticsearch_index_name_tedtalk = config["elasticsearch"]["index_name"]["tedtalk"]
    elasticsearch_index_name_houzz = config["elasticsearch"]["index_name"]["houzz"]
    torch_model_path = config["torch"]["model_path"]
    tedtalk_base_url = config["tedtalk"]["base_url"]
    youtube_api_base_url = config["youtube"]["api_base_url"]
    houzz_story_base_url = config["houzz"]["story_base_url"]
    f.close()
