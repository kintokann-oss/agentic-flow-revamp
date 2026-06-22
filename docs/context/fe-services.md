# Frontend services

> **Slot:** `context.fe_services` · **Rules:** [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev

## How to use this file

- **Read when:** Checking existing API clients before adding fetch wrappers
- **Write when:** fe-dev exports a new or changed function in `src/api/`
- **Section heading:** `## apps/web-react/src/api/<name>.ts`
- **Columns:**

| Column | Meaning |
|--------|---------|
| name | Exported client function name |
| purpose | Human-readable API behavior (required for audit) |
| tests | Colocated test file path |
| api_calls | HTTP method + path or function self-reference |

- **Add a row:** 1. Implement client (paths match contract-summary / OpenAPI) 2. Add section + row 3. List in fe-test-handoff with kind `api client`

---

## apps/web-react/src/api/info.ts

| name | purpose | tests | api_calls |
|------|---------|-------|-----------|
| fetchInfo | GET /api/info client | apps/web-react/src/api/info.test.ts | GET /api/info |

## apps/web-react/src/api/toggleState.ts

| name | purpose | tests | api_calls |
|------|---------|-------|-----------|
| fetchToggleState | GET /api/toggle-state | apps/web-react/src/api/toggleState.test.ts | GET /api/toggle-state |
| saveToggleState | PUT /api/toggle-state | apps/web-react/src/api/toggleState.test.ts | PUT /api/toggle-state |

---

## Example format (generic — not in this repo)

> Illustrates a second API client module. Not implemented in this repo.

## @profile:paths.frontend_root/src/api/items.ts

| name | purpose | tests | api_calls |
|------|---------|-------|-----------|
| fetchItems | GET /api/items | …/items.test.ts | GET /api/items |
| createItem | POST /api/items | …/items.test.ts | POST /api/items |
