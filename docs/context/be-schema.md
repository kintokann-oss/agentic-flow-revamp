# Backend schema (SQLite)

> **Slot:** `context.be_schema` · **Rules:** [rules-sql.md](../rules/rules-sql.md) · **Writers:** be-sql-agent

## How to use this file

- **Read when:** Planning persistence changes; be-dev needs to know tables, keys, and columns before writing services
- **Write when:** be-sql-agent adds or changes a migration, table, seed row, or `db.py` schema helper
- **Section heading:** `## <repo-relative-path>` — migration file, `## Table: <name>`, or `## apps/api/src/db.py`
- **Columns (migrations):**

| Column | Meaning |
|--------|---------|
| file | Migration filename |
| purpose | Human-readable change summary (required for audit) |
| tables | Tables created or altered |

- **Columns (tables):**

| Column | Meaning |
|--------|---------|
| column | Column name |
| type | SQLite type |
| constraints | PRIMARY KEY, CHECK, NOT NULL, etc. |
| purpose | Human-readable role |

- **Add a row:** 1. Add migration SQL 2. Update `init_db()` if runner logic changes 3. Add catalog rows 4. List exports in be-sql-handoff
- **Example format** sections show generic table/migration shape — not live schema until be-sql-agent implements them

---

## apps/api/migrations/001_initial.sql

| file | purpose | tables |
|------|---------|--------|
| 001_initial.sql | Initial app_state toggle storage | app_state |

## Table: app_state

| column | type | constraints | purpose |
|--------|------|-------------|---------|
| key | TEXT | PRIMARY KEY | State key (e.g. toggle) |
| value | INTEGER | NOT NULL, CHECK (0 or 1) | Boolean stored as 0/1 |

## apps/api/src/db.py

| name | kind | purpose |
|------|------|---------|
| get_database_path | function | Resolve SQLite file from DATABASE_URL or default |
| get_connection | function | Open connection with row_factory |
| init_db | function | Apply sorted migrations from migrations/ |
| TOGGLE_KEY | constant | Key for boolean toggle row in app_state |

---

## Example format (generic — not in this repo)

> Illustrates a second table for a new migration. Not applied in this repo.

## Table: items *(example)*

| column | type | constraints | purpose |
|--------|------|-------------|---------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Surrogate key |
| label | TEXT | NOT NULL | Display name |
| created_at | TEXT | NOT NULL | ISO-8601 timestamp |
