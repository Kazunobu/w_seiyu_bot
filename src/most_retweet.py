#! /usr/bin/env python
# coding:utf-8

import twython
import datetime
from manager.api_manager import ApiManager

now = datetime.datetime.today()
TODAY = datetime.date(now.year, now.month, now.day)

twitter = twython.Twython(
	    	app_key = ApiManager.TW_CONSUMER_KEY,
	    	app_secret = ApiManager.TW_CONSUMER_SECRET,
	    	oauth_token = ApiManager.TW_ACCESS_TOKEN,
	    	oauth_token_secret = ApiManager.TW_ACCESS_TOKEN_SECRET
		)

count = 0
max_id = None
most_retweet = None
tcount = 0
while (count < 400):
	results = twitter.get_user_timeline(screen_name='w_seiyu_bot', count=200, max_id=max_id)
	for result in results:
		# US時間のため9時間足す必要あり
		tdatetime = datetime.datetime.strptime(result['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
		addhour = datetime.timedelta(hours=9)
		jpdatetime = tdatetime + addhour
		cratedy = datetime.date(jpdatetime.year, jpdatetime.month, jpdatetime.day)
		
		if TODAY == cratedy:
			tcount += 1
			if most_retweet == None:
				most_retweet = result
			else:
				if int(most_retweet['retweet_count']) < int(result['retweet_count']):
					most_retweet = result
					
	count += len(results)
	max_id = results[len(results) - 1]['id']

text = most_retweet['text']
seiyu = text[0:text.index('http')-1].encode('utf-8')

status = '本日のMRG(MostRetweetGazou)はコチラ！！\n'
status += seiyu + 'さん、おめでとうございます！！\n'
status += 'https://twitter.com/w_seiyu_bot/status/' + str(most_retweet['id'])

print status
# twitter.update_status(status=status)