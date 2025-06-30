import asyncio
from pyppeteer import launch

async def extract_youtube_video(url: str) -> str:
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    try:
        await page.goto("https://ssyoutube.com", timeout=60000)
        await page.type('input[type="text"]', url)
        await page.keyboard.press('Enter')
        await page.waitForFunction('document.querySelector("a.link-download") !== null', timeout=60000)
        link = await page.querySelector("a.link-download")
        return await page.evaluate('(el) => el.href', link) if link else None
    finally:
        await browser.close()
