from slackclient import SlackClient
import requests, json, time
 
HELP = "Options: \n!help, display this menu\n!list, list available memes\n!prev <meme_id>, preview a meme template\n!make <meme_id> !top <top_text> !bot <bottom_text>, create meme\n"

tok = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
sc = SlackClient(tok)
data = json.loads(sc.api_call("rtm.start", token=tok))
team_id = data['team']['id']
bot_id = data['self']['id']
groups = data['groups']
channels = data['channels']
users = data['users']
bots = data['bots']
r = requests.get('http://api.imgflip.com/get_memes')
memelist = r.json()['data']['memes']
 
def list_memes(chan):
    l = ""
    for meme in memelist:
        l = l + meme['id'] + ': ' + meme['name'] + '\n'
    payload = [{
       'fallback': "List of memes and their IDs",
       'title': "Meme List",
       'pretext': "List of memes and their IDs",
       'text': l
    }]
    attach = json.dumps(payload)
    sc.api_call("chat.postMessage", as_user=True, channel=chan, username=bot_id, attachments=attach)

def view_template(MID):
    for meme in memelist:
       if int(meme['id'])==int(MID):
           return meme['url']

def create_meme(MID, t0, t1):
    payload = {
       'text1': t1,
       'text0': t0,
       'template_id':MID,
       'password': 'xxxxxxxxxxx',
       'username': 'xxxxxxxxxxx',
    }
    r = requests.post("http://api.imgflip.com/caption_image", data=payload)
    response = r.json()
    if response['success']==True:
	return response['data']['url']
    else:
	return None
 
def send_msg(msg, chan):
    sc.api_call("chat.postMessage", as_user=True, channel=chan, username=bot_id, text=msg)
 
last_msg = None
if sc.rtm_connect():
    while True:
	latest = sc.rtm_read()
	time.sleep(1)
	try:
	    latest[0]['text']
	except:
	    continue
	if latest[0]['type']=='message':
	    #print latest[0]
	    latestMsg = latest[0]['text']
	    #print latestMsg, latest[0]['channel']
	    if latestMsg!=last_msg:
		last_msg = latestMsg
	    	if latestMsg.find(bot_id)>=0:
		    print "Received"
		    if latestMsg.find('!help')>=0:
			send_msg(HELP, latest[0]['channel'])
		    elif latestMsg.find('!list')>=0:
			list_memes(latest[0]['channel'])
		    elif latestMsg.find('!prev')>=0:
			prev = latestMsg.split(' ')
			send_msg(view_template(int(prev[2])),latest[0]['channel'])
		    elif latestMsg.find('!make')>=0:
			meme_id = int(latestMsg[(latestMsg.find('!make')+5):latestMsg.find('!top')])
			top = latestMsg[(latestMsg.find('!top')+4):latestMsg.find('!bot')]
			bottom = latestMsg[(latestMsg.find('!bot')+4):]
			send_msg(create_meme(meme_id, top, bottom),latest[0]['channel'])
		    else:
			send_msg(HELP, latest[0]['channel'])
