import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.db"

def get_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Create tables."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employeer_name TEXT NOT NULL UNIQUE,
                employeer_surname TEXT NOT NULL UNIQUE,
                employeer_department TEXT NOT NULL,
                employeer_location TEXT NOT NULL,
                employeer_paygrade TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_email TEXT NOT NULL UNIQUE,
                user_pass TEXT NOT NULL
            )
        """)
        conn.commit()

