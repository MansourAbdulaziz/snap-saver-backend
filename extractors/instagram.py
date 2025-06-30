# extractors/instagram.py

import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    browser = await launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-blink-features=AutomationControlled"
        ]
    )
    page = await browser.newPage()
    
    # الانتقال لصفحة التحميل مع انتظار تحميل الـ DOM
    await page.goto("https://snapsave.app/instagram-downloader", {
        "timeout": 60000,
        "waitUntil": "domcontentloaded"
    })

    # مهلة قصيرة للسماح بتحميل العناصر الديناميكية
    await asyncio.sleep(3)

    # الانتظار لعنصر الإدخال
    await page.waitForSelector("#s_input", timeout=60000)
    await page.type("#s_input", url)
    await page.click("#submit")

    try:
        # استخدام waitForFunction للتحقق من الزر والرابط
        await page.waitForFunction(
            """() => {
                const btn = document.querySelector('a.button.is-success');
                return btn && btn.href && btn.href.startsWith('http');
            }""",
            timeout=60000
        )
    except Exception:
        await browser.close()
        raise Exception("❌ لم يتم العثور على رابط التحميل داخل الصفحة")

    # استخراج الرابط
    element = await page.querySelector("a.button.is-success")
    download_url = await page.evaluate('(el) => el.href', element)

    await browser.close()
    return download_url
