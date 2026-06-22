# Shared types

> **Slot:** `context.types` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev, fe-dev (shared DTOs)

## How to use this file

- **Read when:** Checking request/response shapes or shared interfaces before implementing handlers or clients
- **Write when:** A Pydantic model or shared TypeScript type is exported and reused across modules
- **Section heading:** `## <path/to/source/file>` — usually the module where the type is defined
- **Columns:**

| Column | Meaning |
|--------|---------|
| name | Type or model name |
| kind | `pydantic_model`, `interface`, `type`, `class`, `enum` |
| used_by | Handlers, services, or components that consume this type |

- **Add a row:** 1. Define type in source 2. Add section + row 3. List in be-test-handoff with kind `pydantic_model` (BE) or reference from fe-dev handoff (FE)

<!-- kind values: interface | type | class | enum | pydantic_model -->

---

## apps/api/src/routes/toggle_state.py

| name | kind | used_by |
|------|------|---------|
| ToggleStateBody | pydantic_model | update_toggle_state |
| ToggleStateResponse | pydantic_model | read_toggle_state, update_toggle_state |

## apps/api/src/routes/saved_time.py

| name | kind | used_by |
|------|------|---------|
| SavedTimeBody | pydantic_model | update_saved_time |
| SavedTimeResponse | pydantic_model | read_saved_time, update_saved_time |
