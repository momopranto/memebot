import json, requests

DEFAULT_IMG_HEIGHT = [{'height':200}]

def list_memes():
    r = requests.get('http://api.imgflip.com/get_memes')
    memelist = r.json()['data']['memes']
    for i, meme in enumerate(memelist):
	print meme['id'] + ': ' + meme['name']

def create_meme(MID, t0, t1):
    payload = {
	'template_id': MID,
	'text0': t0,
	'text1': t1,
	'username': 'XXXXXXXX',
	'password': 'XXXXXXXX',	
	'boxes': DEFAULT_IMG_HEIGHT
    }
    r = requests.post('https://api.imgflip.com/caption_image', params=payload)
    print r.text

#list_memes()
create_meme(306319, 'such memes', 'much stress')

