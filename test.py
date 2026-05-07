import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY =os.getenv("API_KEY")
CHANNEL_HANDLE = "campusx-official"
maxResults = 60
playlist_id = "UUCWi3hpnq_Pe03nGxuS7isg"

def get_video_ids(playlist_id):
    video_ids = []
    pageToken = None
    base_url = f" https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlist_id}&key={API_KEY}"

    try:
        while True:
            url = base_url
            if pageToken:
                url += f"&pageToken={pageToken}"
            response = requests.get(url)
            print("pehla step poora")
            
            response.raise_for_status()

            data1 = response.json()
            print("dusra step poora")
           
            for item in data1.get('items',[]):
                print("loop step shuru")
                print(item)
                video_id = item['contentDetails']['videoId']
                print(video_id)
                print(video_ids)
                video_ids.append(video_id)
                print(video_ids)

            pageToken = data1.get('nextPageToken')
               
            if not pageToken:
                break
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    get_video_ids(playlist_id)