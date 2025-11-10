from fastapi import APIRouter, Form, HTTPException, Response
from app.database import get_connection
from fastapi.responses import RedirectResponse,FileResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(id: str = Form(...), password: str = Form(...)):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (id, password))
        user = cursor.fetchone()
    conn.close()
    if user:
        return {"success": True, "user_name": user["username"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/login")
def serve_edit_page():
    return FileResponse("frontend/login.html")

@router.get("/logout")
def logout(response: Response):
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("user_id")
    response.delete_cookie("user_name")
    return response

@router.post("/signup")
def signup(
    id: str = Form(...),
    password: str = Form(...),
    code_key: str = Form(...),
    store_name: str = Form(...),
    name: str = Form(...),  # 점주명 → 추후 필요시 stores에 저장 가능
    phone: str = Form(...),
):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 1. 코드 키 유효성 검사 및 중복 사용 확인
            cursor.execute("SELECT * FROM code_keys WHERE code = %s AND is_used = FALSE", (code_key,))
            code = cursor.fetchone()
            if not code:
                raise HTTPException(status_code=400, detail="유효하지 않거나 이미 사용된 코드입니다.")

            # 2. 점포 등록
            cursor.execute("INSERT INTO stores (name, address) VALUES (%s, '')", (store_name,))
            store_id = cursor.lastrowid

            # 3. 유저 등록
            cursor.execute("""
                INSERT INTO users (username, password, phone, store_id, code_key)
                VALUES (%s, %s, %s, %s, %s)
            """, (id, password, phone, store_id, code_key))

            # 4. 코드키 사용 처리
            cursor.execute("UPDATE code_keys SET is_used = TRUE, issued_to = %s WHERE code = %s", (id, code_key))

        conn.commit()
        return {"success": True}
    finally:
        conn.close()


