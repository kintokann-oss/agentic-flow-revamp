# Backend services

> **Slot:** `context.be_services` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev

## How to use this file

- **Read when:** Checking existing domain logic before adding services
- **Write when:** be-dev exports a new or changed function from `src/services/`
- **Skeleton (shipped):** no service modules yet — only **Example format** below until be-dev implements features

---

## Example format (generic — not in this repo)

## @profile:paths.backend_root/src/services/items.py

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| list_items | Read all item rows from store | …/tests/test_items.py |  |
| create_item | Insert one item row | …/tests/test_items.py |  |
