#! /usr/bin/env python
# coding:utf-8

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

# 画像検索結果ページ
PAGE_URL = "http://image.search.yahoo.co.jp/search?fr=sfp_as&p=%s&oq=&ei=UTF-8&ktot=37&dtot=0"

class YahooImageFinder:
	u''' Yahooの画像検索を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def find_image(self, seiyu, idx):

		# 画像検索一覧ページ
		page = PAGE_URL % urllib.quote(seiyu)

		start_idx = 1
		links = []
		for i in range (3):
			start_idx = (i * 20) + 1
			url = page + '&b=%s' % start_idx

			htmlfp = urllib2.urlopen(url)
			pageHtml = htmlfp.read().decode("utf-8", "replace") 
			htmlfp.close()
		
			soup = BeautifulSoup(pageHtml)
			for div in soup.findAll("div", {"class" : "gridmodule"}):
				for p in div.findAll("p", {"class" : "tb"}):
					for link in p.findAll("a"):
						imageLink = link['href']

						# 他の検索対象のリンクが存在するため無視
						if not imageLink.startswith('http://image.search.yahoo.co.jp/search') :
							links.append(imageLink)

		return links[idx]