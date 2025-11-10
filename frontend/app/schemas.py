### ✅ schemas.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    name: Optional[str]
    code_key: Optional[str]

class CodeKey(BaseModel):
    code: str
    agency_name: Optional[str]

class Video(BaseModel):
    cctv_id: int
    file_path: str
    detected_type: str
    start_time: str
    end_time: str

class Alert(BaseModel):
    cctv_id: int
    detected_type: str
    detected_date: str
    start_time: str