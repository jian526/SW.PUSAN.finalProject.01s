### ✅ main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import users, code_keys, videos, alerts, stores, cctvs, calls,auth



app = FastAPI()

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# 라우터 등록
app.include_router(users.router)
app.include_router(code_keys.router)
app.include_router(videos.router)
app.include_router(alerts.router)
app.include_router(stores.router)
app.include_router(cctvs.router)
app.include_router(calls.router)
app.include_router(auth.router)





@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")


@app.get("/cctv/index")
def read_index():
    return FileResponse("frontend/index.html")

@app.get("/alerts")
def serve_edit_page():
    return FileResponse("frontend/alerts.html")

@app.get("/mypage")
def serve_edit_page():
    return FileResponse("frontend/mypage.html")

@app.get("/live")
def serve_edit_page():
    return FileResponse("frontend/live.html")

@app.get("/video_alerts")
def serve_edit_page():
    return FileResponse("frontend/video_alerts.html")

@app.get("/login")
def serve_edit_page():
    return FileResponse("frontend/login.html")

@app.get("/signup")
def serve_edit_page():
    return FileResponse("frontend/signup.html")

@app.get("/code_info")
def serve_edit_page():
    return FileResponse("frontend/code_info.html")

@app.get("/start")
def serve_edit_page():
    return FileResponse("frontend/start.html")