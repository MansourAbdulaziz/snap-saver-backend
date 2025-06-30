import asyncio
from pyppeteer import launch

async def extract_facebook_video(url: str) -> str:
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    try:
        await page.goto("https://fdown.net", timeout=60000)
        await page.type('input[name="URLz"]', url)
        await page.click('button[type="submit"]')
        await page.waitForFunction('document.querySelector("a[download]") !== null', timeout=60000)
        link = await page.querySelector("a[download]")
        return await page.evaluate('(el) => el.href', link) if link else None
    finally:
        await browser.close()
