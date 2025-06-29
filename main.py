from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from scraper import extract_instagram_video
from fastapi import Request

app = FastAPI()

@app.post("/api/instagram")
async def post_instagram_video(request: Request):
    try:
        body = await request.json()
        url = body.get("url")
        if not url:
            return JSONResponse(status_code=400, content={"error": "Missing URL"})

        video_url = await extract_instagram_video(url)
        return {"download_url": video_url}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
