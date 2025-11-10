from fastapi import APIRouter, Form
from app.database import get_connection
import datetime

router = APIRouter(prefix="/calls", tags=["Calls"])

@router.post("/request")
def request_call(store_id: int = Form(...), reason: str = Form(...)):
    now = datetime.datetime.now()
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO calls (store_id, call_time, reason) VALUES (%s, %s, %s)", (store_id, now, reason))
        conn.commit()
    conn.close()
    return {"success": True}
