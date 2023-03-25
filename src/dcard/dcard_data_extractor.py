#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
import json
import logging
import requests
import pandas as pd
from fake_useragent import UserAgent
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger


base_url = "https://www.dcard.tw/service/api/v2"
popular = "false"
max = "10"

logger = get_logger(name=__name__)

class DcardExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()

    def get_df_from_api(self, url: str) -> pd.DataFrame:
        """
        """
        # user_agent = UserAgent()
        # headers = {"User-Agent": user_agent.random}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        response = requests.get(url, headers=headers).text
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
    
    def get_Dcard_posts_links(self, postid):
        '''
        文章內引用連結
        '''
        url = self.base_url + '/posts/' + str(postid) + '/links'
        df = self.get_df_from_api(url)
        return df
    
    def get_post_mata(self, forums_name: str) -> dict:
        """
        """
        url = f"{base_url}/forums/{forums_name}/posts?popular={popular}&limit={max}"
        # if before_postid:
        #     url += f"&before={before_postid}"
        df = self.get_df_from_api(url = url)
        return df

    # @log(logger)
    def extract(self):
        """
        main function to do data extraction
        """
        forums_name = "tech_job"
        df = self.get_post_mata(forums_name)
        # logger.info(f"{df.columns}")
        print(df)


dc = DcardExtractor()
dc.extract()