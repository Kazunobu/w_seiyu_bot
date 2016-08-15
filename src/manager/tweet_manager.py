#! /usr/bin/env python
# coding:utf-8

import sqlite3
import random
from config_manager import ConfigManager

#DBファイル
DB_FILE = ConfigManager.DB_FILE

class TweetManager:
	u''' ツイートの管理を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def save_tweet(self, tweet_id, seiyu, image_uri):
		db = sqlite3.connect(DB_FILE)

		try:
			save_sql = 'insert into tweet_tbl (tweet_id, seiyu_name, image_uri) values (?,?,?)'
			db.execute(save_sql, (tweet_id, seiyu, image_uri))
		except Exception as e:
			print e
			db.rollback()
		else:
			db.commit()
		finally:
			db.close()

	def get_tweet(self, tweet_id):
		db = sqlite3.connect(DB_FILE)

		search_sql = "select seiyu_name, image_uri from tweet_tbl where tweet_id = ?";
		result = db.execute(search_sql, (tweet_id,)).fetchone()

		db.close()

		result_dict = {"seiyu" : result[0], "image_uri" : result[1]}
		return result_dict


	def delete_all_tweets(self):
		db = sqlite3.connect(DB_FILE)

		delete_sql = "delete from tweet_tbl"
		db.execute(delete_sql)

		db.commit()
		db.close()

if __name__ == "__main__":
	m = TweetManager()
	print m.get_tweet('488646330160398336')
