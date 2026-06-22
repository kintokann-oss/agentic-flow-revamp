# Backend SQL handoff — TASK-XXX

> **Required** output from **be-sql-agent** when the task touches persistence — before **be-dev** writes services/routes.  
> Orchestrator runs a human checkpoint, then dispatches **be-dev**.

## Why this file exists

`be-sql-agent` owns DDL and migrations; **be-dev** owns HTTP and domain logic. This file tells be-dev which tables, keys, and columns exist — without be-dev reading every migration file or editing schema.

**Handles:** migrations applied · tables/columns · db.py constants · service query hints.  
**See also:** [ARTIFACTS.md](ARTIFACTS.md#be-sql-handoffmd)

## Files changed

<!-- paths under @profile:paths.migrations_root/ and db.py -->

## New or changed exports

| Symbol | File | Kind |
|--------|------|------|
| | | migration / table / db_module |

## Schema summary

<!-- tables, columns, seeds — human-readable for be-dev -->

| Table | Columns | Seed / default |
|-------|---------|----------------|
| | | |

## Constants for services

<!-- db.py keys importers should use -->

| Constant | Value | Used for |
|----------|-------|----------|
| | | |

## Notes for be-dev

<!-- which tables to query; ON CONFLICT patterns; no DDL in services -->

## Verify (cross-stage)

- [ ] Every export uses a **Kind** value that maps to `context.be_schema` (see `project.profile.yaml` → `context_routing`)
- [ ] Migrations registered in be-schema.md with human `purpose`
- [ ] `@profile:commands.be_test` — `tests/test_db.py` passes after schema change
