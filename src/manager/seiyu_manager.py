#! /usr/bin/env python
# coding:utf-8

import sqlite3
import random
from api_manager import ApiManager

#DBファイル
DB_FILE = ApiManager.DB_FILE

class SeiyuManager:
	u''' 声優の管理を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def get_seiyu(self):
		
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