#! /usr/bin/env python
# coding:utf-8

import sqlite3
import random
from config_manager import ConfigManager

#DBファイル
DB_FILE = ConfigManager.DB_FILE

class BlackListManager:
	u''' ブラックリストの管理を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def contains(self, seiyu, url):
		db = sqlite3.connect(DB_FILE)

		# 該当データがブラックリストに存在するか
		count_sql = 'select count(*) from black_list_tbl where seiyu_name = ? and image_uri = ?'
		count = db.execute(count_sql, (seiyu, url)).fetchone()[0]

		db.close()

		return count > 0

	def save_black_list(self, seiyu, image_uri):
		db = sqlite3.connect(DB_FILE)

		try:
			save_sql = 'insert into black_list_tbl (seiyu_name, image_uri) values (?,?)'
			db.execute(save_sql, (seiyu, image_uri))
		except Exception as e:
			print e
			db.rollback()
		else:
			db.commit()
		finally:
			db.close()