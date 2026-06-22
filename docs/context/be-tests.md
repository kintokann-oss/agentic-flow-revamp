# Backend tests

> **Slot:** `context.be_tests` · **Rules:** [rules-testing.md](../rules/rules-testing.md) · **Writers:** be-testing-agent

---

## Skeleton (shipped)

## @profile:paths.backend_tests/test_health.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| get_health | …/src/routes/health.py | unit |

## @profile:paths.backend_tests/test_info.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| get_info | …/src/routes/info.py | unit |

## @profile:paths.backend_tests/test_db.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| init_db | …/src/db.py | unit |

---

## Example format (generic — not in this repo)

## @profile:paths.backend_tests/test_items.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| list_items | …/src/routes/items.py | unit |
| create_item | …/src/routes/items.py | unit |
