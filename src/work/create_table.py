#! /usr/bin/env python
# coding:utf-8
import sqlite3

DB_FILE = 'w_seiyu_bot.sqlite'

def main():
	db = sqlite3.connect(DB_FILE)

	seiyu_tbl = "CREATE TABLE seiyu_tbl (name TEXT PRIMARY KEY , name_e TEXT, birthday TEXT)"
	black_list_tbl = "CREATE TABLE black_list_tbl (id INTEGER PRIMARY KEY AUTOINCREMENT, seiyu_name TEXT NOT NULL, image_uri TEXT NOT NULL)"
	tweet_tbl = "CREATE TABLE tweet_tbl (tweet_id TEXT PRIMARY KEY, seiyu_name TEXT NOT NULL, image_uri TEXT NOT NULL)"
	check_user_tbl = "CREATE TABLE check_user_tbl (id INTEGER PRIMARY KEY AUTOINCREMENT, screen_name TEXT NOT NULL)"

	db.execute(seiyu_tbl)
	db.execute(black_list_tbl)
	db.execute(tweet_tbl)
	db.execute(check_user_tbl)

	db.close()

if __name__ == "__main__":
	main()