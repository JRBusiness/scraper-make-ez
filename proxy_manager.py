import random
from config import PROXY_LIST

def get_random_proxy():
    return random.choice(PROXY_LIST)

def mark_proxy_dead(proxy):
    # Placeholder: mark this proxy as failed in your pool
    print(f"Proxy failed: {proxy}")
