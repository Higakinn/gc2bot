import os 
import json
import random

from pytube import Search
from mastodon import Mastodon

yt_base_url ="https://www.youtube.com"
url = os.getenv("MASTODON_URL")
token = os.getenv("MASTODON_TOKEN")
keywords = json.loads(os.getenv("SEARCH_KEYWORDS")) 

mastodon = Mastodon(
        access_token = token,
        api_base_url = url
)
 
# YouTubeで検索
for pref in keywords:
	for festival in keywords[pref]:
		print(festival)
		results = Search(festival).results
		# ランダムで抽出
		result = random.choice(results)
		video_url=f"{yt_base_url}/watch?v={result.video_id}"
		chanel = f"【チャンネル名】\n{result.author}\n{result.channel_url}"
		video = f"【タイトル】\n{result.title}\n{video_url}"

		toot_content = f"{pref}の祭り\n{video}\n{chanel}\n#{festival}"
		mastodon.toot(toot_content)
