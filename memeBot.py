import praw
import time
from pprint import pprint
import requests
import json


while True:
	r = praw.Reddit('Meme making creator')
	r.login('makemememe','')
	messages = r.get_unread()
	for m in messages:
		if 'help' in m.body:
			continue
		elif 'create' in m.body or 'new' in m.body:
			body = m.body.lstrip('/umakeme ')
			[init, splitter, rest] = body.partition(':')
			[meme,splitter,rest] = rest.partition(',')
			[disc,splitter,rest] = rest.partition(': ')
			[text1, splitter, rest] = rest.partition(',')
			[disc,splitter,text2] = rest.partition(':')
			# print meme
			# print text1
			# print text2
			url = 'https://api.imgflip.com/caption_image'
			data = {'template_id':'61585', 'username':'infobiac', 'password':'', 'text0':text1,'text1':text2}
			r = requests.post(url,data=data)
			dic = json.loads(r.text)
			yes = dic['data']['url']
			m.reply(yes)
			m.mark_as_read()
	time.sleep(10)
	#m.reply("Heya there bucko")
	#m.mark_as_read()