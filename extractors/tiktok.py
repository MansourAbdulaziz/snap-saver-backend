import asyncio
from pyppeteer import launch

async def extract_tiktok_video(url: str) -> str:
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    try:
        await page.goto("https://snaptik.app", timeout=60000)
        await page.type('#url', url)
        await page.click('#submiturl')
        await page.waitForFunction('document.querySelector("a.without_watermark") !== null', timeout=60000)
        link = await page.querySelector("a.without_watermark")
        return await page.evaluate('(el) => el.href', link) if link else None
    finally:
        await browser.close()
