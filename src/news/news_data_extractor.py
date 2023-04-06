# -*- coding: utf-8 -*-

import sys
import requests
sys.path.append("../..")
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger
from utils.config_parser import youtube_api_base_url, youtube_api_key, fn_

logger = get_logger(name=__name__)

class NewsExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
    
    @log(logger)
    def get_playlist_id(self, channel_username: str) -> str:
        """
        """
        part = "contentDetails"
        url = f"{youtube_api_base_url}/channels?part={part}&forUsername={channel_username}&key={youtube_api_key}"
        result = requests.get(url).json()
        playlist_id = result["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        return playlist_id
    
    @log(logger)
    def get_video_id_list(self, playlist_id: str, results_per_page: str, pages: int=None, nextPageToken: str=None) -> list:
        """
        """
        idx = 1
        part = "contentDetails"
        video_id_list = []
        while nextPageToken != "":
            logger.info(f"YouTube Page No.: {idx}")
            url = f'{youtube_api_base_url}/playlistItems?part={part}&playlistId={playlist_id}&maxResults={results_per_page}&key={youtube_api_key}'
            if nextPageToken != None:
                url += f"&pageToken={nextPageToken}"
            result = requests.get(url).json()

            totalResults = result['pageInfo']['totalResults']
            nextPageToken = result.get("nextPageToken", "")
            video_id_tmp = [item['contentDetails']['videoId'] for item in result["items"]]
            video_id_list += video_id_tmp
            idx += 1
            if pages == None:
                continue
            if idx > pages:
                break

        return totalResults, nextPageToken, video_id_list
    
    @log(logger)
    def parse_video_metadata(self, metadata: dict) -> dict:
        """
        """
        url_ = f"https://www.youtube.com/watch?v={metadata['id']}"
        info = {
            fn_.uid: metadata['id'],
            fn_.channel: metadata['snippet'].get('channelTitle', ""),
            fn_.tags: metadata['snippet'].get('tags', []),
            fn_.posted: metadata['snippet'].get('publishedAt', ""),
            fn_.link: url_,
            fn_.title: metadata['snippet'].get('title', ""),
            fn_.details: metadata['snippet'].get('description', ""),
            fn_.likes: metadata['statistics'].get('likeCount', ""),
            fn_.comment_count: metadata['statistics'].get('commentCount', ""),
            fn_.views: metadata['statistics'].get('viewCount', "")
        }
        return info
    
    @log(logger)
    def get_video_info(self, video_id_list: list) -> dict:
        """
        video_id_list length <= 50
        """
        video_ids = ",".join(video_id_list)
        part = "snippet,statistics"
        url = f'{youtube_api_base_url}/videos?part={part}&id={video_ids}&key={youtube_api_key}'
        result = requests.get(url).json()

        meta_list = result["items"]
        infos = [self.parse_video_metadata(metadata) for metadata in meta_list]

        return infos

    @log(logger)
    def extract(self, channel_username: str="CNN") -> list:
        """
        main logic
        ChannelID: "UCupvZG-5ko_eiXAupbDfxWw"
        """
        # get play list id from channel
        playlist_id = self.get_playlist_id(channel_username = channel_username)

        # get video id list
        totalResults, nextPageToken, video_id_list = self.get_video_id_list(playlist_id = playlist_id,
                                                                  results_per_page = "50",
                                                                  pages = 5)
        logger.info(f"totalResults: {totalResults}, nextPageToken: {nextPageToken}")
        
        # get videos info
        video_id_list = self.chunks(video_id_list, 50)
        results = []
        for idx, vid_chunk in enumerate(video_id_list):
            logger.info(f"Video Chunk No.: {idx}")
            chunck_result = self.get_video_info(video_id_list = vid_chunk)
            results += chunck_result
        
        return results