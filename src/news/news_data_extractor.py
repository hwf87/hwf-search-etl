# -*- coding: utf-8 -*-

import sys
import requests
sys.path.append("../..")
from src.CrawlerBase import ExtractorBase
from utils.utils import log, get_logger

logger = get_logger(name=__name__)

api_key = "AIzaSyDxLknOj3nYnOjKs0Uc83omWXwNH6_TdHI"
channel_id = "UCupvZG-5ko_eiXAupbDfxWw"
channel_username = "CNN"
base_uri = "https://www.googleapis.com/youtube/v3"

"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=CNN&key=AIzaSyDxLknOj3nYnOjKs0Uc83omWXwNH6_TdHI"

'''
{
  "kind": "youtube#channelListResponse",
  "etag": "IbXPspjj5fQ4E6OF2FGfdSAqO6Q",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "G8xQgHvyOJZrWSekOjayPj-5Cbc",
      "id": "UCupvZG-5ko_eiXAupbDfxWw",
      "contentDetails": {
        "relatedPlaylists": {
          "likes": "",
          "uploads": "UUupvZG-5ko_eiXAupbDfxWw"
        }
      }
    }
  ]
}
'''

class NewsExtractor(ExtractorBase):
    def __init__(self):
        super().__init__()
    
    def get_playlist_id(self, channel_username: str) -> str:
        """
        """
        part = "contentDetails"
        url = f"{base_uri}/channels?part={part}&forUsername={channel_username}&key={api_key}"
        result = requests.get(url).json()
        playlist_id = result["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        return playlist_id
    
    def get_video_id_list(self, playlist_id: str) -> list:
        """
        """
        max_results = "10"
        part = "contentDetails"
        url = f'{base_uri}/playlistItems?part={part}&playlistId={playlist_id}&maxResults={max_results}&key={api_key}'
        result = requests.get(url).json()

        # print(f"TOTAL: {result['pageInfo']['totalResults']}")        
        video_id_list = [item['contentDetails']['videoId'] for item in result["items"]]

        return video_id_list
    
    def get_video_info(self, video_id: str) -> dict:
        """
        """
        part = "snippet,statistics"
        url = f'{base_uri}/videos?part={part}&id={video_id}&key={api_key}'
        result = requests.get(url).json()
        data_item = result["items"][0]
        url_ = f"https://www.youtube.com/watch?v={data_item['id']}"
        info = {
            'id': data_item['id'],
            'channelTitle': data_item['snippet']['channelTitle'],
            'tags': data_item['snippet']['tags'],
            'publishedAt': data_item['snippet']['publishedAt'],
            'video_url': url_,
            'title': data_item['snippet']['title'],
            'description': data_item['snippet']['description'],
            'likeCount': data_item['statistics']['likeCount'],
            'commentCount': data_item['statistics']['commentCount'],
            'viewCount': data_item['statistics']['viewCount']
        }
        print(info)

        return info

    @log(logger)
    def extract(self) -> list:
        """
        main logic
        """
        # get total pages
        print("Hello")

NE = NewsExtractor()
playlist_id = NE.get_playlist_id(channel_username = channel_username)
print(f"MY_PLAYLIST_ID: {playlist_id}")

video_id_list = NE.get_video_id_list(playlist_id = playlist_id)
my_vid = video_id_list[0]
print(f"MY_VID: {my_vid}")

NE.get_video_info(video_id = my_vid)