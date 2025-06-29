import requests
from bs4 import BeautifulSoup

def extract_instagram_video(url: str) -> str:
    try:
        session = requests.Session()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Referer": "https://snapsave.app",
            "Origin": "https://snapsave.app",
        }

        data = {
            "url": url,
            "lang": "en"
        }

        response = session.post(
            "https://snapsave.app/action.php",
            headers=headers,
            data=data,
            timeout=15
        )
        response.raise_for_status()

        # طباعة المحتوى الأولي للصفحة HTML
        print("🔵 HTML RESPONSE:\n", response.text[:1000])

        soup = BeautifulSoup(response.text, "html.parser")
        link = soup.find("a", attrs={"target": "_blank", "rel": "nofollow"})

        if link and link.has_attr("href"):
            return link["href"]
        else:
            raise Exception("لم يتم العثور على رابط التحميل من الموقع")

    except Exception as e:
        print("🔴 خطأ أثناء استخراج الفيديو:", e)
        raise Exception("حدث خطأ في استخراج الفيديو: " + str(e))
