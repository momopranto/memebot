from slackclient import SlackClient
import json, time

tok = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
sc = SlackClient(tok)
data = json.loads(sc.api_call("rtm.start", token=tok))
bot_id = data['self']['id']
team_id = data['team']['id']
groups = data['groups']
channels = data['channels']
users = data['users']
bots = data['bots']

def sendMsg(msg, chan):
    sc.api_call("chat.postMessage", as_user=True, channel=chan, username=bot_id, text=msg)


last_msg = None
if sc.rtm_connect():
    while True:
	latest = sc.rtm_read()
	time.sleep(1)
	try:
            latest[0]
    	except:
            continue
	if (latest[0]['type']=='message'):
	    latestMsg = latest[0]['text']
	    print latestMsg, latest[0]['channel']
	    if(latestMsg != last_msg):
        	last_msg = latestMsg
	    if (latestMsg.lower().find('doot')>=0):
		sendMsg('Thank you, Mr.Skeletal.', latest[0]['channel'])
		print "sent"
else:
    print "Connection failed. Make sure token is valid.\n"
