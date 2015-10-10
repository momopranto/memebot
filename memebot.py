from slackclient import SlackClient
import requests, json, time

HELP = "Options: \n!help, display this menu\n!list, list available memes\n!prev <meme_id>, preview a meme template\n!make <meme_id> <top_text> <bottom_text>, create meme\n"

tok = 'xoxb-11791613732-SXbxlkDUMCXcezRujSGEuD73'
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
	'password': 'slackmemebot',
	'username': 'memememe',
    }
    r = requests.post("http://api.imgflip.com/caption_image", data=payload)
    response = r.json()
    if response['success']==True:
	return response['data']['url']
    else:
	return None

def send_msg(msg, chan):
    sc.api_call("chat.postMessage", as_user=True, channel=chan, username=bot_id, text=msg)

#list_memes('G0BPCSJHE')
#print memelist
send_msg(view_template(306319),'G0BPCSJHE')
