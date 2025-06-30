import asyncio
from pyppeteer import launch

async def extract_instagram_video(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://snapsave.app/instagram", timeout=60000)
    await page.type("#url", url)
    await page.click("button[type='submit']")
    
    # الانتظار حتى يظهر رابط التحميل (نستخدم waitForFunction بدل waitForSelector)
    await page.waitForFunction(
        'document.querySelector("a.button.is-success") !== null',
        timeout=60000
    )
    
    element = await page.querySelector("a.button.is-success")
    download_url = await page.evaluate('(el) => el.href', element)
    
    await browser.close()
    return download_url
