#! /usr/bin/env python
# coding:utf-8

import sqlite3
import random
from api_manager import ApiManager

#DBファイル
DB_FILE = ApiManager.DB_FILE

class CheckUserManager:
	u''' チェックユーザーの管理を行う  '''

	def __init__(self):
		u''' 初期化 '''

	def get_user_screen_names(self):
		db = sqlite3.connect(DB_FILE)

		sql = 'select screen_name from check_user_tbl'
		results = db.execute(sql).fetchall()

		screen_names = [ result[0] for result in results]

		db.close()

		return screen_names

if __name__ == "__main__":
	m = CheckUserManager()
	print m.get_user_screen_names()