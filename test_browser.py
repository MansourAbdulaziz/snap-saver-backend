from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # تشغيل المتصفح بوضع مرئي
    page = browser.new_page()
    page.goto("https://snapsave.app", timeout=60000)

    input("📌 الصق رابط إنستقرام داخل الموقع يدويًا، ثم اضغط Enter بعد ظهور رابط التحميل...")
    page.screenshot(path="page.png")  # يلتقط صورة للصفحة لحفظها
    print("✅ تم حفظ صورة الصفحة باسم page.png")
