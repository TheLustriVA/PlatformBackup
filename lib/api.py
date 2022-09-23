# This file will contain functions, handlers, and objects for connecting to various APIs and online services.

from dotenv import load_dotenv
import os
import praw

def get_reddit_session():
    env_path = "lib/.env"       # Set the path for the environment file
    load_dotenv(dotenv_path=env_path)     # Load the environment file

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        refresh_token=os.getenv("REDDIT_REFRESH_TOKEN"),
        user_agent="MonARCH-SI by /u/MediciVA"
    )
    
    return reddit

def get_reddit_client():
    env_path = "lib/.env"       # Set the path for the environment file
    load_dotenv(dotenv_path=env_path)     # Load the environment file

    reddit_temp = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        redirect_uri=os.getenv("REDDIT_REDIRECT"),
        user_agent="MonARCH-SI by /u/MediciVA"
    )

    scopes_list = [
        "account",
        "edit",
        "flair",
        "history",
        "identity",
        "mysubreddits",
        "privatemessages",
        "read",
        "save",
        "submit",
        "subscribe",
        "vote",
        "wikiread" 
    ]

    auth = reddit_temp.auth.url(scopes=scopes_list, state="MonARCH-SI", duration="permanent")
    print(auth)
    
    auth_code = input("Enter the code from the URL: ")
    refresh_token = reddit_temp.auth.authorize(auth_code)
    redditor = reddit_temp.user.me()
    print(refresh_token)
    print(redditor)
    
    with open(".env", "a", encoding="utf-8") as f:
        f.write(f"REDDIT_REFRESH_TOKEN={refresh_token}")

    reddit = get_reddit_session()
    
    return reddit

def get_subreddit_list():
    return ['learnpython', 'redditdev', 'dndmemes']