# API routes (backend)

> **Slot:** `context.api_catalog` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev

## How to use this file

- **Read when:** Planning or implementing HTTP endpoints; checking reuse before adding routes
- **Write when:** be-dev adds or changes a route handler — one row per route
- **Section heading:** `## <repo-relative-path>` to handler module under `@profile:paths.backend_root`
- **Skeleton (shipped)** rows document the minimal sample app; **Example format** rows are templates only

---

## Skeleton (shipped)

## @profile:paths.backend_root/src/routes/health.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /health | get_health |  | HealthResponse | …/tests/test_health.py |

## @profile:paths.backend_root/src/routes/info.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /api/info | get_info |  | *(inline dict)* | …/tests/test_info.py |

---

## Example format (generic — not in this repo)

> Illustrates a feature module. Swap `items` for your domain.

## @profile:paths.backend_root/src/routes/items.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /api/items | list_items |  | ItemListResponse | …/tests/test_items.py |
| POST | /api/items | create_item | ItemBody | ItemResponse | …/tests/test_items.py |
