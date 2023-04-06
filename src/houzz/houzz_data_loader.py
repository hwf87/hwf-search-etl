#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
from src.CrawlerBase import LoaderBase
from utils.utils import get_logger, log
from utils.config_parser import elasticsearch_index_name_houzz, houzz_schema, fn_

logger = get_logger(name=__name__)

class HouzzLoader(LoaderBase):
    def __init__(self):
        super().__init__()
    
    @log(logger)
    def load(self, documents: list) -> None:
        """
        """
        es = self.get_es_client()
        index_exist = self.check_index(index_name = elasticsearch_index_name_houzz, es = es)
        if not index_exist:
            self.create_index(index_name = elasticsearch_index_name_houzz, body = houzz_schema, es = es)
        
        if index_exist != None:
            self.bulk_insert(actions = self.load_action_batch(
                                    op_type = "index",
                                    index_name = elasticsearch_index_name_houzz,
                                    documents = documents
                                ),
                             es = es)

    @log(logger)
    def load_action_batch(self, op_type: str, index_name: str, documents: list) -> dict:
        """
        """
        for document in documents:
            document_id = document[fn_.uid]
            actions = {
                "_op_type": op_type,
                "_index": index_name,
                "_id": document_id,
                "_source": document
            }
            yield actions