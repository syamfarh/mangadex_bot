import os
import praw
from dotenv import load_dotenv, dotenv_values, set_key, find_dotenv

dotenv_file = find_dotenv()
load_dotenv(override=True)

reddit = praw.Reddit(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    user_agent = os.getenv("USER_AGENT"),
)

def prawReddit():
    last_fetched_post_id = os.environ["LAST_FETCHED_POST_ID"]
    subreddit = reddit.subreddit("manga")
    returnList = []
    top_posts = list(subreddit.new(limit=10, params={
                    'before': last_fetched_post_id}))

    if (top_posts):
        os.environ["LAST_FETCHED_POST_ID"] = top_posts[0].fullname
        set_key(dotenv_file, "LAST_FETCHED_POST_ID", os.environ["LAST_FETCHED_POST_ID"])
    for submission in top_posts:
        if ("[DISC]" in submission.title):
            returnList.append("https://www.reddit.com/r/manga/comments/" + submission.id)
    
    return returnList