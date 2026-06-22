# Backend schema (SQLite)

> **Slot:** `context.be_schema` · **Rules:** [rules-sql.md](../rules/rules-sql.md) · **Writers:** be-sql-agent

## How to use this file

- **Read when:** Planning persistence changes before writing services
- **Write when:** be-sql-agent adds or changes a migration, table, or connection module export
- **Skeleton (shipped)** documents the empty migration placeholder; **Example format** shows future tables

---

## Skeleton (shipped)

## @profile:paths.migrations_root/001_initial.sql

| file | purpose | tables |
|------|---------|--------|
| 001_initial.sql | Placeholder — no feature tables until first task migration | *(none)* |

## @profile:paths.backend_root/src/db.py

| name | kind | purpose |
|------|------|---------|
| get_database_path | function | Resolve DB file from DATABASE_URL or default |
| get_connection | function | Open connection with row_factory |
| init_db | function | Apply sorted migrations from migrations/ |

---

## Example format (generic — not in this repo)

## Table: items *(example)*

| column | type | constraints | purpose |
|--------|------|-------------|---------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Surrogate key |
| label | TEXT | NOT NULL | Display name |
| created_at | TEXT | NOT NULL | ISO-8601 timestamp |
