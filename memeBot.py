import praw
import time
from pprint import pprint
import requests
import json
import os


while True:
	#don't forget to use export REDDIT_MEME_PW= to reset password dummy
	pw=os.environ['REDDIT_MEME_PW']
	r = praw.Reddit('Meme making creator')
	r.login('makemememe',pw)
	messages = r.get_unread()
	
	for m in messages:
		body = m.body.lstrip('/umakeme ')
		if 'help' in m.body:
			m.reply("Hey budy! Thanks for pinging the help desk. Each command starts with /u/makemememe and can be followed by:    \n* help: That pulls up this menu dummy!    \n* list: list the full list of memes available, and what you have to type to get them   \n* meme: actually creating the meme. ")
			m.mark_as_read()
		elif 'create' in m.body or 'new' in m.body or 'meme' in m.body:
			if ':' in m.body:
				[init, splitter, rest] = body.partition(':')
				[meme,splitter,rest] = rest.partition(',')
				[disc,splitter,rest] = rest.partition(':')
				[text1, splitter, rest] = rest.partition(',')
				[disc,splitter,text2] = rest.partition(':')
				meme = meme.lower()
				if "bad" in meme and "luck" in meme:
					template='61585'
				if "one" in meme and "does" in meme and "simply" in meme:
					template='61579'
				if "batman" in meme:
					template='438680'
				if 'interesting' in meme and 'world' in meme:
					template= '61532'
				if 'aliens' in meme:
					template = '101470'
				if 'futurama' in meme:
					template='61520'
				if 'everywhere' in meme:
					template ='347390'
				if 'dicaprio' in meme and 'cheers' in meme:
					template='5496396'
				if 'is' in meme and 'coming' in meme:
					template='61546'
				if 'y u' in meme and 'no' in meme:
					template='61527'
				if 'first' in meme:
					template='61539'
				if 'none' in meme and 'business' in meme:
					template='16464531'
				if 'wonka' in meme:
					template='61582'
				if 'would' in meme and 'great' in meme:
					template='563423'
				if 'success' in meme and 'kid' in meme:
					template='61544'
				if 'grumpy' in meme:
					template = '405658'
				if 'third' in meme and 'skeptical' in meme:
					template ='101288'
				if 'picard' in meme and 'facepalm' in meme:
					template='1509839'
				if 'doge' in meme:
					template='8072285'
				if 'matrix' in meme:
					template='100947'
				if 'x all' in meme:
					template='61533'
				if 'picard' in meme and 'wtf' in meme:
					template='245898'
				if 'am i' in meme:
					template='259680'
				if 'evil' in meme and 'toddler' in meme:
					template='235589'
				if 'evil' in meme and 'laser' in meme:
					template='40945639'
				if 'philosoraptor' in meme:
					template='61516'
				if 'maury' in meme:
					template='444501'
				if 'damn' in meme and 'high' in meme:
					template='61580'
				if 'disaster' in meme:
					template ='97984'
				if 'third world' in meme and 'success' in meme:
					template='101287'
				if 'confession' in meme:
					template='100955'
				if 'grandma' in meme and 'internet' in meme:
					template='61556'
				if 'awkward' in meme and 'sea' in meme:
					template='13757816'
				if 'yo dawg' in meme:
					template='101716'
				if 'loses their' in meme or 'joker' in meme:
					template='101716'
				if '10 guy' in meme or 'high guy' in meme:
					template='101440'
				if 'sparta' in meme or 'leonidas' in meme or '300' in meme:
					template='195389'
				if 'keanu' in meme:
					template='61583'
				if 'back in' in meme or 'angry old' in meme:
					template='718432'
				if 'kill' in meme and 'yourself' in meme:
					template='172314'
				if 'overly' in meme and 'attached' in meme:
					template='100952'
				if 'mvp' in meme:
					template='15878567'
				if 'mugatu' in meme or 'so hot' in meme:
					template='21604248'
				if 'buy' in meme and 'boat' in meme:
					template='1367068'
				if 'scumbag' in meme:
					template='61522'
				if 'got any more' in meme:
					template='13424299'
				if 'spiderman' in meme or 'masturbating' in meme:
					template='1366993'
				if 'ermahgerd' in meme or 'berks' in meme:
					template='101462'
				if 'awkward' in meme and 'awesome' in meme and 'penguin' in meme:
					template='61584'
				if 'christ' in meme:
					template='17699'
				if 'pepperidge' in meme:
					template='1232104'
				if 'wolf' in meme and 'wall' in meme:
					template='17496002'
				if 'archer' in meme:
					template='10628640'
				if 'jackie' in meme and 'wtf' in meme:
					template='412211'
				if 'grinds' in meme or 'peter griffin' in meme:
					template='356615'
				if 'clarity' in meme:
					template='100948'
				if 'goin for' in meme:
					template='8774527'
				if 'satisfied' in meme and 'seal' in meme:
					template='23909796'
				if 'shut' in meme and 'take' in meme:
					template='176908'
				if 'gollum' in meme:
					template='681831'
				if 'puffin' in meme:
					template='7761261'
				if 'live' in meme and 'dangerously' in meme:
					template='646581'
				if 'ron burgundy' in meme or 'ron burgandy' in meme:
					template='1232147'
				if 'dwight' in meme:
					template='61554'
				if 'awkward' in meme and 'penguin' in meme:
					template='61524'
				if 'malicious' in meme and ('mallard' in meme or 'duck' in meme):
					template='1595847'
				if 'advice' in meme and ('mallard' in meme or 'duck' in meme):
					template='1356640'
				# print meme
				# print text1
				# print text2
				url = 'https://api.imgflip.com/caption_image'
				data = {'template_id':template, 'username':'infobiac', 'password':pw, 'text0':text1,'text1':text2}
				r = requests.post(url,data=data)
				dic = json.loads(r.text)
				print dic
				yes = dic['data']['url']
				m.reply(yes)
				m.mark_as_read()
	time.sleep(2)
	#m.reply("Heya there bucko")
	#m.mark_as_read()