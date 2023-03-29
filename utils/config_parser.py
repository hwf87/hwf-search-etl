import yaml
import json
import sys
sys.path.append("..")


with open("./config/config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    elasticsearch_host = config["elasticsearch"]["host"]
    f.close()

with open("./config/es_index_schema/tedtalk.json", "r") as f:
    tedtalk_schema = json.load(f)
    f.close()
