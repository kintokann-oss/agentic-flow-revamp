# Findings — TASK-XXX

> **navigator** writes reuse/create (step 1). **fe-design-navigator** appends **Design findings** (UI tasks, before fe-dev).  
> See [ARTIFACTS.md](ARTIFACTS.md#findingsmd) · Paths from [`project.profile.yaml`](../project.profile.yaml)

## Why this file exists

Context catalogs know *symbols exist*; findings translate that into *what this task should do* — extend an existing page or create a new component, reuse API or add contract paths. Design findings add *how* UI must respect theme, i18n, and component tiers.

**Handles:** catalog search summary · reuse vs create (all layers) · design reuse/gaps (UI only).  
**Read by:** you, `fe-dev` (Design findings required), orchestrator at checkpoints.

---

## Catalog search (navigator)

| Source | Result |
|--------|--------|
| `@profile:context.api_catalog` | |
| `@profile:context.be_schema` | |
| `@profile:context.fe_components` | |
| Other catalogs from dispatch | |

## Reuse

| Asset | Action |
|-------|--------|
| | **Extend** / **Keep** |

## Create

| Path | Purpose |
|------|---------|
| | |

## Verify (before done)

- [ ] Reuse/create covers plan acceptance items
- [ ] No duplicate paths in Create vs Reuse

---

## Design findings (fe-design-navigator)

### Paths
- theme: `@profile:paths.theme_css`
- i18n: `@profile:paths.i18n_locales`

### Theme tokens (reuse)
-

### i18n keys (reuse)
-

### Base components (reuse)
-

### Extending (reuse)
-

### Gaps
-
