#! /usr/bin/env python
# coding:utf-8

import sqlite3
import random
from config_manager import ConfigManager

#DBファイル
DB_FILE = ConfigManager.DB_FILE

class SeiyuManager:
	u''' 声優の管理を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def get_seiyu(self):
		u''' ツイート対象の声優を取得する '''
		
		db = sqlite3.connect(DB_FILE)

		# 声優のカウントを取得
		count_sql = 'select count(*) from seiyu_tbl'
		count = db.execute(count_sql).fetchone()[0]
		assert count != None

		# 取得インデックス
		seiyu_sql = 'select name from seiyu_tbl order by name'
		i = random.randint(0, count-1)
		seiyu = db.execute(seiyu_sql).fetchall()[i][0]

		db.close()

		return seiyu.encode('utf-8')

	def get_birthday_seiyus(self, birthday):
		u''' 誕生日の声優一覧を取得して返す '''

		sql = "select name from seiyu_tbl where birthday = ?"

		db = sqlite3.connect(DB_FILE)
		
		results = db.execute(sql, (birthday,)).fetchall()
		names = [ result[0] for result in results]

		db.close()

		return names		
