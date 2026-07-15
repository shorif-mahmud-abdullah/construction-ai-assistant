import os

import psycopg2
from dotenv import load_dotenv

from app.tools.memory.models import Note

load_dotenv()


class NoteRepository:

    def _get_connection(self):
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

    def save(self, content: str) -> Note:
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (note) VALUES (%s) RETURNING id, created_at",
            (content,),
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Note(id=row[0], content=content, created_at=row[1])

    def list_all(self) -> list[Note]:
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, note, created_at FROM notes ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Note(id=r[0], content=r[1], created_at=r[2]) for r in rows]
