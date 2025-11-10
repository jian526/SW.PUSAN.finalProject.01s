from fastapi import APIRouter, Query
from app.database import get_connection
from fastapi.responses import FileResponse

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.get("/video")
def serve_edit_page():
    return FileResponse("frontend/video.html")
