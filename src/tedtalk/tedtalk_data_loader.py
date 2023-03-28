#-*- coding: UTF-8 -*-

import sys
import json
sys.path.append("../..")
from elasticsearch import Elasticsearch
from src.CrawlerBase import LoaderBase
from utils.utils import get_logger, log

logger = get_logger(name=__name__)

class TedtalkLoader(LoaderBase):
    def __init__(self):
        super().__init__()
    
    def load(self, data):
        
        print(f"TYPE: {type(data)}")
        print(f"MYDATA===== {data}")
        es = Elasticsearch("http://127.0.0.1:9200", verify_certs = False)
        res = es.index(index = 'tedtalk', id = data["uid"], body = data)
        print(res)
