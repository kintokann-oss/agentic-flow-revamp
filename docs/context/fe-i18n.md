# Frontend i18n (react-i18next)

> **Slot:** `context.fe_i18n` · **Rules:** [rules-i18n.md](../rules/rules-i18n.md) · **Writers:** fe-dev

## How to use this file

- **Read when:** Adding or changing user-facing copy; fe-design-navigator planning i18n keys
- **Write when:** fe-dev adds a key to locale JSON — register row here with human `purpose`
- **Table columns:**

| Column | Meaning |
|--------|---------|
| namespace | i18n namespace (e.g. `app`, `time`, `common`) |
| key | Key within namespace (nested keys use dot in handoff: `app.toggle.on`) |
| purpose | Human-readable label role (required for audit) |
| used_in | Component or file that calls `t(t('key'))` |

- **Add a row:** 1. Add string to `en.json` + stub in other locales 2. Add table row 3. List keys in fe-test-handoff **i18n keys added**

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
| time | now | Live clock label | TimeDialog.tsx |
| time | saved | Saved time label | TimeDialog.tsx |
| time | empty | No saved time placeholder | TimeDialog.tsx |
| time | loading | Loading saved time | TimeDialog.tsx |
| time | saveButton | Save current time button | TimeDialog.tsx |
| time | saveError | Save failure message | TimeDialog.tsx |
| time | ariaLabel | Time panel aria-label | TimeDialog.tsx |
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
  "time": { "now": "...", "saveButton": "..." },
  "common": { "toggle": { "true": "...", "false": "..." } }
}
```
