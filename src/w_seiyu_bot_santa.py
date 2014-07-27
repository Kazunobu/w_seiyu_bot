#! /usr/bin/env python
# coding: utf-8

import random
import twython
import os
from manager.api_manager import ApiManager

d = {
	'01' : 'サンタの群れ01',
	'02' : 'サンタの群れ02',
	'03' : 'スフィアサンタ01',
	'04' : 'スフィアサンタ02',
	'05' : 'たまゆらサンタ01',
	'06' : 'たまゆらサンタ02',
	'07' : 'ゆいかおりサンタ01',
	'08' : 'ゆいかおりサンタ02',
	'09' : 'ゆいかおりサンタ03',
	'10' : 'ゆいかおりサンタ04',
	'11' : 'ゆいかおりサンタ05',
	'12' : 'ゆいかおりサンタ06',
	'13' : 'ゆいかおりサンタ07',
	'14' : 'ゆいかおりサンタ08',
	'15' : 'ゆいかおりサンタ09',
	'16' : '阿澄佳奈サンタ01',
	'17' : '伊藤かな恵サンタ＆井上麻里奈サンタ01',
	'18' : '伊藤かな恵サンタ01',
	'19' : '伊藤かな恵サンタ02',
	'20' : '伊藤かな恵サンタ03',
	'21' : '井口裕香サンタ01',
	'22' : '井上麻里奈サンタ01',
	'23' : '井上麻里奈サンタ02',
	'24' : '花澤香菜サンタ01',
	'25' : '花澤香菜サンタ02',
	'26' : '花澤香菜サンタ03',
	'27' : '茅原実里サンタ01',
	'28' : '茅原実里サンタ02',
	'29' : '高垣彩陽サンタ01',
	'30' : '今井麻美サンタ01',
	'31' : '佐倉綾音サンタ01',
	'32' : '三上枝織サンタ＆大久保瑠美サンタ01',
	'33' : '三上枝織サンタ01',
	'34' : '三森すずこサンタ01',
	'35' : '三森すずこサンタ02',
	'36' : '三森すずこサンタ03',
	'37' : '三澤紗千香サンタ01',
	'38' : '小清水亜美サンタ01',
	'39' : '小倉唯サンタ01',
	'40' : '小倉唯サンタ02',
	'41' : '小倉唯サンタ03',
	'42' : '小倉唯サンタ04',
	'43' : '小倉唯サンタ05',
	'44' : '松来未祐サンタ01',
	'45' : '上坂すみれサンタ01',
	'46' : '上坂すみれサンタ02',
	'47' : '上坂すみれサンタ03',
	'48' : '新谷良子サンタ＆阿澄佳奈トナカイ01',
	'49' : '水樹奈々サンタ01',
	'50' : '瀬戸麻沙美サンタ01',
	'51' : '石原夏織サンタ01',
	'52' : '石原夏織サンタ02',
	'53' : '大久保瑠美サンタ01',
	'54' : '竹達彩奈サンタ01',
	'55' : '竹達彩奈サンタ02',
	'56' : '中島愛サンタ01',
	'57' : '中二病サンタ01',
	'58' : '田村ゆかりサンタ01',
	'59' : '田村ゆかりサンタ02',
	'60' : '徳井青空サンタ＆三森すずこサンタ01',
	'61' : '徳井青空サンタ01',
	'62' : '徳井青空サンタ02',
	'63' : '徳井青空サンタ03',
	'64' : '内田真礼サンタ01',
	'65' : '内田真礼サンタ02',
	'66' : '内田真礼サンタ03',
	'67' : '南條愛乃トナカイ01',
	'68' : '日高里菜サンタ01',
	'69' : '豊崎愛生サンタ01',
	'70' : '豊崎愛生サンタ02',
	'71' : '名塚佳織サンタ01'
}

def tweet(filepath, comment):
	twitter = twython.Twython(
    app_key = ApiManager.CONSUMER_KEY,
    app_secret = ApiManager.CONSUMER_SECRET,
    oauth_token = ApiManager.ACCESS_TOKEN,
    oauth_token_secret = ApiManager.ACCESS_TOKEN_SECRET
	)
	photo = open(filepath, 'rb')
	twitter.update_status_with_media(status=comment, media=photo)

files = os.listdir('santa')
i = random.randint(0, len(files)-1)
filename = files[i]
print filename

key = filename.split('.')[0]
state = d[key]
state = state[:len(state)-2]
state = '【メリークリスマス】' + state
print state

TEMPFILE = 'santa/' + files[i]
tweet(TEMPFILE, state)