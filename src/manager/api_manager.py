#! /usr/bin/env python
# coding:utf-8

import ConfigParser

#DBファイル
CONFIG_FILE = '../conf/w_seiyu_bot.config'

class ApiManager:
	
	config = ConfigParser.SafeConfigParser()
	config.read(CONFIG_FILE)

	# TwitterのAPIキー
	TW_CONSUMER_KEY = config.get("API", "TW_CONSUMER_KEY")
	TW_CONSUMER_SECRET = config.get("API", "TW_CONSUMER_SECRET")
	TW_ACCESS_TOKEN = config.get("API", "TW_ACCESS_TOKEN")
	TW_ACCESS_TOKEN_SECRET = config.get("API", "TW_ACCESS_TOKEN_SECRET")

	# GOOGLEのカスタム検索APIキーと検索エンジンID
	GOOGLE_API_KEY = config.get("API", "GOOGLE_API_KEY")
	GOOGLE_CX = config.get("API", "GOOGLE_CX")
	
	# KLOUTのAPIキー
	KLOUT_KEY = config.get("API", "KLOUT_KEY")	

	# DBのファイルパス
	DB_FILE = config.get("DB", "PATH")
	
	# フォロー対象のKLOUT基準値
	KLOUT_SCORE = config.get("APP", "KLOUT_SCORE")

	# 声優の検索結果最大件数（ここからランダムで１件が対象となる。）
	FIND_COUNT = int(config.get("APP", "FIND_COUNT"))