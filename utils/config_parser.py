import os
import yaml
import json
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
        self.description = "description"
        self.related_tags = "related_tags"
        self.comment_count = "comment_count"

# Common Field Naming 
fn = FieldName()

# Env variables
youtube_api_key = os.environ.get["YOUTUBE_API_KEY"]

# Common Config
with open("./config/config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    elasticsearch_host = config["elasticsearch"]["host"]
    elasticsearch_index_name_news = config["elasticsearch"]["index_name"]["news"]
    elasticsearch_index_name_tedtalk = config["elasticsearch"]["index_name"]["tedtalk"]
    elasticsearch_index_name_houzz = config["elasticsearch"]["index_name"]["houzz"]
    torch_model_path = config["torch"]["model_path"]
    tedtalk_base_url = config["tedtalk"]["base_url"]
    youtube_api_base_url = config["youtube"]["api_base_url"]
    # youtube_api_key = config["youtube"]["api_key"]
    houzz_story_base_url = config["houzz"]["story_base_url"]
    f.close()

# Elasticsearch Index Schema
with open("./config/es_index_schema/tedtalk.json", "r") as f:
    tedtalk_schema = json.load(f)
    f.close()
with open("./config/es_index_schema/news.json", "r") as f:
    news_schema = json.load(f)
    f.close()
with open("./config/es_index_schema/houzz.json", "r") as f:
    houzz_schema = json.load(f)
    f.close()
    
    
    
    

