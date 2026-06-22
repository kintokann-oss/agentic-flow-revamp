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

## apps/api/src/services/saved_time.py

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| get_saved_time | Read saved ISO time from SQLite | apps/api/tests/test_saved_time.py |  |
| set_saved_time | Persist saved ISO time to SQLite | apps/api/tests/test_saved_time.py |  |
