#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
from src.CrawlerBase import LoaderBase
from utils.utils import get_logger, log
from utils.config_parser import elasticsearch_host, tedtalk_schema

logger = get_logger(name=__name__)

class TedtalkLoader(LoaderBase):
    def __init__(self):
        super().__init__()
    
    @log(logger)
    def load(self, documents: list) -> None:
        """
        """
        index_name = "tedtalk_3"
        # host = "http://127.0.0.1:9200"
        es = self.get_es_client(host = elasticsearch_host)
        index_exist = self.check_index(index_name = index_name, es = es)
        if not index_exist:
            self.create_index(index_name = index_name, body = tedtalk_schema, es = es)
        
        if index_exist != None:
            self.bulk_insert(actions = self.load_action_batch(
                                    op_type = "index",
                                    index_name = index_name,
                                    documents = documents
                                ),
                             es = es)

    @log(logger)
    def load_action_batch(self, op_type: str, index_name: str, documents: list) -> dict:
        """
        """
        for document in documents:
            document_id = document["uid"]
            actions = {
                "_op_type": op_type,
                "_index": index_name,
                # "_id": document_id,
                "_source": document
            }
            yield actions


        # es = Elasticsearch("http://127.0.0.1:9200", verify_certs = False)
        # res = es.index(index = 'tedtalk', id = data["uid"], body = data)
        # print(res)
