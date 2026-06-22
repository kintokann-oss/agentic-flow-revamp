# i18n rules

**Scope:** frontend copy · **Stack:** `@profile:stack.frontend` · **Locales:** `@profile:paths.i18n_locales`

| Path | Role |
|------|------|
| `@profile:paths.frontend_root/src/i18n/` | Init, resources, default namespace |
| `@profile:paths.i18n_locales` | Locale JSON files (source + stubs) |

Wire i18n init in the app entry before render (path from profile).

## Rules

- **No user-facing string literals** in UI source — use the project's i18n API + `t('key')`
- Applies to: labels, titles, `aria-label`, `placeholder`, error messages, button text
- New copy: add keys to locale files; register row in [`fe-i18n.md`](../context/fe-i18n.md)
- Key shape: `namespace.section.key` (e.g. `app.actions.save`)

## Components

```tsx
const { t } = useTranslation('app');
<button>{t('actions.save')}</button>
```

## Tests

- Prefer `i18n.t('namespace:key')` for expected text, or render with test i18n instance
- Avoid hardcoded locale strings in assertions when a key exists

## Agents

- `fe-dev` — read `fe-i18n.md` before adding UI copy
- `fe-testing-agent` — align test expectations with locale keys
