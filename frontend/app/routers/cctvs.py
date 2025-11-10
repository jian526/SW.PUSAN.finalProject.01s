from fastapi import APIRouter, Form
from app.database import get_connection
import pymysql.cursors  
from fastapi.responses import FileResponse

router = APIRouter(prefix="/cctvs", tags=["CCTV"])


@router.get("/cctv_edit")
def serve_edit_page():
    return FileResponse("frontend/cctv_edit.html")

# ✅ CCTV 추가
@router.post("/add")
def add_cctv(
    name: str = Form(...),
    model: str = Form(...),
    location: str = Form(...),
    rtsp_url: str = Form(...),
    store_id: int = Form(...)
):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO cctvs (name, model, location, rtsp_url, store_id) VALUES (%s, %s, %s, %s, %s)",
            (name, model, location, rtsp_url, store_id)
        )
        conn.commit()
    conn.close()
    return {"success": True}

    return {"success": True}


@router.get("/add")
def serve_edit_page():
    return FileResponse("frontend/cctv_add.html")


# ✅ CCTV 삭제
@router.post("/delete")
def delete_cctv(cctv_id: int = Form(...)):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM cctvs WHERE id = %s", (cctv_id,))
        conn.commit()
    conn.close()
    return {"success": True}

# ✅ CCTV 목록 JSON 반환
@router.get("/api/list")
def get_cctv_list():
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor: 
        cursor.execute("SELECT * FROM cctvs ORDER BY id ASC")
        cctvs = cursor.fetchall()
    conn.close()
    return cctvs  

@router.post("/set_main/{cctv_id}")
def set_main_cctv(cctv_id: int):
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        # 1. 선택된 CCTV의 store_id 가져오기
        cursor.execute("SELECT store_id FROM cctvs WHERE id = %s", (cctv_id,))
        result = cursor.fetchone()
        if not result:
            conn.close()
            return {"success": False, "message": "해당 CCTV를 찾을 수 없습니다."}

        store_id = result["store_id"]

        # 2. 해당 store의 모든 CCTV is_main = FALSE
        cursor.execute("UPDATE cctvs SET is_main = FALSE WHERE store_id = %s", (store_id,))

        # 3. 선택한 CCTV만 is_main = TRUE
        cursor.execute("UPDATE cctvs SET is_main = TRUE WHERE id = %s", (cctv_id,))
        conn.commit()

    conn.close()
    return {"success": True, "message": "메인 카메라가 설정되었습니다."}

