import praw

REDDIT_APP_ID = "A_pvXoSDWS2pSRHnj2JE6w"
REDDIT_APP_SECRET = "BBvkuqxXtDvuDGKSu1S7-kS2OYjJpA"

reddit = praw.Reddit(client_id=REDDIT_APP_ID,client_secret=REDDIT_APP_SECRET,user_agent="efc_reditv1")

subreddit = reddit.subreddit("python")
hot_python = subreddit.hot(limit=5)
for submission in hot_python:
    if not submission.stickied:
        print(submission.title)
