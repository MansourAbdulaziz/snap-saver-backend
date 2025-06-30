from pyppeteer import launch

async def extract_twitter_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto("https://twdown.net/", timeout=60000)

    await page.waitForSelector("#url")
    await page.type("#url", url)
    await page.click("button[type='submit']")

    try:
        await page.waitForFunction(
            """() => {
                const btn = document.querySelector('a.download-link');
                return btn && btn.href && btn.href.startsWith('http');
            }""",
            timeout=60000
        )
    except Exception:
        await browser.close()
        raise Exception("❌ لم يتم العثور على رابط تويتر داخل الصفحة")

    element = await page.querySelector("a.download-link")
    download_url = await page.evaluate('(el) => el.href', element)

    await browser.close()
    return download_url
