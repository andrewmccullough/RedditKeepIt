import praw

# Visit the PRAW website for instructions on installation and configuration.
# https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application

username="" #Your username.

reddit = praw.Reddit(
    client_id = "", #14 character code.
    client_secret = "", #27 character code.
    password = "", #Your password. Feel free to review my code to ensure it's not being used in a way you don't like.
    user_agent = "", #Can be whatever you want.
    username = username #Do not modify.
)

subreddit_array = [
    "",
    "",
    "" #Add more if you'd like.
]
