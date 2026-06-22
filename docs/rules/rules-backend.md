# Backend rules (FastAPI)

**Scope:** `@profile:paths.backend_root/**` · **Catalogs:** [api-list.md](../context/api-list.md), [be-services.md](../context/be-services.md), [types.md](../context/types.md)

## File layout

| Path (under backend root) | Role |
|---------------------------|------|
| `src/routes/` | One module per feature — HTTP handlers only |
| `src/services/` | Domain functions — no FastAPI imports |
| `src/db.py` | Connection helpers — **schema owned by be-sql-agent** ([rules-sql.md](rules-sql.md)) |
| `migrations/` | Sorted SQL migrations applied by `init_db()` |
| `tests/` | Integration tests via TestClient (see [rules-testing.md](rules-testing.md)) |

## Route handlers

- One router file per feature (e.g. `toggle_state.py`, `saved_time.py`)
- **Thin handler:** parse request → call service → return response model
- Register routes with `@router.get` / `@router.put` etc.; mount router in app entry
- Document every route in [api-list.md](../context/api-list.md)

## Pydantic models

- Request/response models colocated in the route module (this PoC) or extracted when shared
- Register shared models in [types.md](../context/types.md) with `kind: pydantic_model`
- Use explicit field types; avoid untyped `dict` in public APIs

## Services

- Pure functions in `src/services/` — accept primitives / models, return domain data
- **No HTTP types** inside services (no `Request`, `HTTPException`, status codes)
- Register every exported function in [be-services.md](../context/be-services.md) with human `purpose`

## Persistence

- SQLite via `DATABASE_URL` — schema/migrations: **[rules-sql.md](rules-sql.md)** + [be-schema.md](../context/be-schema.md)
- **be-sql-agent** owns DDL; **be-dev** writes parameterized queries in services only

## Errors

- Raise `HTTPException` with stable status codes (400 validation, 404 not found, 500 unexpected)
- Document error behavior in `contract-summary.md` and route tests
- Do not leak stack traces or internal paths in responses

## OpenAPI

- Generated at `/openapi.json` when the app runs — **no hand-edited contract package**
- After implementing routes, write `contract-summary.md` for human-readable IR
- fe-dev reads contract-summary + live OpenAPI for API client paths

## Catalog duty (after every export)

| Export kind | Catalog file |
|-------------|--------------|
| Route handler | [api-list.md](../context/api-list.md) |
| Service function | [be-services.md](../context/be-services.md) |
| Shared Pydantic model | [types.md](../context/types.md) |

Section heading must match the source file path exactly (repo-relative). Every row needs a human-written `purpose`.

## Testing

- **be-dev does not write tests** — write [be-test-handoff.md](../working/be-test-handoff.template.md) instead
- **be-testing-agent** implements tests from handoff; see [rules-testing.md](rules-testing.md) and [test-writing.md](../context/test-writing.md)
