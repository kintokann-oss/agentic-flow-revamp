# Frontend services

> **Slot:** `context.fe_services` · **Rules:** [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev

## How to use this file

- One section per module under `@profile:paths.frontend_root/src/api/`
- **Skeleton (shipped)** documents info client; **Example format** shows CRUD client pattern

---

## Skeleton (shipped)

## @profile:paths.frontend_root/src/api/info.ts

| name | purpose | tests | api_calls |
|------|---------|-------|-----------|
| fetchInfo | GET /api/info client | …/info.test.ts | GET /api/info |

---

## Example format (generic — not in this repo)

## @profile:paths.frontend_root/src/api/items.ts

| name | purpose | tests | api_calls |
|------|---------|-------|-----------|
| fetchItems | GET /api/items | …/items.test.ts | GET /api/items |
| createItem | POST /api/items | …/items.test.ts | POST /api/items |
