# Frontend test handoff — TASK-XXX

> **Required** output from **fe-dev** before the FE testing step.  
> Orchestrator runs a human checkpoint, then dispatches **fe-testing-agent**.

## Why this file exists

`fe-dev` builds UI but **must not write frontend tests** (`@profile:commands.fe_test`). This file tells `fe-testing-agent` what to test — including **i18n keys** and **fetch mocks** that BE handoff does not cover. Kept separate so FE and BE lanes never overwrite one shared handoff.

**Handles:** components/hooks/clients · UI behaviors · i18n keys · colocated test paths.  
**See also:** [ARTIFACTS.md](ARTIFACTS.md#fe-test-handoffmd)

## Files changed

<!-- paths under @profile:paths.frontend_root/ -->

## New or changed exports

| Symbol | File | Kind |
|--------|------|------|
| | | component / hook / api client |

## Testable behaviors

<!-- render, click, hook state, mocked fetch — not implementation details -->

-
-

## i18n keys added

| namespace.key | purpose |
|---------------|---------|
| | |

## Suggested test files

| Export | Test file (colocated) |
|--------|------------------------|
| | |

## Notes for fe-testing-agent

<!-- mocks (fetch), userEvent flows, i18n keys to assert with i18n.t() -->

## Verify (cross-stage)

- [ ] Exports match `ui-summary.md`
- [ ] i18n keys match `fe-i18n.md` rows
- [ ] Client paths match `contract-summary.md` (if API tests mocked)
