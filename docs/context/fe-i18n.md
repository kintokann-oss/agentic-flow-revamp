# Frontend i18n (react-i18next)

> **Slot:** `context.fe_i18n` · **Rules:** [rules-i18n.md](../rules/rules-i18n.md) · **Writers:** fe-dev

## How to use this file

- **Write when:** fe-dev adds a key to locale JSON — register row here with `purpose`
- **Skeleton (shipped)** lists keys in the minimal App; **Example format** shows feature namespaces

Locale files: `@profile:paths.i18n_locales`

---

## Skeleton (shipped)

| namespace | key | purpose | used_in |
|-----------|-----|---------|---------|
| app | title | Page heading | App.tsx |
| app | errors.serverUnreachable | API info fetch failure | App.tsx |

---

## Example format (generic — not in this repo)

| namespace | key | purpose | used_in |
|-----------|-----|---------|---------|
| items | list.empty | Empty list placeholder | ItemList.tsx |
| items | actions.save | Primary save button label | DetailPanel.tsx |

## Namespace layout *(example)*

```json
{
  "app": { "title": "..." },
  "items": { "list": { "empty": "..." }, "actions": { "save": "..." } }
}
```
