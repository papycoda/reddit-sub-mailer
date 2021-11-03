import praw
import random
import socket
import sys
import re
from praw.reddit import Subreddit

reddit = praw.Reddit(
    client_id="q6-o0w0NOIwqCDeuL6UY6Q",
    client_secret="blWovLnpyxxuSnjl-ACiAoe_C9shoA",
    refresh_token = "622219923593-2HnNHnN6Vc8-OGHfb1uykhUmBeREog", #final oauth step
    redirect_uri="https://www.reddit-mailer.herokuapp.com",
    user_agent="sub-mailer",
)
state = str(random.randint(0, 65000))
url = reddit.auth.url(["account","subscribe","mysubreddits","identity","read"], state, "permanent") #step 1 to get authentication for user
print(f"Now open this url in your browser: {url}")
#print(reddit.auth.authorize('w2mBRzK4HDgO08LJvDzkPGJBkJUdcA'))# step 2 to print refresh token
print(reddit.user.me()) # step 3 to check if user is logged in
#print(reddit.auth.scopes())
for subreddit in reddit.user.subreddits(limit=None):
    subs = (str(subreddit))
    print(subs)
    top3 = subreddit.hot(limit=3)
    for submission in top3:
        print(submission.title, submission.url, end='\n')
    

#to do: get top 3 posts of all subreddits for the day, then send users only the one they're concerned with by selecting the category from the database.
#or just continue with this trend but make it dynamic.. enerating different results per user. which means it has to store praw instances for every new user
