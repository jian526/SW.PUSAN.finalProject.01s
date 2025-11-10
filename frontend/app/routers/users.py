from fastapi import APIRouter, Query
from app.database import get_connection

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def get_my_info(user_name: str = Query(...)):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, username, name, code_key, created_at FROM users WHERE username = %s", (user_name,))
        user = cursor.fetchone()
    conn.close()
    return user
