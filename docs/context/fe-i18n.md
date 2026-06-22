# Frontend i18n (react-i18next)

> **Slot:** `context.fe_i18n` · **Rules:** [rules-i18n.md](../rules/rules-i18n.md) · **Writers:** fe-dev

## How to use this file

- **Read when:** Adding or changing user-facing copy; fe-design-navigator planning i18n keys
- **Write when:** fe-dev adds a key to locale JSON — register row here with `purpose`
- **Table columns:**

| Column | Meaning |
|--------|---------|
| namespace | i18n namespace (e.g. `app`, `common`) |
| key | Key within namespace (nested keys use dot in handoff: `app.toggle.on`) |
| purpose | Human-readable label role (required for audit) |
| used_in | Component or file that calls `t(t('key'))` |

- **Add a row:** 1. Add string to `en.json` + stub in other locales 2. Add table row 3. List keys in fe-test-handoff **i18n keys added**
- Rows under **Example format** are generic placeholders — not keys in this repo's locale files

Locale files live under `apps/web-react/src/i18n/locales/`.

| namespace | key | purpose | used_in |
|-----------|-----|---------|---------|
| app | preferences.title | Page heading | App.tsx |
| app | status.title | Status panel heading | App.tsx |
| app | errors.serverUnreachable | API info fetch failure | App.tsx |
| app | errors.saveFailed | Toggle persist failure | App.tsx |
| app | toggle.on | BaseButton label when true | App.tsx |
| app | toggle.off | BaseButton label when false | App.tsx |
| app | flow.on | FlowDialog active label | FlowDialog.tsx |
| app | flow.off | FlowDialog idle label | FlowDialog.tsx |
| common | toggle.true | BaseButton default true label | BaseButton.tsx |
| common | toggle.false | BaseButton default false label | BaseButton.tsx |

**Adding a key:** update `en.json` + stub in `el.json` → add row here with `purpose`.

## Locale files

| File | Role |
|------|------|
| `apps/web-react/src/i18n/locales/en.json` | Source |
| `apps/web-react/src/i18n/locales/el.json` | Greek stub |

## Namespace layout (`en.json`)

```json
{
  "app": { "preferences": { "title": "..." }, "toggle": { "on": "...", "off": "..." } },
  "common": { "toggle": { "true": "...", "false": "..." } }
}
```

---

## Example format (generic — not in this repo)

> Illustrates a second namespace and nested keys. Use your feature name instead of `items`.

| namespace | key | purpose | used_in |
|-----------|-----|---------|---------|
| items | list.empty | Empty list placeholder | ItemList.tsx |
| items | actions.save | Primary save button label | DetailPanel.tsx |
