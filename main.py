import requests 
import praw

reddit = praw.Reddit(
    user_agent = 'comment extraction from wsb (by u/Equivalent-Prior-778)',
    client_id = 'KOWBaK7N7TiUqAlkIV5sMA',
    client_secret = 'k06HBMoXReM6_O5iGFp0-4he_r8yHQ',
    username = 'Equivalent-Prior-778',
    password = 'Pigpen123!',
)
url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url = url)
print(submission.comments)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
    print('-----------')
