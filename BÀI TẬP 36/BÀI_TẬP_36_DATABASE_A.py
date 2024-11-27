import sqlite3
from datetime import datetime

class AttendanceDB:
    def __init__(self):
        self.conn = sqlite3.connect("C:/Users/Acer/Downloads/THIGIACMAYTINH_THAYTUNG-master/THIGIACMAYTINH_THAYTUNG-master/BÀI TẠP 36/my_database.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT(50) PRIMARY KEY,
                name TEXT(250),
                class_id TEXT(25)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                class_id TEXT,
                date TEXT,
                time TEXT,
                confidence REAL,
                FOREIGN KEY (student_id) REFERENCES students (student_id)
            )
        """)
        self.conn.commit()

a = AttendanceDB()
