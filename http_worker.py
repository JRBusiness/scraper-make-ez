import asyncio
import httpx
from proxy_manager import get_random_proxy, mark_proxy_dead
from fingerprint import get_random_headers

async def fetch(client, url, proxy):
    try:
        response = await client.get(url, timeout=10)
        print(f"Fetched {url}: {response.status_code}")
    except Exception as e:
        mark_proxy_dead(proxy)
        print(f"Retry due to error: {e}")

async def run_http_scraper():
    urls = [f"https://example.com/api/page/{i}" for i in range(1, 6)]
    proxy = get_random_proxy()
    headers = get_random_headers()

    async with httpx.AsyncClient(proxies=proxy, headers=headers) as client:
        tasks = [fetch(client, url, proxy) for url in urls]
        await asyncio.gather(*tasks)
