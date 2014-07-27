#! /usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import json

# APIのURL
API_URL = "http://ajax.googleapis.com/ajax/services/search/images?q=%s&v=1.0&rsz=large"

class GoogleImageFinder:
	u''' googleの画像検索を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def find_image(self, seiyu, idx):

		#Googleのみapiを利用
		URL = API_URL % urllib.quote(seiyu)
		url = URL + "&start=%s" % (idx-1)

		f = urllib2.urlopen(url)
		data = json.loads(f.read())

		# 念のため失敗ははじく
		imgurl = None
		if data['responseStatus'] != 400:
			for result in data['responseData']['results']:
				imgurl = result['url']
				break

		return imgurl
