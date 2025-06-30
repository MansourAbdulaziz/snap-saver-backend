import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    try:
        await page.goto("https://snapsave.app", timeout=60000)
        await page.type('input[name="url"]', url)
        await page.click('button[type="submit"]')

        # ✅ انتظار الزر الذي يحتوي على "Download" باستخدام waitForFunction
        await page.waitForFunction(
            '''() => {
                const btns = document.querySelectorAll("a.button");
                return Array.from(btns).some(btn => btn.innerText.toLowerCase().includes("download"));
            }''',
            timeout=60000
        )

        # ✅ العثور على الزر الذي يحتوي على "Download"
        link = await page.querySelector('a.button.is-success')
        if link:
            href = await page.evaluate('(el) => el.href', link)
            return href
        else:
            raise Exception("❌ لم يتم العثور على رابط التحميل في الصفحة.")
    finally:
        await browser.close()

# للتجربة المباشرة
if __name__ == "__main__":
    test_url = "https://www.instagram.com/reel/Cxyz123AbcD/"
    print("⏳ استخراج الرابط...")
    result = asyncio.get_event_loop().run_until_complete(extract_instagram_video(test_url))
    print("✅ رابط التحميل:", result)
