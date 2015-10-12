# Memebot

Python Slack bot for generating context based memes


### Setup:

1. First, you need to have a slack account and join a team
2. Next, [create](https://my.slack.com/services/new/bot) a new bot user and generate an API token
3. [Sign up](https://imgflip.com/signup) for an imgflip account if you dont already have one
4. Edit memebot.py to include the information obtained from above
5. Enjoy!

#### Required Packages:

You will need the slackclient and requests libraries. If you do not have them they can be installed with pip:

```
sudo pip install <package-name>
```
Where package name would be slackclient or requests. If you do not have pip giyf :)

### Usage:

```
!help, display this menu
!list, list available templates
!prev <meme_id>, preview a template
!make <meme_id> !top <top_text> !bot <bottom_text>, create a meme
```
