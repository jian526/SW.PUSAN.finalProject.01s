import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",         # 또는 RDS 주소
        user="root",
        password="12345",
        db="argos_app",           # DB 이름
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
