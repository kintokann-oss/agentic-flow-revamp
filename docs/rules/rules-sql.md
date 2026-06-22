# SQL / persistence rules (SQLite)

**Scope:** `@profile:paths.migrations_root/**`, `@profile:paths.backend_root/src/db.py` · **Catalog:** [be-schema.md](../context/be-schema.md)

## Stack (this project)

| Piece | Location |
|-------|----------|
| Engine | SQLite via stdlib `sqlite3` |
| Connection helper | `@profile:paths.backend_root/src/db.py` — `get_connection()`, `get_database_path()`, `init_db()` |
| Migrations | `@profile:paths.migrations_root/*.sql` — applied in sorted filename order by `init_db()` |
| Env override | `DATABASE_URL` — see [envs.md](../context/envs.md) |

## Ownership

| Agent | Owns |
|-------|------|
| **be-sql-agent** | DDL migrations, `init_db()` wiring, seed rows, schema catalog rows, `be-sql-handoff.md` |
| **be-dev** | Routes and services — **queries only** via `get_connection()`; imports key constants from `db.py` |
| **be-testing-agent** | Tests using temp DB via `DATABASE_URL` fixture — no DDL in tests |

## Migration rules

1. **One file per change** — `NNN_description.sql` (zero-padded prefix, snake_case description)
2. **Idempotent where possible** — prefer `CREATE TABLE IF NOT EXISTS`, `INSERT OR IGNORE`
3. **No DROP in PoC** unless plan explicitly requires destructive migration (document in handoff)
4. **No raw DDL in routes or services** — only in migration files + `init_db()` runner
5. **Register every migration file** in [be-schema.md](../context/be-schema.md) with human `purpose`

## Query rules (be-dev / services)

- Parameterized queries only — `?` placeholders, never f-string SQL
- One table concern per service module when practical
- Document table/column usage in `be-sql-handoff.md` for be-dev
- Shared keys (e.g. state keys) as constants in `db.py` — be-sql-agent adds new constants

## Testing

- Tests set `DATABASE_URL` to a temp file — see [test-writing.md](../context/test-writing.md)
- Schema tests live in `tests/test_db.py` — be-sql-agent updates when migrations change
- be-sql-agent does **not** write route/service tests — hand off to be-dev → be-testing-agent

## Catalog duty

| Export kind | Catalog file | Handoff kind |
|-------------|--------------|--------------|
| Migration file | be-schema.md | `migration` |
| Table / column change | be-schema.md | `table` |
| db.py module symbol | be-schema.md | `db_module` |
