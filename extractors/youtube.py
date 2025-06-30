import yt_dlp

async def extract_youtube_video(url: str) -> str:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'mp4',
        'forcejson': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info['url']
        except Exception:
            raise Exception("❌ فشل استخراج رابط YouTube")
