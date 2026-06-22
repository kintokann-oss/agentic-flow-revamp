# Backend services

> **Slot:** `context.be_services` · **Rules:** [rules-backend.md](../rules/rules-backend.md) · **Writers:** be-dev

## How to use this file

- **Read when:** Checking existing domain logic before adding services or refactoring routes
- **Write when:** be-dev exports a new or changed function from `src/services/`
- **Section heading:** `## apps/api/src/services/<name>.py`
- **Columns:**

| Column | Meaning |
|--------|---------|
| name | Exported function name |
| purpose | Human-readable behavior (required for audit) |
| tests | Test file that covers this function |
| depends_on | Other symbols or services this function uses |

- **Add a row:** 1. Implement service function 2. Add section + row 3. List in be-test-handoff with kind `service`

---

## apps/api/src/services/toggle_state.py

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| get_toggle_state | Read boolean toggle from SQLite | apps/api/tests/test_toggle_state.py |  |
| set_toggle_state | Persist boolean toggle to SQLite | apps/api/tests/test_toggle_state.py |  |

---

## Example format (generic — not in this repo)

> Illustrates a second service module. Not implemented in this repo.

## @profile:paths.backend_root/src/services/items.py

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| list_items | Read all item rows from store | …/tests/test_items.py |  |
| create_item | Insert one item row | …/tests/test_items.py |  |
