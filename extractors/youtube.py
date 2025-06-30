import yt_dlp

async def extract_youtube_video(url: str) -> str:
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'forcejson': True,
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict.get("url") or info_dict["formats"][0]["url"]
    except Exception:
        raise Exception("❌ لم نتمكن من استخراج رابط تحميل اليوتيوب.")
