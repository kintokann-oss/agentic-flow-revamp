# Shared types

> **Slot:** `context.types` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev, fe-dev (shared DTOs)

## How to use this file

- **Read when:** Checking request/response shapes before implementing handlers or clients
- **Write when:** A shared model or TypeScript type is exported and reused
- **Skeleton (shipped):** info route returns inline dict — no pydantic rows yet

---

## Example format (generic — not in this repo)

## @profile:paths.backend_root/src/routes/items.py

| name | kind | used_by |
|------|------|---------|
| ItemBody | pydantic_model | create_item |
| ItemResponse | pydantic_model | create_item, list_items |
| ItemListResponse | pydantic_model | list_items |
