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

def prawReddit(user_data):
    last_fetched_post_id = user_data["recent_post_id"]
    subreddit = reddit.subreddit(user_data["subreddit"])
    returnList = []
    if (checkRemoved(last_fetched_post_id)):
        top_posts = list(subreddit.new(limit=10))
    else:
        top_posts = list(subreddit.new(limit=None, params={
                    'before': last_fetched_post_id}))
    if (top_posts):
        user_data["subreddit"] = top_posts[0].fullname
    for submission in top_posts:
        if (user_data["keyword"] != ""):
            if (user_data["keyword"] in submission.title):
                returnList.append("https://www.reddit.com" + submission.permalink)
        else:
            returnList.append("https://www.reddit.com" + submission.permalink) 
    return returnList

def checkRemoved(last_fetched_post_id):
    if (last_fetched_post_id == ""):
        return True
    post2 = reddit.submission(id=last_fetched_post_id[3:])
    return not(post2.removed_by_category is None)

def subExists(sub):
    try:
        reddit.subreddits.search_by_name(sub, exact=True, include_nsfw=True)
        return True
    except:
        return False

if __name__ == '__main__':
    user_data1 = {"recent_post_id": "", "subreddit": "manga", "keyword": "[DISC]"}
    user_data2 = {"recent_post_id": "", "subreddit": "nsfw", "keyword": ""}
    print(prawReddit(user_data2))