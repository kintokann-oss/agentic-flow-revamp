# API routes (backend)

> **Slot:** `context.api_catalog` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev

## How to use this file

- **Read when:** Planning or implementing HTTP endpoints; checking reuse before adding routes
- **Write when:** be-dev adds or changes a route handler — one row per route
- **Section heading:** `## apps/api/src/routes/<feature>.py` (repo-relative path to handler module)
- **Columns:**

| Column | Meaning |
|--------|---------|
| method | HTTP verb (GET, PUT, POST, DELETE) |
| path | URL path (e.g. `/api/toggle-state`) |
| handler | Python function name |
| request_type | Pydantic body model or empty for no body |
| response_type | Pydantic response model |
| tests | Colocated test file path |

- **Add a row:** 1. Implement route in source 2. Add `## <file-path>` section if missing 3. Add table row 4. List export in be-test-handoff with kind `route`

---

## apps/api/src/routes/health.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /health | get_health |  | HealthResponse | apps/api/tests/test_health.py |

## apps/api/src/routes/info.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /api/info | get_info |  | InfoResponse | apps/api/tests/test_info.py |

## apps/api/src/routes/toggle_state.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /api/toggle-state | read_toggle_state |  | ToggleStateResponse | apps/api/tests/test_toggle_state.py |
| PUT | /api/toggle-state | update_toggle_state | ToggleStateBody | ToggleStateResponse | apps/api/tests/test_toggle_state.py |

## apps/api/src/routes/saved_time.py

| method | path | handler | request_type | response_type | tests |
|--------|------|---------|--------------|---------------|-------|
| GET | /api/saved-time | read_saved_time |  | SavedTimeResponse | apps/api/tests/test_saved_time.py |
| PUT | /api/saved-time | update_saved_time | SavedTimeBody | SavedTimeResponse | apps/api/tests/test_saved_time.py |
