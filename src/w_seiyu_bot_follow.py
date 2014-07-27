#! /usr/bin/env python
# coding: utf-8

import sys
import codecs
import random
import json
import urllib2
import twython
from manager.api_manager import ApiManager
from manager.seiyu_manager import SeiyuManager

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# KLOUT関連
ID_URL = 'http://api.klout.com/v2/identity.json/twitter?screenName=%s&key=' + ApiManager.KLOUT_KEY
SCORE_URL = 'http://api.klout.com/v2/user.json/%s/score?key=' + ApiManager.KLOUT_KEY

twitter = twython.Twython(
    app_key = ApiManager.CONSUMER_KEY,
    app_secret = ApiManager.CONSUMER_SECRET,
    oauth_token = ApiManager.ACCESS_TOKEN,
    oauth_token_secret = ApiManager.ACCESS_TOKEN_SECRET
)

# キーワードを特定
seiyu_manager = SeiyuManager()
keyword = seiyu_manager.get_seiyu()
print keyword.decode('utf-8')

# 特定キーワードを検索
results = twitter.search(q=keyword, count=100)
follow_count = 0
for result in results['statuses']:
	
	try:
		# twitterのユーザー名を取得
		screen_name = result['user']['screen_name']
	
		# twitterユーザーのkloutIdを取得
		f = urllib2.urlopen(ID_URL % screen_name)
		klout_id = json.loads(f.read())['id']
	
		# スコアを取得
		f = urllib2.urlopen(SCORE_URL % klout_id)
		score = json.loads(f.read())['score']
		
		# KLOUTスコアが基準値以上ならフォロー
		f_score = float(score)
		if f_score > int(ApiManager.KLOUT_SCORE):
			twitter.create_friendship(screen_name=screen_name, follow="true")
			print u"%sさんをフォローしました。" % screen_name
			print u"KLOUT:%s" % score
			follow_count += 1

	except Exception as e:
		print e
		print u"エラーが起こりましたが無視します。"

print u"☆☆☆%sユーザーをフォローしました。☆☆☆" % follow_count