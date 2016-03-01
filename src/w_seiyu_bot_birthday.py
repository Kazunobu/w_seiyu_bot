#! /usr/bin/env python
# coding:utf-8

import datetime
import os
import random
import urllib
import twython
from manager.api_manager import ApiManager
from manager.seiyu_manager import SeiyuManager
from finder.yahoo import YahooImageFinder
from finder.bing import BingImageFinder
from finder.google import GoogleImageFinder

# 一時ファイル
TEMPFILE = 'w_seiyu_temp'

def tweet_birthday_image(seiyu, tempfile):
	twitter = twython.Twython(
    	app_key = ApiManager.TW_CONSUMER_KEY,
    	app_secret = ApiManager.TW_CONSUMER_SECRET,
    	oauth_token = ApiManager.TW_ACCESS_TOKEN,
    	oauth_token_secret = ApiManager.TW_ACCESS_TOKEN_SECRET
	)

	photo = open(tempfile, 'rb')
	status = '【祝】本日は' + seiyu + 'さんのお誕生日です！！\n'
	status += seiyu + 'さん、おめでとうございます！！\n'
	print status
	# return twitter.update_status_with_media(status=status, media=photo)

def main():

	today = datetime.date.today()
	todaystr = today.strftime("%m%d")

	seiyu_manager = SeiyuManager()
	seiyus = seiyu_manager.get_birthday_seiyus(todaystr)
	
	if len(seiyus) > 0:

		# 検索エンジンを決定
		finder = YahooImageFinder()
		searchmode = random.randint(1, 3)
		if searchmode == 1:
			finder = YahooImageFinder()
		elif searchmode == 2:
			finder = BingImageFinder()
		else:
			finder = GoogleImageFinder()

		for i, seiyu in enumerate(seiyus):

			# 声優画像取得
			idx = random.randint(1, ApiManager.FIND_COUNT)
			image_uri = finder.find_image(seiyu.encode('utf-8'), idx)
			print image_uri
			
			# ダウンロード
			urllib.urlretrieve(image_uri, TEMPFILE + str(i))

			# ツイート
			tweet_birthday_image(seiyu.encode('utf-8'), TEMPFILE + str(i))

			# 一時ファイルを削除
			os.remove(TEMPFILE + str(i))
			
	else:
		print "not found..."

if __name__ == "__main__":
	main()
	
