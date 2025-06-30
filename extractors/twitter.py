import asyncio
from pyppeteer import launch

async def extract_twitter_video(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://twdown.net/", timeout=60000)
    await page.type("input[name='URL']", url)
    await page.click("button[type='submit']")

    await page.waitForFunction(
        'document.querySelector("a.download-button") !== null',
        timeout=60000
    )

    element = await page.querySelector("a.download-button")
    download_url = await page.evaluate('(el) => el.href', element)

    await browser.close()
    return download_url
