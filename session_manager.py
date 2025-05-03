import os
import json

def save_cookies(context, session_id):
    cookies = context.cookies()
    with open(f"cookies/session_{session_id}.json", "w") as f:
        json.dump(cookies, f)

def load_cookies(context, session_id):
    try:
        with open(f"cookies/session_{session_id}.json", "r") as f:
            cookies = json.load(f)
        context.add_cookies(cookies)
    except FileNotFoundError:
        pass

