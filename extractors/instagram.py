import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    try:
        await page.goto("https://snapsave.app", timeout=60000)
        await page.type('input[name="url"]', url)
        await page.click('button[type="submit"]')
        await page.waitForFunction('document.querySelector("a.button.is-success") !== null', timeout=60000)
        link = await page.querySelector("a.button.is-success")
        return await page.evaluate('(el) => el.href', link) if link else None
    finally:
        await browser.close()
