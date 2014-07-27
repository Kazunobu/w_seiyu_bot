#! /usr/bin/env python
# coding:utf-8

import ConfigParser

#DBファイル
CONFIG_FILE = '../conf/w_seiyu_bot.config'

class ApiManager:
	
	config = ConfigParser.SafeConfigParser()
	config.read(CONFIG_FILE)

	# TwitterのAPIキー
	CONSUMER_KEY = config.get("API", "CONSUMER_KEY")
	CONSUMER_SECRET = config.get("API", "CONSUMER_SECRET")
	ACCESS_TOKEN = config.get("API", "ACCESS_TOKEN")
	ACCESS_TOKEN_SECRET = config.get("API", "ACCESS_TOKEN_SECRET")	
	
	# KLOUTのAPIキー
	KLOUT_KEY = config.get("API", "KLOUT_KEY")	

	# DBのファイルパス
	DB_FILE = config.get("DB", "PATH")
	
	# フォロー対象のKLOUT基準値
	KLOUT_SCORE = config.get("KLOUT", "KLOUT_SCORE")