import asyncio
from pyppeteer import launch

async def extract_facebook_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
    page = await browser.newPage()
    await page.goto("https://snapsave.app/facebook-video-downloader", {"timeout": 60000, "waitUntil": "domcontentloaded"})
    await asyncio.sleep(3)
    await page.waitForSelector("#s_input", timeout=60000)
    await page.type("#s_input", url)
    await page.click("#submit")
    try:
        await page.waitForFunction(
            "() => document.querySelector('a.button.is-success')?.href?.startsWith('http')",
            timeout=60000
        )
    except Exception:
        await browser.close()
        raise Exception("❌ لم يتم العثور على رابط التحميل داخل الصفحة")
    element = await page.querySelector("a.button.is-success")
    download_url = await page.evaluate("(el) => el.href", element)
    await browser.close()
    return download_url
