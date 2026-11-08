import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "backend.db"

def get_db():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
    finally:
        connection.close()
