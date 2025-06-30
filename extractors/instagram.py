# extractors/instagram.py

import asyncio
from pyppeteer import launch

async def extract_instagram_video(url: str) -> str:
    print("🚀 بدء تحميل المتصفح...")
    browser = await launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox"]
    )
    try:
        page = await browser.newPage()
        print("🌐 فتح صفحة SnapSave...")
        await page.goto("https://snapsave.app/instagram-downloader", timeout=90000)

        print("⌛ انتظار حقل الإدخال...")
        await page.waitForFunction(
            'document.querySelector("#s_input") !== null',
            timeout=90000
        )

        await page.type("#s_input", url)
        await page.click("#submit")
        print("📨 تم لصق الرابط والضغط على زر التحميل")

        print("⌛ انتظار رابط التحميل...")
        await page.waitForFunction(
            """() => {
                const btn = document.querySelector('a.button.is-success');
                return btn && btn.href && btn.href.startsWith('http');
            }""",
            timeout=90000
        )

        element = await page.querySelector("a.button.is-success")
        download_url = await page.evaluate('(el) => el.href', element)

        print(f"✅ تم استخراج الرابط: {download_url}")
        return download_url

    except Exception as e:
        print(f"❌ خطأ أثناء الاستخراج: {str(e)}")
        raise Exception("❌ لم يتم العثور على رابط التحميل داخل الصفحة أو حدث خطأ أثناء الانتظار.")

    finally:
        await browser.close()
        print("🧹 تم إغلاق المتصفح")
