import asyncio
from pyppeteer import launch

async def extract_facebook_video(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://snapsave.app/facebook", timeout=60000)
    await page.type("input[name='url']", url)
    await page.click("button[type='submit']")

    await page.waitForFunction(
        'document.querySelector("a.button.is-success") !== null',
        timeout=60000
    )

    element = await page.querySelector("a.button.is-success")
    download_url = await page.evaluate('(el) => el.href', element)

    await browser.close()
    return download_url
