import requests 
import praw
from analysis import *
from praw.models import MoreComments

class User:
    user_agent = 'python: 3.10.1 (by/Equivalent-Prior-778)'
    client_id = 'KOWBaK7N7TiUqAlkIV5sMA'
    client_secret = 'k06HBMoXReM6_O5iGFp0-4he_r8yHQ'
    username = 'Equivalent-Prior-778'
    password = 'Pigpen123!'

reddit = praw.Reddit(
    client_id = str(User.client_id),
    client_secret = str(User.client_secret),
    user_agent = str(User.user_agent),
)

stock_list = []

for comment in reddit.submission(id = 'rpl3lv').comments:
    if isinstance(comment, MoreComments):
        continue
    parse_comment(comment.body, stock_list)
    

data = clean_data(stock_list)

print(data)