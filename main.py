from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from scraper import extract_instagram_video

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Snap Saver API (Pyppeteer) is running"}

@app.get("/download")
async def download_instagram_video(url: str = Query(...)):
    try:
        video_url = await extract_instagram_video(url)
        return {"success": True, "video_url": video_url}
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})
