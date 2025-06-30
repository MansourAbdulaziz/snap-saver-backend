from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# ✅ استيراد السكربتات من مجلد extractors
from extractors.instagram import extract_instagram_video
from extractors.tiktok import extract_tiktok_video
from extractors.twitter import extract_twitter_video
from extractors.facebook import extract_facebook_video
from extractors.youtube import extract_youtube_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

@app.post("/api/download")
async def download_video(request: VideoRequest):
    url = request.url.strip().lower()

    try:
        if "instagram.com" in url:
            download_url = await extract_instagram_video(url)
        elif "tiktok.com" in url:
            download_url = await extract_tiktok_video(url)
        elif "x.com" in url or "twitter.com" in url:
            download_url = await extract_twitter_video(url)
        elif "facebook.com" in url or "fb.watch" in url:
            download_url = await extract_facebook_video(url)
        elif "youtube.com" in url or "youtu.be" in url:
            download_url = await extract_youtube_video(url)
        else:
            return {"error": "❌ رابط غير مدعوم حالياً"}

        return {"download_url": download_url}

    except Exception as e:
        return {"error": str(e)}
