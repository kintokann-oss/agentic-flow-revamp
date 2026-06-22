# Agent registry

> Master matrix for the multi-agent flow. **Agents are project-agnostic** — paths and stacks live in [`project.profile.yaml`](project.profile.yaml).  
> **Template:** [`.github/agents/agent.template.md`](../.github/agents/agent.template.md) · **Artifacts:** [working/ARTIFACTS.md](working/ARTIFACTS.md)

---

## Layer model

| Layer | Location | Role |
|-------|----------|------|
| 1 | `.github/agents/*.agent.md` | Generic roles — Reads / Steps / Writes via `@profile:` slots |
| 2 | `docs/rules/agent-decisions.md` | Orchestration policy (gates, reuse, routing) |
| 3 | [`docs/project.profile.yaml`](project.profile.yaml) + `docs/rules/*` + `docs/context/*` | **Project factory** — paths, catalogs, coding rules, app architecture |
| 4 | `docs/working/<TASK-ID>/*` | **Task run** — plan, findings, handoffs, state |

---

## Roster

| Agent | Role | Writes code? | Default gate |
|-------|------|--------------|--------------|
| plan-agent | User goal → grill → `plan.md` + glossary + ADRs | No | anchor (approval) |
| orchestrator | Execute steps, state, dispatch | No | — |
| navigator | Reuse/create → `findings.md` | No | anchor |
| fe-design-navigator | Design findings → `findings.md` | No | anchor |
| be-sql-agent | Schema migrations + `be-sql-handoff.md` + be-schema catalog | Yes (schema only) | anchor |
| be-dev | Backend + `contract-summary.md` + `be-test-handoff.md` | Yes (BE) | light |
| be-testing-agent | `@profile:commands.be_test` from handoff / test-gap | Tests only | light |
| fe-dev | UI + `ui-summary.md` + `fe-test-handoff.md` | Yes (FE) | anchor |
| fe-testing-agent | `@profile:commands.fe_test` from handoff / test-gap | Tests only | light |
| be-debugger / fe-debugger | Fix + `test-gap.md` | Minimal patch | anchor |
| flow-end-validator | Context audit + test suites + sign-off | No | anchor |

---

## Reads / writes matrix

Slot names resolve via [`project.profile.yaml`](project.profile.yaml) `agent_bindings`.

| Agent | Reads (summary) | Writes (summary) |
|-------|-----------------|------------------|
| plan-agent | rules.decisions, ubiquitous_language, context.index, prior run_log | plan, ubiquitous_language, ADRs |
| orchestrator | plan, state, run_log, profile | state, run_log |
| navigator | rules.decisions, context.index, plan (acceptance) | findings |
| fe-design-navigator | rules.theming, rules.i18n, fe_design_system, fe_i18n, findings, plan (UI) | findings (Design section) |
| be-sql-agent | rules.sql, rules.backend, be_schema, envs, findings, plan (persistence) | migrations, db.py, be_sql_handoff, be_schema catalog |
| be-dev | rules.*, api_catalog, be_schema, be_services, types, envs, findings, be_sql_handoff, plan (API) | backend code, contract_summary, be_test_handoff, context rows |
| be-testing-agent | rules.testing, test_writing, be_tests, api_catalog, be_test_handoff, test_gap | backend tests, be_tests catalog |
| fe-dev | rules.*, fe_* catalogs, findings, contract_summary | frontend code, ui_summary, fe_test_handoff, context rows |
| fe-testing-agent | rules.testing, rules.i18n, test_writing, fe_tests, fe_i18n, fe_test_handoff, test_gap | frontend tests, fe_tests catalog |
| be-debugger | rules.testing, test_writing, be_tests, api_catalog, findings | backend patch, test_gap |
| fe-debugger | rules.testing, test_writing, fe_* catalogs, findings | frontend patch, test_gap |
| flow-end-validator | context.index, plan, state, run_log, handoffs | context_audit, state (done), run_log (final) |

---

## Default full-stack step order

1. navigator  
2. **be-sql-agent** (when persistence/schema changes) → be-dev → be-testing-agent  
3. fe-design-navigator  
4. fe-dev → fe-testing-agent  
5. flow-end-validator (context audit + tests + sign-off)

Bug-fix: navigator → debugger → testing agent → flow-end-validator.

---

## Slot syntax

In agent files and dispatch packs:

- `@profile:context.api_catalog` → `docs/context/api-list.md` (this project)
- `@profile:paths.backend_root` → `apps/api` (this project)
- `@profile:artifact.findings` → `docs/working/<TASK-ID>/findings.md`

Orchestrator expands slots from profile when dispatching.
