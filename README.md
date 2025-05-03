# 🕵️‍♂️ Web Scraping & Automation Starter Template (Playwright + HTTPx + Stealth)

A powerful starter template for building **undetectable web scrapers** and **browser automation bots**.  
Combines `Playwright` for dynamic interaction, `httpx` for high-speed parallel scraping, and advanced **browser fingerprint evasion**.

---

## 🚀 Features

✅ **Headless Browser Automation (Playwright)**  
✅ **Async HTTP Scraping (httpx + asyncio)**  
✅ **Proxy Rotation with Retry Logic**  
✅ **Browser Fingerprint Spoofing (WebGL, Canvas, AudioContext)**  
✅ **Login + Pagination Support**  
✅ **Session Cookie Persistence**  

---

## 📦 Tech Stack

- [Playwright (Python)](https://playwright.dev/python/)
- [httpx](https://www.python-httpx.org/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [Residential Proxy Support]
- Fingerprint injection via JavaScript

---

## 📁 Project Structure

```
scraper_project/
├── main.py                      # Entry point
├── config.py                    # Target URLs, headers, proxies
├── fingerprint.py               # User-Agent & viewport randomizer
├── proxy_manager.py             # Proxy selection + failure marking
├── session_manager.py           # Cookie save/load logic
├── playwright_worker.py         # Browser scraping logic
├── http_worker.py               # Async HTTP scraping logic
├── fingerprint_inject.js        # Injected browser fingerprint spoof
└── cookies/                     # Stores session cookies
```
---

## 🔐 Anti-Bot Techniques Used

| Technique                     | Benefit                                      |
|------------------------------|----------------------------------------------|
| Canvas & WebGL Spoofing      | Avoid detection via rendering fingerprint    |
| AudioContext Entropy Control | Mitigates audio fingerprint uniqueness       |
| Random Headers & Viewport    | Prevent pattern clustering                   |
| Proxy Rotation               | Avoid IP bans and geo-restrictions           |
| Retry on Proxy Failure       | Increases scraping resilience                |
| Session Cookie Reuse         | Prevent re-logins and redundant detection    |

---

## 💻 How to Run

```bash
# Install dependencies
pip install playwright httpx

# Install browsers
playwright install

# Run the scraper
python main.py
```

> ✅ Make sure to replace dummy credentials, selectors, and URLs in `playwright_worker.py`.

---

## ✏️ Use Cases

- Login-required dashboards (admin panels, social media)
- E-commerce product data scrapers
- Real estate listings / paginated APIs
- Teaching stealth automation & anti-bot bypass techniques

---

## 🔧 Customize This Template

- Add captcha solving (e.g., 2captcha or AI)
- Integrate headless container deployment (Docker)
- Store extracted data to SQLite, CSV, or Elasticsearch
- Add TOR or rotating proxy service

---

## 🤝 License

MIT License.  
This template is for **educational and ethical scraping purposes** only. Do not use against sites that disallow scraping in their Terms of Service.

---

## 🙋‍♂️ Want Help or Custom Solutions?

Need a custom scraper built for your SaaS product, internal dashboard, or research project?

📩 Contact me via [LinkedIn](https://www.linkedin.com/in/jerry-luong-605037233/) happy to help!