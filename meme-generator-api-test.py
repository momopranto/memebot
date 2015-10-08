import json, requests

DEFAULT_IMG_HEIGHT = [{'height':200}]

def list_memes():
    r = requests.get('http://api.imgflip.com/get_memes')
    memelist = r.json()['data']['memes']
    for i, meme in enumerate(memelist):
	print meme['id'] + ': ' + meme['name']

def create_meme(MID, t0, t1):
    payload = {
	'username': 'slackmemebot',
	'password': 'memememe',
	'template_id': 306319,
	'text0': 'Top text',
	'text0': 'bOTTOM text'
    }
    r = requests.post("https://api.imgflip.com/caption_image", data=payload)
    print r.text

#list_memes()
create_meme(306319, 'such memes', 'much stress')

