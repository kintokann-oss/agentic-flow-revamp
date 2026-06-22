# Frontend components

> **Slot:** `context.fe_components` · **Rules:** [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev

## How to use this file

- **Section heading:** `## <repo-relative-path>` under `@profile:paths.frontend_root`
- **Skeleton (shipped)** documents minimal App; **Example format** shows component rows for future features

---

## Skeleton (shipped)

## @profile:paths.frontend_root/src/App.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| App | Root shell; loads backend info on mount | …/App.test.tsx | fetchInfo |

---

## Example format (generic — not in this repo)

## @profile:paths.frontend_root/src/components/DetailPanel/DetailPanel.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| DetailPanel | Nested panel inside a base surface | …/DetailPanel.test.tsx | useItemList |

## @profile:paths.frontend_root/src/components/ItemList/ItemList.tsx

| name | purpose | tests | depends_on |
|------|---------|-------|------------|
| ItemList | Renders a list of items from API | …/ItemList.test.tsx | useItemList |
