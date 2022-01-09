import requests 
import praw
from methods import *
from praw.models import MoreComments
API_Key = '4PMmhcfwKg0DsZBddMS8nXRHsyAnxECU'

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

# get comments from reddit:
for comment in reddit.submission(id = 'rrz70p').comments:
    if isinstance(comment, MoreComments):
        continue
    parse_comment(comment.body, stock_list)


counted_data = count_data(stock_list)

sorted_data = sorted(counted_data.items(), key=lambda counted_data: counted_data[1], reverse=True)

print(sorted_data)
