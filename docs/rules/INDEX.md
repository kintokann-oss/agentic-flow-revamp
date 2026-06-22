# Rules index

**Project paths and agent bindings:** [`docs/project.profile.yaml`](../project.profile.yaml)

## Rules vs context

| Layer | Location | Purpose | Updated by |
|-------|----------|---------|------------|
| **Rules** | `docs/rules/*.md` | How to write code — conventions, placement, anti-patterns | Humans |
| **Context** | `docs/context/*.md` | What exists — durable inventory of exports, routes, keys, tests | Dev/testing agents after implementation |

Rules tell agents **how** to build; context catalogs record **what** was built. At task end, `flow-end-validator` runs [`validate_context_catalog.py`](../../scripts/validate_context_catalog.py) to confirm handoff exports appear in the correct catalog with human `purpose` text.

---

| File | Slot | Applies to (profile scope) | Read by agents | Written by agents |
|------|------|----------------------------|----------------|-------------------|
| [agent-decisions.md](agent-decisions.md) | `rules.decisions` | All agents | plan-agent, orchestrator, all specialists | humans |
| [rules-frontend.md](rules-frontend.md) | `rules.frontend` | `@profile:paths.frontend_root/**` | fe-dev | humans |
| [rules-backend.md](rules-backend.md) | `rules.backend` | `@profile:paths.backend_root/**` | be-dev | humans |
| [rules-sql.md](rules-sql.md) | `rules.sql` | `@profile:paths.migrations_root/**`, db.py | be-sql-agent | humans |
| [rules-testing.md](rules-testing.md) | `rules.testing` | All tests | be/fe-testing-agent, debuggers | humans |
| [rules-theming.md](rules-theming.md) | `rules.theming` | Frontend CSS | fe-design-navigator, fe-dev | humans |
| [rules-i18n.md](rules-i18n.md) | `rules.i18n` | Frontend copy | fe-design-navigator, fe-dev, fe-testing-agent | humans |
