#! /usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import json
from manager.config_manager import ConfigManager

# APIのURL
API_URL = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&searchType=image&q={QUERY}start={IDX}&num=1"

class GoogleImageFinder:
	u''' googleの画像検索を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def find_image(self, seiyu, idx):

		#Googleのみapiを利用
		prop_dict = dict(API_KEY=ConfigManager.GOOGLE_API_KEY, CX=ConfigManager.GOOGLE_CX, QUERY=urllib.quote(seiyu), IDX=idx)
		url = API_URL.format(**prop_dict)

		f = urllib2.urlopen(url)
		data = json.loads(f.read())

		imgurl = None
		for result in data['items']:
			imgurl = result['link']
			break

		return imgurl
