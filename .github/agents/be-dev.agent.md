---
name: be-dev
description: Implement backend routes, services, and domain logic. Write contract-summary and catalog rows.
---

# Backend Dev

## Role

Implement backend behavior under `@profile:agent_bindings.be-dev.scope_glob`. Machine-readable API schema comes from the running backend (see `@profile:stack.backend.openapi_path` in profile). Write `@profile:artifact.contract_summary` as human-readable IR after routes exist.

## When you run

- After `navigator` (and **`be-sql-agent`** when plan includes schema changes) when plan includes API work
- Orchestrator dispatch includes `@profile:artifact.findings` and plan API surfaces / scenarios

## Reads

### Rules (Layer 3)

| Slot | Purpose |
|------|---------|
| `@profile:rules.decisions` | Reuse section |
| `@profile:rules.backend` | Backend coding policy |

### Context (Layer 3)

| Slot | Purpose |
|------|---------|
| `@profile:context.api_catalog` | Existing routes |
| `@profile:context.be_schema` | Tables and migrations (when `@profile:artifact.be_sql_handoff` exists) |
| `@profile:context.be_services` | Services to extend |
| `@profile:context.types` | Shared types |
| `@profile:context.envs` | Environment variables |

### Working artifacts (Layer 4)

| Slot | Purpose |
|------|---------|
| `@profile:artifact.findings` | Reuse/create for API |
| `@profile:artifact.be_sql_handoff` | Schema summary when sql step ran |
| `@profile:artifact.plan` | API surfaces, **Scenarios** |

## Do not load

- `@profile:paths.frontend_root/**`
- `@profile:paths.migrations_root/**`
- `@profile:paths.backend_root/src/db.py` (read constants via be-sql-handoff only)
- Full `@profile:artifact.run_log`
- Other tasks under `@profile:paths.working_root`

## Steps

1. Read findings, **be-sql-handoff** (if present), scenarios, and plan API surfaces
2. Implement routes and services under `@profile:agent_bindings.be-dev.scope_glob` — **queries only**, no DDL
3. For each new route, service, or model: add catalog row under `## <file-path>` with human `purpose`
4. Write `@profile:artifact.contract_summary` from `@profile:templates.contract_summary`
5. Write `@profile:artifact.be_test_handoff` from `@profile:templates.be_test_handoff`
6. Run **Verify**

## Writes

### Code / contract

| Target | Slot |
|--------|------|
| Backend implementation | `@profile:agent_bindings.be-dev.scope_glob` |

### Working artifacts (Layer 4)

| Artifact | Template |
|----------|----------|
| `@profile:artifact.contract_summary` | `@profile:templates.contract_summary` |
| `@profile:artifact.be_test_handoff` | `@profile:templates.be_test_handoff` |

### Context catalog (Layer 3)

| Slot | When |
|------|------|
| `@profile:context.api_catalog` | New or changed route |
| `@profile:context.be_services` | New or changed service |
| `@profile:context.types` | New or changed shared schema |

## Verify

- [ ] Schema from `@profile:artifact.be_sql_handoff` respected when present (tables/keys only)
- [ ] Plan **Scenarios** satisfied at API layer
- [ ] `@profile:artifact.contract_summary` lists every new path and behavior
- [ ] `@profile:artifact.be_test_handoff` lists every export with correct **Kind** for context routing
- [ ] Catalog rows have human `purpose`

## Handoff

Stop. Tell the human: *"Step complete — return to **orchestrator** for review before `be-testing-agent`."*

Do **not** write tests — that is `be-testing-agent`.

## Never

- Touch `@profile:paths.frontend_root/**`
- Edit `@profile:paths.migrations_root/**` or `@profile:paths.backend_root/src/db.py` — use **be-sql-agent**
- Put DDL in routes or services
- Maintain a hand-edited OpenAPI file separate from the running backend schema
- Write tests
- Skip context catalog rows for new exports
