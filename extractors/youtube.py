import yt_dlp

async def extract_youtube_video(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best',
        'forcejson': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get("url")
