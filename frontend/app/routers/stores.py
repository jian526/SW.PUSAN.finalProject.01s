from fastapi import APIRouter
from app.database import get_connection

router = APIRouter(prefix="/stores", tags=["Stores"])

@router.get("/")
def list_stores():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM stores")
        stores = cursor.fetchall()
    conn.close()
    return stores

