from src.db import get_database_path, init_db


def test_get_database_path_default(tmp_path, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    path = get_database_path()
    assert path.name == "app.db"
    assert path.parent.name == "data"


def test_get_database_path_override(tmp_path, monkeypatch):
    db_file = tmp_path / "custom.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_file}")
    assert get_database_path() == db_file


def test_init_db_applies_migrations_without_error(tmp_path, monkeypatch):
    db_file = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_file}")
    init_db()
    assert db_file.exists()
