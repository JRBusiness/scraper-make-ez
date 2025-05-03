import asyncio
from playwright_worker import run_playwright_scraper
from http_worker import run_http_scraper

if __name__ == "__main__":
    asyncio.run(run_http_scraper())
    run_playwright_scraper()
