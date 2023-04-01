#-*- coding: UTF-8 -*-

import sys
import json
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
        logger.info(f"input_json_list Length: {len(input_json_list)}")

        results = []
        chunk_json_list = self.chunks(input_json_list, 500)

        for idx, chunk in enumerate(chunk_json_list):
            logger.info(f"Chunk No.: {idx}")
            df_chunk = pd.DataFrame(chunk)

            df_chunk["embeddings"] = self.inference(batch_texts = df_chunk["details"].tolist())
            results_chunk = df_chunk.to_json(orient="records")
            results_chunk = json.loads(results_chunk)
            results += results_chunk
        
        return results
    
    @log(logger)
    def inference(self, batch_texts: list) -> list:
        """
        """
        embeddings = self.model.encode(batch_texts)
        batch_embeddings = embeddings.tolist()

        return batch_embeddings


    # @log(logger)
    # def transform(self, input_json_list: list) -> list:
    #     """
    #     """
    #     logger.info(f"input_json_list Length: {len(input_json_list)}")
    #     results = []
    #     for item in input_json_list:
    #         item["embeddings"] = self.inference(item["details"])
    #         results.append(item)
    #     #chunk_results = self.chunks(results, 500)

    #     return results  #chunk_results
    
    # @log(logger)
    # def inference(self, text: str) -> list:
    #     """
    #     """
    #     embeddings = self.model.encode(text)
    #     embeddings = embeddings.tolist()

    #     return embeddings
    

# data = [
#     {"id": 1, "text":"apple is a fruit!!"},
#     {"id": 2, "text":"sky is blue!!"},
#     {"id": 3, "text":"pencil is not a fruit!!"}
# ]

# TT = TedtalkTransformer()
# res = TT.transform(data)

# print(res)