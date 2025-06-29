import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    try:
        await page.goto("https://snapsave.app", timeout=60000)
        await page.type('input[name="url"]', url)
        await page.click('button[type="submit"]')
        await page.waitForSelector("a.button.is-success", timeout=20000)

        link = await page.querySelector("a.button.is-success")
        if link:
            href = await page.evaluate('(el) => el.href', link)
            return href
        else:
            raise Exception("لم يتم العثور على رابط التحميل من الموقع")
    finally:
        await browser.close()
