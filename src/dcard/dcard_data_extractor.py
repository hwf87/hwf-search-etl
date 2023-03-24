#-*- coding: UTF-8 -*-

import sys
sys.path.append("../..")
import json
import logging
import requests
import pandas as pd
from src.CrawlerBase import ExtractorBase
from utils.utils import exception_handler

class DcardExtractor(ExtractorBase):
    def __init__(self, base_url, popular, max_limit):
        super().__init__()
        self.base_url = base_url
        self.popular = popular
        self.max_limit = max_limit

    @exception_handler
    def extract(self):
        print("This is a test!")

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
    
dc = DcardExtractor()
dc.extract()