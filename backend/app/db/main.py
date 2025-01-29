import sqlite3

from backend.app.db.db import get_connection


def get_user_by_email(email: str):
    """Get user by email from users table"""

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_email = ?", (email,))
            user = cursor.fetchone()
            return user
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
