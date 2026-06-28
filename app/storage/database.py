import sqlite3
from pathlib import Path

from app.config import config


class Database:
    def __init__(self):
        db_path = Path(config.get("sqlite_path"))

        # Create the parent directory if it doesn't exist
        db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(db_path)

        # Return rows like dictionaries instead of tuples
        self.connection.row_factory = sqlite3.Row

    def execute(self, query: str, params: tuple = ()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def executemany(self, query: str, params: list[tuple]):
        cursor = self.connection.cursor()
        cursor.executemany(query, params)
        self.connection.commit()
        return cursor

    def close(self):
        self.connection.close()