user_data = {}

def add_user(id):
    if id not in user_data:
        user_data[id] = {}
        user_data[id]["subreddit"] = ""
        user_data[id]["recent_post_id"] = ""
        user_data[id]["keyword"] = ""
    user_data[id]["cont_loop"] = ""

def update_recent_id(id):
    user_data[id]["recent_post_id"] = ""

def add_subreddit_to_user(message):
    user_data[message.from_user.id]["subreddit"] = message.text
    
def add_keyword_to_user(message):
    user_data[message.from_user.id]["keyword"] = message.text.lower()
    

def off_loop(id):
    user_data[id]["cont_loop"] = ""

def on_loop(id):
    user_data[id]["cont_loop"] = user_data[id]["subreddit"]
