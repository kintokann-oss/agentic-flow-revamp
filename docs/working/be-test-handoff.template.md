# Backend test handoff — TASK-XXX

> **Required** output from **be-dev** before the BE testing step.  
> Orchestrator runs a human checkpoint, then dispatches **be-testing-agent**.

## Why this file exists

`be-dev` implements routes and services but **must not write backend tests** (`@profile:commands.be_test`). This file is the contract to `be-testing-agent`: which exports changed, what behaviors to assert, where tests should live. Separates implementation from test authoring.

**Handles:** BE exports · observable API behaviors · suggested test paths · fixture notes.  
**See also:** [ARTIFACTS.md](ARTIFACTS.md#be-test-handoffmd)

## Files changed

<!-- paths under @profile:paths.backend_root/ -->

## New or changed exports

| Symbol | File | Kind |
|--------|------|------|
| | | route / service / pydantic_model |

## Testable behaviors

<!-- observable outcomes: status codes, JSON shape, DB persistence, errors -->

-
-

## Suggested test files

| Export | Test file |
|--------|-----------|
| | `@profile:paths.backend_tests/test_*.py` |

## Notes for be-testing-agent

<!-- fixtures, temp DB, env vars, edge cases -->

## Verify (cross-stage)

- [ ] Every export uses a **Kind** value that maps to the correct context file (see `project.profile.yaml` → `context_routing`)
- [ ] Suggested test files are colocated under `@profile:paths.backend_tests/`
