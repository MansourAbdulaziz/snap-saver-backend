from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from scraper import extract_instagram_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download")
def download_instagram_video(url: str = Query(...)):
    try:
        video_url = extract_instagram_video(url)
        return {"success": True, "video_url": video_url}
    except Exception as e:
        return {"success": False, "error": str(e)}    
