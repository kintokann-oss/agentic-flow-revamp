# Backend tests

> **Slot:** `context.be_tests` · **Rules:** [rules-testing.md](../rules/rules-testing.md) · **Writers:** be-testing-agent

## How to use this file

- **Read when:** be-testing-agent or debugger checks existing test coverage
- **Write when:** be-testing-agent adds or extends a test file from handoff or test-gap
- **Section heading:** `## apps/api/tests/test_<feature>.py`
- **Columns:**

| Column | Meaning |
|--------|---------|
| covers_symbol | Function or handler name under test |
| covers_file | Source file path being tested |
| kind | `unit` or `integration` |

- **Add a row:** 1. Write test file 2. Add section + one row per symbol covered 3. List path in be-test-handoff **Suggested test files**

---

## apps/api/tests/test_health.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| get_health | apps/api/src/routes/health.py | unit |

## apps/api/tests/test_info.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| get_info | apps/api/src/routes/info.py | unit |

## apps/api/tests/test_toggle_state.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| read_toggle_state | apps/api/src/routes/toggle_state.py | unit |
| update_toggle_state | apps/api/src/routes/toggle_state.py | unit |
| get_toggle_state | apps/api/src/services/toggle_state.py | unit |
| set_toggle_state | apps/api/src/services/toggle_state.py | unit |

---

## Example format (generic — not in this repo)

> Illustrates coverage rows for a second feature test file. Not implemented in this repo.

## @profile:paths.backend_root/tests/test_items.py

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| list_items | …/src/routes/items.py | unit |
| create_item | …/src/routes/items.py | unit |
| list_items | …/src/services/items.py | unit |
