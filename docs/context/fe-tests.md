# Frontend tests

> **Slot:** `context.fe_tests` · **Rules:** [rules-testing.md](../rules/rules-testing.md) · **Writers:** fe-testing-agent

## How to use this file

- **Read when:** fe-testing-agent or debugger checks existing test coverage
- **Write when:** fe-testing-agent adds or extends a colocated test from handoff or test-gap
- **Section heading:** `## apps/web-react/src/<path>/<Name>.test.tsx` (or `.test.ts`)
- **Columns:**

| Column | Meaning |
|--------|---------|
| covers_symbol | Component, hook, or client name under test |
| covers_file | Source file path being tested |
| kind | `unit` or `integration` |

- **Add a row:** 1. Write colocated test 2. Add section + row 3. List path in fe-test-handoff **Suggested test files**

---

## apps/web-react/src/App.test.tsx

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| App | apps/web-react/src/App.tsx | unit |

## apps/web-react/src/api/info.test.ts

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| fetchInfo | apps/web-react/src/api/info.ts | unit |

## apps/web-react/src/api/savedTime.test.ts

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| fetchSavedTime | apps/web-react/src/api/savedTime.ts | unit |
| saveSavedTime | apps/web-react/src/api/savedTime.ts | unit |

## apps/web-react/src/api/toggleState.test.ts

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| fetchToggleState | apps/web-react/src/api/toggleState.ts | unit |
| saveToggleState | apps/web-react/src/api/toggleState.ts | unit |

## apps/web-react/src/components/BaseButton/BaseButton.test.tsx

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| BaseButton | apps/web-react/src/components/BaseButton/BaseButton.tsx | unit |

## apps/web-react/src/components/FlowDialog/FlowDialog.test.tsx

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| FlowDialog | apps/web-react/src/components/FlowDialog/FlowDialog.tsx | unit |

## apps/web-react/src/components/TimeDialog/TimeDialog.test.tsx

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| TimeDialog | apps/web-react/src/components/TimeDialog/TimeDialog.tsx | unit |

## apps/web-react/src/hooks/useSavedTime.test.ts

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| useSavedTime | apps/web-react/src/hooks/useSavedTime.ts | unit |

## apps/web-react/src/hooks/useToggleState.test.ts

| covers_symbol | covers_file | kind |
|---------------|-------------|------|
| useToggleState | apps/web-react/src/hooks/useToggleState.ts | unit |
