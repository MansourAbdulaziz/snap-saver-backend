import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    try:
        # فتح موقع SnapSave
        await page.goto("https://snapsave.app", timeout=60000)

        # لصق رابط إنستقرام
        await page.type('input[name="url"]', url)

        # الضغط على زر التحميل
        await page.click('button[type="submit"]')

        # التقاط لقطة شاشة بعد الضغط (للتصحيح لاحقًا)
        await page.screenshot({'path': 'debug.png'})

        # انتظار ظهور زر التحميل (حتى 40 ثانية)
        await page.waitForSelector("a.button.is-success", timeout=40000)

        # استخراج رابط التحميل
        link = await page.querySelector("a.button.is-success")
        if link:
            href = await page.evaluate('(el) => el.href', link)
            return href
        else:
            raise Exception("❌ لم يتم العثور على زر التحميل.")
    finally:
        await browser.close()
