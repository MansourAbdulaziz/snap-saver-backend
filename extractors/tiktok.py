from pyppeteer import launch

async def extract_tiktok_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto("https://ssstik.io/en", timeout=60000)
    
    await page.waitForSelector("#main_page_text")
    await page.type("#main_page_text", url)
    await page.click("button[type='submit']")

    try:
        await page.waitForFunction(
            """() => {
                const link = document.querySelector("a.without_watermark");
                return link && link.href && link.href.startsWith('http');
            }""",
            timeout=60000
        )
    except Exception:
        await browser.close()
        raise Exception("❌ لم يتم العثور على رابط TikTok داخل الصفحة")

    link = await page.querySelector("a.without_watermark")
    download_url = await page.evaluate("(el) => el.href", link)

    await browser.close()
    return download_url
