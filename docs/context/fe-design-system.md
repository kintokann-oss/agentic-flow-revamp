# Frontend design system

> **Slot:** `context.fe_design_system` · **Rules:** [rules-theming.md](../rules/rules-theming.md), [rules-i18n.md](../rules/rules-i18n.md), [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** fe-dev, fe-design-navigator (findings)

## How to use this file

- **Read when:** Before styling or adding UI — theme paths, base vs extending tiers
- **Write when:** Registering a new base or extending component (`purpose` required)
- **Not a symbol-per-row catalog** — path tables + base/extending registries
- Rows below are **generic examples** unless listed under **Skeleton (shipped)**
- **Example format** sections show table shape only — not audited until implemented

---

## Paths (relative to repo root)

| Asset | Path | Notes |
|-------|------|-------|
| Theme tokens | `@profile:paths.theme_css` | **Only file** with raw color literals — [rules-theming.md](../rules/rules-theming.md) |
| Global styles | `@profile:paths.frontend_root/src/styles/index.css` | Resets — `var(--*)` only |
| i18n locales | `@profile:paths.i18n_locales` | See [fe-i18n.md](fe-i18n.md) |
| App shell styles | `@profile:paths.frontend_root/src/App.css` | Page layout — `var(--*)` only |
| Base components | `@profile:paths.frontend_root/src/components/Base*/` | Folders named `Base<Name>/` |
| Extending components | `@profile:paths.frontend_root/src/components/<Name>/` | Must declare `extends_base` below |

**Lookup order:** theme tokens → i18n keys → base components → extending components → page shell.

### Theme token sections (in `theme.css`)

| Section | Examples |
|---------|----------|
| Palette | `--palette-slate-700`, `--palette-emerald-500` |
| Semantic | `--color-text-primary`, `--color-error`, `--color-surface-page` |
| Spacing | `--space-1` … `--space-8` |
| Typography | `--font-family-sans`, `--font-size-md` |
| Elevation | `--radius-md`, `--shadow-panel` |

---

## Skeleton (shipped)

No base or extending component folders in the skeleton yet. fe-dev registers the first base before any extending component.

---

## Base components *(example format)*

| name | path | purpose |
|------|------|---------|
| BaseCard *(example)* | `@profile:paths.frontend_root/src/components/BaseCard/` | Foundation surface primitive for panels and dialogs |

Naming: exported component `Base<Name>` in `components/Base<Name>/Base<Name>.tsx`.

---

## Extending components *(example format)*

| name | path | extends_base | purpose |
|------|------|--------------|---------|
| DetailPanel *(example)* | `@profile:paths.frontend_root/src/components/DetailPanel/` | BaseCard | Nested detail content inside a base surface |

**Rule:** every row **must** have `extends_base` set to an existing **base** component name.

---

## Adding UI (checklist)

1. Colors/spacing → semantic tokens in `theme.css`; component CSS uses `var(--*)` only
2. User-facing text → locales + row in `fe-i18n.md` — no string literals in JSX
3. Check **base components** — reuse or extend before inventing a parallel control
4. New **extending** row → `extends_base` must already appear in the base table
5. Update this file when adding base or extending components (`purpose` column)
