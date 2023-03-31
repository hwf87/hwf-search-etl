import yaml
import json
import sys
sys.path.append("..")

with open("./config/config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    elasticsearch_host = config["elasticsearch"]["host"]
    elasticsearch_index_name_news = config["elasticsearch"]["index_name"]["news"]
    elasticsearch_index_name_tedtalk = config["elasticsearch"]["index_name"]["tedtalk"]
    youtube_api_base_url = config["youtube"]["api_base_url"]
    youtube_api_key = config["youtube"]["api_key"]
    f.close()

with open("./config/es_index_schema/tedtalk.json", "r") as f:
    tedtalk_schema = json.load(f)
    f.close()

with open("./config/es_index_schema/news.json", "r") as f:
    news_schema = json.load(f)
    f.close()

