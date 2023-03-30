#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
from src.CrawlerBase import TransformerBase
from utils.utils import get_logger, log
from sentence_transformers import SentenceTransformer

logger = get_logger(name=__name__)

class NewsTransformer(TransformerBase):
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
        for item in input_json_list:
            item["embeddings"] = self.inference(item["details"])
            results.append(item)
        #chunk_results = self.chunks(results, 500)

        return results  #chunk_results
    
    @log(logger)
    def inference(self, text: str) -> list:
        """
        """
        embeddings = self.model.encode(text)
        embeddings = embeddings.tolist()

        return embeddings
