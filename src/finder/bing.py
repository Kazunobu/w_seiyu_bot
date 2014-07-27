#! /usr/bin/env python
# coding:utf-8

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

# 画像検索結果ページ
PAGE_URL = "http://www.bing.com/images/async?q=%s&async=content&count=1"

class BingImageFinder:
	u''' Bingの画像検索を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def find_image(self, seiyu, idx):

		page = PAGE_URL % urllib.quote(seiyu)

		# 画像取得処理
		url = page + '&first=%s' % idx
		htmlfp = urllib2.urlopen(url)
		pageHtml = htmlfp.read().decode("utf-8", "replace") 
		htmlfp.close()

		soup = BeautifulSoup(pageHtml)

		imgurl = None
		for div in soup.findAll("div", {"class" : "dg_u"}):
			for link in div.findAll("a"):
				data = link['m']
				for value in data.split(","):
					if value.startswith("imgurl:"):
						imgurl = value.strip("imgurl:")
						imgurl = imgurl.strip('"')

		return imgurl
