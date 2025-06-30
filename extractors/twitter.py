import asyncio
from pyppeteer import launch

async def extract_twitter_video(url: str) -> str:
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    try:
        await page.goto("https://twdown.net", timeout=60000)
        await page.type('input[name="URL"]', url)
        await page.click('button[type="submit"]')
        await page.waitForFunction('document.querySelector("a.download-button") !== null', timeout=60000)
        link = await page.querySelector("a.download-button")
        return await page.evaluate('(el) => el.href', link) if link else None
    finally:
        await browser.close()
