from playwright.sync_api import sync_playwright
from fingerprint import get_random_headers, get_random_viewport
from proxy_manager import get_random_proxy
from session_manager import save_cookies, load_cookies
import uuid

def run_playwright_scraper():
    session_id = str(uuid.uuid4())
    proxy = get_random_proxy()
    headers = get_random_headers()
    viewport = get_random_viewport()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy={"server": proxy})
        context = browser.new_context(
            user_agent=headers["User-Agent"],
            viewport=viewport,
            locale="en-US",
        )
        load_cookies(context, session_id)
        page = context.new_page()

        with open("fingerprint_inject.js") as f:
            js_script = f.read()
        page.add_init_script(js_script)

        page.goto("https://example.com/login")
        # Example login
        # page.fill("input[name='username']", "youruser")
        # page.fill("input[name='password']", "yourpass")
        # page.click("button[type='submit']")
        page.wait_for_timeout(2000)

        page.goto("https://example.com/data")
        while True:
            content = page.content()
            print(content[:500])  # Truncate output
            if not page.locator("text=Next").is_visible():
                break
            page.click("text=Next")
            page.wait_for_timeout(2000)

        save_cookies(context, session_id)
        context.close()
        browser.close()
