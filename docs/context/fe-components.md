# Frontend components

> **Slot:** `context.fe_components` · **Rules:** [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev

## How to use this file

- **Read when:** Checking existing UI before adding or extending components
- **Write when:** fe-dev exports a new or changed React component
- **Section heading:** `## apps/web-react/src/components/<Name>/<Name>.tsx` or page path like `App.tsx`
- **Columns:**

| Column | Meaning |
|--------|---------|
| name | Exported component name |
| purpose | Human-readable UI role (required for audit) |
| tests | Colocated test file path |
| depends_on | Hooks, child components, or API clients used |

- **Add a row:** 1. Implement component 2. Add section + row 3. List in fe-test-handoff with kind `component`

---

## apps/web-react/src/App.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| App | Root shell; flow background + FlowDialog + BaseButton | apps/web-react/src/App.test.tsx | BaseButton, FlowDialog, fetchInfo, useToggleState |

## apps/web-react/src/components/FlowDialog/FlowDialog.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| FlowDialog | Status dialog; reflects true/false flow state; nests TimeDialog | apps/web-react/src/components/FlowDialog/FlowDialog.test.tsx |  |

## apps/web-react/src/components/TimeDialog/TimeDialog.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| TimeDialog | Nested time dialog; live clock + save Time button | apps/web-react/src/components/TimeDialog/TimeDialog.test.tsx | useSavedTime |

## apps/web-react/src/components/BaseButton/BaseButton.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| BaseButton | Foundation true/false button — app-wide base control | apps/web-react/src/components/BaseButton/BaseButton.test.tsx |  |
