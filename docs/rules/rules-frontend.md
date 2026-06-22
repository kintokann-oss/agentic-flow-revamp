# Frontend rules (React)

**Scope:** `@profile:paths.frontend_root/**` · **Catalogs:** [fe-components.md](../context/fe-components.md), [fe-utils.md](../context/fe-utils.md), [fe-services.md](../context/fe-services.md), [fe-design-system.md](../context/fe-design-system.md)

## File layout

| Path (under frontend root) | Role |
|----------------------------|------|
| `src/components/` | UI components — one folder per component |
| `src/hooks/` | Custom hooks — `use*` naming |
| `src/api/` | Thin fetch wrappers for backend endpoints |
| `src/styles/` | Global CSS + `theme.css` (tokens only file with raw colors) |
| `src/i18n/` | react-i18next setup and locale JSON files |
| `src/App.tsx` | Root page shell |

## Components

- One folder per component: `ComponentName/ComponentName.tsx` + colocated `ComponentName.css`
- Export a named function component; props type as `ComponentNameProps`
- Register every exported component in [fe-components.md](../context/fe-components.md)

## Base vs extending components

- **Base components** — `Base<Name>/` folders; listed in fe-design-system **base** table
- **Extending components** — specialized UI on a base; **must** set `extends_base` in fe-design-system
- **No extending component without a base** — create/register the base first
- UI tasks: run **`fe-design-navigator`** before **`fe-dev`** (plan step or design findings pass)
- Read order: theme tokens → i18n keys → base components → extending → page shell

## Hooks

- Name `use*`; place in `src/hooks/`
- Encapsulate data loading, API calls, and local UI state
- Register in [fe-utils.md](../context/fe-utils.md) with human `purpose`

## API clients

- Thin `fetch` wrappers in `src/api/` — one module per backend resource
- Paths must match [contract-summary.md](../working/contract-summary.template.md) / live OpenAPI
- Register in [fe-services.md](../context/fe-services.md) with `api_calls` column

## State

- Prefer custom hooks over global stores in this PoC
- Server state flows: hook → API client → backend; document in fe-utils + fe-services catalogs

## Styling

- **`var(--token-name)` only** outside `theme.css` — see [rules-theming.md](rules-theming.md)
- Component CSS files use semantic tokens, never `#`, `rgb()`, or `hsl()` literals

## Copy (i18n)

- **No user-facing string literals** in JSX/TSX — see [rules-i18n.md](rules-i18n.md)
- Use `useTranslation('namespace')` + `t('key')`; register keys in [fe-i18n.md](../context/fe-i18n.md)

## Catalog duty (after every export)

| Export kind | Catalog file |
|-------------|--------------|
| Component | [fe-components.md](../context/fe-components.md) |
| Hook / util | [fe-utils.md](../context/fe-utils.md) |
| API client | [fe-services.md](../context/fe-services.md) |
| Base / extending UI | [fe-design-system.md](../context/fe-design-system.md) |
| i18n key | [fe-i18n.md](../context/fe-i18n.md) |

Section heading must match the source file path exactly (repo-relative).

## Testing

- **fe-dev does not write tests** — write [fe-test-handoff.md](../working/fe-test-handoff.template.md) instead
- **fe-testing-agent** implements tests from handoff; see [rules-testing.md](rules-testing.md) and [test-writing.md](../context/test-writing.md)
