import asyncio
from pyppeteer import launch

async def extract_tiktok_video(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://snaptik.app/", timeout=60000)
    await page.type("input[name='url']", url)
    await page.click("button[type='submit']")

    await page.waitForFunction(
        'document.querySelector("a.download-link") !== null',
        timeout=60000
    )

    element = await page.querySelector("a.download-link")
    download_url = await page.evaluate('(el) => el.href', element)

    await browser.close()
    return download_url
