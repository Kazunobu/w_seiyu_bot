#! /usr/bin/env python
# coding:utf-8

import random
import urllib
import twython
from manager.api_manager import ApiManager
from manager.seiyu_manager import SeiyuManager
from manager.black_list_manager import BlackListManager
from manager.tweet_manager import TweetManager
from finder.yahoo import YahooImageFinder
from finder.bing import BingImageFinder
from finder.google import GoogleImageFinder

# 一時ファイル
TEMPFILE = 'w_seiyu_temp'

def tweet_image(seiyu):
	twitter = twython.Twython(
    	app_key = ApiManager.CONSUMER_KEY,
    	app_secret = ApiManager.CONSUMER_SECRET,
    	oauth_token = ApiManager.ACCESS_TOKEN,
    	oauth_token_secret = ApiManager.ACCESS_TOKEN_SECRET
	)

	photo = open(TEMPFILE, 'rb')
	return twitter.update_status_with_media(status=seiyu, media=photo)

def main():

	# 検索エンジンを決定
	finder = None
	searchmode = random.randint(1, 4)
	if searchmode == 1:
		finder = YahooImageFinder()
	elif searchmode == 2:
		finder = BingImageFinder()
	else:
		finder = GoogleImageFinder()
	
	# 声優•取得位置
	seiyu_manager = SeiyuManager()
	seiyu = seiyu_manager.get_seiyu()
	print seiyu
	
	idx = random.randint(1, 50)

	# 画像URI取得
	image_uri = finder.find_image(seiyu, idx)
	print image_uri

	# ブラックリストチェック
	black_list_manager = BlackListManager()
	while black_list_manager.contains(seiyu.decode('utf-8'), image_uri):
		idx = random.randint(1, 50)
		image_uri = finder.find_image(seiyu, idx)

	# 画像のダウンロード
	urllib.urlretrieve(image_uri, TEMPFILE)

	# ツイート
	result = tweet_image(seiyu)
	print result
	
	# ツイート内容を登録
	tweet_manager = TweetManager()
	tweet_manager.save_tweet(result['id'], seiyu.decode('utf-8'), image_uri.decode('utf-8'))

if __name__ == "__main__":
	main()
	