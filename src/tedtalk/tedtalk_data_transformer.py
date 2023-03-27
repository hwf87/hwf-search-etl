#-*- coding: UTF-8 -*-

import sys
from retry import retry
import pandas as pd
sys.path.append("../..")
from src.CrawlerBase import TransformerBase
from utils.utils import get_logger, log
from sentence_transformers import SentenceTransformer

logger = get_logger(name=__name__)

class TedtalkTransformer(TransformerBase):
    def __init__(self):
        super().__init__()
        self.model_path = 'paraphrase-multilingual-MiniLM-L12-v2'
        self.model = SentenceTransformer(self.model_path)

    @log(logger)
    def transform(self, input_json_list: list) -> list:
        """
        """
        results = []
        for item in input_json_list:
            item["embeddings"] = self.inference(item["details"])
            results.append(item)

        return results[0]
    
    @log(logger)
    def inference(self, text: str) -> list:
        """
        """
        embeddings = self.model.encode(text)
        embeddings = embeddings.tolist()
        return embeddings
    

# data = [
#     {"id": 1, "text":"apple is a fruit!!"},
#     {"id": 2, "text":"sky is blue!!"},
#     {"id": 3, "text":"pencil is not a fruit!!"}
# ]

# TT = TedtalkTransformer()
# res = TT.transform(data)

# print(res)