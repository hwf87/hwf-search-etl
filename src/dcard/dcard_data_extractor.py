#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
import json
import logging
import requests
import pandas as pd
from src.CrawlerBase import ExtractorBase
from utils.utils import log

base_url = ""
popular = ""
max_limit = ""

def get_logger(name: str):
    logger = logging.getLogger(f"{name}")
    handler = logging.StreamHandler()
    formatter = logging.Formatter('process: p%(process)s | funcName: %(funcName)s | line: %(lineno)d | level: %(levelname)s | message:{%(message)s}')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger(name=__name__)

class DcardExtractor(ExtractorBase):
    def __init__(self, base_url, popular, max_limit):
        super().__init__()
        self.base_url = base_url
        self.popular = popular
        self.max_limit = max_limit

    @log(logger)
    def extract(self):
        print(f"This is a test!{aa}")
        logger.debug(f"successfully execute!!")

    def get_df_from_api(self, url):
        response = requests.get(url).text
        data = json.loads(response)
        df = pd.DataFrame(data)
        return df

    def get_Dcard_forums(self):
        '''
        看板資訊
        '''
        url = self.base_url + '/forums'
        df = self.get_df_from_api(url)
        return df

    def get_Dcard_posts_all(self):
        '''
        全部文章
        '''
        url = self.base_url + '/posts'
        df = self.get_df_from_api(url)
        return df

    def get_Dcard_posts(self, forums_name, before_postid=None):
        '''
        看板文章列表
        '''
        if before_postid == None:
            url = self.base_url + '/forums/' + str(forums_name) + '/posts' + '?popular=' + self.popular + '&limit=' + str(self.max_limit)
        else:
            url = self.base_url + '/forums/' + str(forums_name) + '/posts' + '?popular=' + self.popular + '&limit=' + str(self.max_limit) + '&before=' + str(before_postid)
        df = self.get_df_from_api(url)
        return df

    def get_Dcard_posts_context(self, postid):
        '''
        文章內容
        '''
        url = self.base_url + '/posts/' + str(postid)
        df = self.get_df_from_api(url)
        return df
    
    def get_Dcard_posts_links(self, postid):
        '''
        文章內引用連結
        '''
        url = self.base_url + '/posts/' + str(postid) + '/links'
        df = self.get_df_from_api(url)
        return df

    def get_Dcard_posts_comments(self, postid, after_floorid=None):
        '''
        文章留言
        '''
        if after_floorid == None:
            url = self.base_url + '/posts/' + str(postid) + '/comments'
        else:
            url = self.base_url + '/posts/' + str(postid) + '/comments' + '?after=' + str(after_floorid)
        df = self.get_df_from_api(url)
        return df
    
dc = DcardExtractor(base_url, popular, max_limit)
dc.extract()