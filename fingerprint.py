import random
from config import HEADERS_POOL

def get_random_headers():
    return random.choice(HEADERS_POOL)

def get_random_viewport():
    return {"width": random.randint(1024, 1920), "height": random.randint(768, 1080)}
