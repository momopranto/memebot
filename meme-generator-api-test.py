import json, requests

def list_memes():
    r = requests.get('http://api.imgflip.com/get_memes')
    memelist = r.json()['data']['memes']
    for meme in memelist:
	print meme['id'] + ': ' + meme['name']

def create_meme(MID, t0, t1):
    payload = {
	'username': 'slackmemebot',
	'password': 'memememe',
	'template_id': MID,
	'text0': t0,
	'text1': t1,
    }
    r = requests.post("http://api.imgflip.com/caption_image", data=payload)
    print r.json()['data']['url']

#list_memes()
create_meme(306319, 'such memes', 'much stress')

