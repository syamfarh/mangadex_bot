user_data = {}

def add_user(id):
    if id not in user_data:
        user_data[id] = {}
        user_data[id]["subreddit"] = ""
        user_data[id]["recent_post_id"] = ""
        user_data[id]["keyword"] = ""

def add_subreddit_to_user(message):
    user_data[message.from_user.id]["subreddit"] = message.text
