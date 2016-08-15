#! /usr/bin/env python
# coding:utf-8

import sqlite3
import twython
from manager.config_manager import ConfigManager
from manager.check_user_manager import CheckUserManager
from manager.seiyu_manager import SeiyuManager
from manager.black_list_manager import BlackListManager
from manager.tweet_manager import TweetManager

twitter = twython.Twython(
	    	app_key = ConfigManager.TW_CONSUMER_KEY,
	    	app_secret = ConfigManager.TW_CONSUMER_SECRET,
	    	oauth_token = ConfigManager.TW_ACCESS_TOKEN,
	    	oauth_token_secret = ConfigManager.TW_ACCESS_TOKEN_SECRET
		)

def main():

	# チェックユーザーのIDを取得
	check_user_manager = CheckUserManager()
	screen_names = check_user_manager.get_user_screen_names()
	print screen_names

	# 最新の200件のメンションを取得
	for result in twitter.get_mentions_timeline(count=200):

		# チェックユーザーからの特定キーワードの場合は不正画像とみなす
		if result['user']['screen_name'] in screen_names:
			
			print result["text"]
			if result["text"] in "【NG】":

				# ツイートIDを取得してツイートテーブルを検索
				tweet_id = result["in_reply_to_status_id"]
				tweet_manager = TweetManager()
				tweet = tweet_manager.get_tweet(tweet_id)

				# blackListテーブルへの登録
				black_list_manager = BlackListManager()
				black_list_manager.save_black_list(tweet['seiyu'], tweet['image_uri'])

				# ツイートの削除
				twitter.destroy_status(id=tweet_id)

	# ツイートテーブルの全削除
	tweet_manager = TweetManager()
	tweet_manager.delete_all_tweets()

if __name__ == "__main__":
	main()




	
