# Theming rules

**Scope:** frontend CSS · **Token file:** `@profile:paths.theme_css`

**Only `@profile:paths.theme_css` may contain** `#`, `rgb()`, `rgba()`, `hsl()`, `hsla()` literals.

Everywhere else (`*.css`, inline `style`, component class rules): use **`var(--token-name)`** only.

## Token layout

Organize `:root` in this order:

1. **Raw palette** — `--palette-neutral-*`, `--palette-primary-*`, `--palette-emerald-*`
2. **Semantic colors** — `--color-bg`, `--color-text`, `--color-error`, component/surface tokens
3. **Spacing** — `--space-1` … `--space-8`
4. **Typography** — `--font-family-sans`, `--font-size-*`, `--line-height-*`
5. **Radius, shadow, z-index** — `--radius-*`, `--shadow-*`, `--z-overlay`, `--z-modal`

## Adding a new color

1. Add palette step in the theme file if needed
2. Add semantic token referencing palette
3. Use semantic token in component CSS — never add a new hex in component files

## Agents

- `fe-dev`, `fe-design-navigator` — read [`fe-design-system.md`](../context/fe-design-system.md) for theme path
- Future CI: lint for hex outside `@profile:paths.theme_css` (not automated here)
