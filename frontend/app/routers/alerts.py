from fastapi import APIRouter
from app.database import get_connection
import pymysql

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.get("/list")
def get_today_alerts():
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""
            SELECT event_type AS alert_type, 
                   CONCAT(detected_date, ' ', start_time) AS detected_at
            FROM alerts
            WHERE detected_date = CURDATE()
            ORDER BY detected_date DESC, start_time DESC
        """)
        alerts = cursor.fetchall()
    conn.close()
    return alerts