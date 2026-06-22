# Frontend utils & hooks

> **Slot:** `context.fe_utils` · **Rules:** [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev

## How to use this file

- **Read when:** Checking existing hooks or helpers before adding state/data logic
- **Write when:** fe-dev exports a hook (`use*`) or shared util function
- **Section heading:** `## apps/web-react/src/hooks/<name>.ts`
- **Columns:**

| Column | Meaning |
|--------|---------|
| name | Exported hook or function name |
| purpose | Human-readable behavior (required for audit) |
| tests | Colocated test file path |
| depends_on | API clients or other symbols used |

- **Add a row:** 1. Implement hook 2. Add section + row 3. List in fe-test-handoff with kind `hook`

---

## apps/web-react/src/hooks/useToggleState.ts

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| useToggleState | Load/persist boolean toggle via API | apps/web-react/src/hooks/useToggleState.test.ts | fetchToggleState, saveToggleState |

---

## Example format (generic — not in this repo)

> Illustrates a hook that wraps an API client. Not implemented in this repo.

## @profile:paths.frontend_root/src/hooks/useItemList.ts

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| useItemList | Load and refresh item list via API | …/useItemList.test.ts | fetchItems, createItem |
