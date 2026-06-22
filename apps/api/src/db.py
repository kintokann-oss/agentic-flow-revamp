import os
import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "app.db"
MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"
TOGGLE_KEY = "toggle"


def get_database_path() -> Path:
    override = os.environ.get("DATABASE_URL")
    if override:
        if override.startswith("sqlite:///"):
            return Path(override.removeprefix("sqlite:///"))
        return Path(override)
    return DEFAULT_DB_PATH


def get_connection() -> sqlite3.Connection:
    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
            conn.executescript(migration.read_text(encoding="utf-8"))
        conn.commit()
