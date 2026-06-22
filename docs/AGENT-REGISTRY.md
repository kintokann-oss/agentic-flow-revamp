# Agent registry

> Master matrix for the multi-agent flow. **Agents (Layer 1) are project-agnostic** — they reference only `@profile:` slots. Paths, stacks, and catalogs live in [`project.profile.yaml`](project.profile.yaml) and `docs/rules/` / `docs/context/`.  
> **Template:** [`.github/agents/agent.template.md`](../.github/agents/agent.template.md) · **Artifacts:** [working/ARTIFACTS.md](working/ARTIFACTS.md)

---

## Layer model

| Layer | Location | Role |
|-------|----------|------|
| 1 | `.github/agents/*.agent.md` | Generic roles — Reads / Steps / Writes via `@profile:` slots only |
| 2 | `docs/rules/agent-decisions.md` | Orchestration policy (gates, reuse, routing) |
| 3 | [`docs/project.profile.yaml`](project.profile.yaml) + `docs/rules/*` + `docs/context/*` | **Project factory** — paths, catalogs, coding rules, app architecture |
| 4 | `docs/working/<TASK-ID>/*` | **Task run** — plan, findings, handoffs, state |

**Portability rule:** Copy Layer 1–2 unchanged to another repo. Change only Layer 3 (profile + rules + context) and Layer 4 per task.

---

## Separation of concerns

Each agent has **one primary job**. Overlap is resolved by dispatch order and forbidden scopes in `agent_bindings`.

| Agent | Owns | Does not own |
|-------|------|--------------|
| **plan-agent** | Grill, glossary, ADRs, `plan.md` | Code, catalogs (except glossary), orchestration |
| **orchestrator** | Dispatch, `state.yaml`, `run-log.md`, gates | Code, plan edits, catalog rows |
| **navigator** | Reuse/create in `findings.md` | Code, catalog writes, design findings |
| **fe-design-navigator** | Design findings in `findings.md` | Code, catalog writes, API work |
| **be-sql-agent** | Migrations, connection module, schema catalog, `be-sql-handoff.md` | Routes, services, route tests |
| **be-dev** | Routes, services, `contract-summary.md`, `be-test-handoff.md`, BE catalog rows | DDL, migrations, tests, frontend |
| **be-testing-agent** | Backend tests, `be-tests` catalog | Feature code |
| **fe-dev** | UI, clients, hooks, `ui-summary.md`, `fe-test-handoff.md`, FE catalog rows | Tests, backend |
| **fe-testing-agent** | Frontend tests, `fe-tests` catalog | Feature code |
| **be-debugger** / **fe-debugger** | Minimal fix, `test-gap.md` | Refactors, tests (testing agent writes them) |
| **flow-end-validator** | Context audit, test commands, sign-off | Code, catalog fixes |

**Single-writer rules:**

- **DDL** → be-sql-agent only  
- **HTTP handlers + domain services** → be-dev only (queries, no DDL)  
- **Colocated tests** → testing agents only (from handoff or test-gap)  
- **Catalog rows for exports** → dev agents that created the export  
- **Catalog audit** → flow-end-validator only (read-only check)

---

## Roster

| Agent | Role (one line) | Writes code? | Default gate |
|-------|-----------------|--------------|--------------|
| plan-agent | User goal → grill → `plan.md` + glossary + ADRs | No | anchor |
| orchestrator | Execute steps, state, dispatch | No | — |
| navigator | Reuse/create → `findings.md` | No | anchor |
| fe-design-navigator | Design findings → `findings.md` | No | anchor |
| be-sql-agent | Schema + migrations + schema handoff | Yes (schema only) | anchor |
| be-dev | Backend + contract summary + BE handoff | Yes (BE) | light |
| be-testing-agent | BE tests from handoff / test-gap | Tests only | light |
| fe-dev | UI + UI summary + FE handoff | Yes (FE) | anchor |
| fe-testing-agent | FE tests from handoff / test-gap | Tests only | light |
| be-debugger / fe-debugger | Fix + `test-gap.md` | Minimal patch | anchor |
| flow-end-validator | Context audit + test suites + sign-off | No | anchor |

---

## Reads / writes matrix

Slot names resolve via [`project.profile.yaml`](project.profile.yaml) `agent_bindings`.

| Agent | Reads (summary) | Writes (summary) |
|-------|-----------------|------------------|
| plan-agent | rules.decisions, rules.architecture, ubiquitous_language, context.index, prior run_log | plan, ubiquitous_language, ADRs |
| orchestrator | rules.decisions, plan, state, run_log, profile | state, run_log |
| navigator | rules.decisions, rules.architecture, context.index, ubiquitous_language, plan (acceptance) | findings |
| fe-design-navigator | rules.theming, rules.i18n, fe_design_system, fe_i18n, findings, plan (UI) | findings (Design section) |
| be-sql-agent | rules.sql, rules.backend, be_schema, envs, findings, plan (persistence) | migrations, db module, be_sql_handoff, be_schema catalog |
| be-dev | rules.backend, api_catalog, be_schema, be_services, types, envs, findings, be_sql_handoff, plan (API) | backend code, contract_summary, be_test_handoff, context rows |
| be-testing-agent | rules.testing, test_writing, be_tests, api_catalog, be_test_handoff, test_gap | backend tests, be_tests catalog |
| fe-dev | rules.frontend, theming, i18n, fe_* catalogs, findings, contract_summary | frontend code, ui_summary, fe_test_handoff, context rows |
| fe-testing-agent | rules.testing, rules.i18n, test_writing, fe_tests, fe_i18n, fe_test_handoff, test_gap | frontend tests, fe_tests catalog |
| be-debugger | rules.testing, test_writing, be_tests, api_catalog, findings | backend patch, test_gap |
| fe-debugger | rules.testing, test_writing, fe_* catalogs, findings | frontend patch, test_gap |
| flow-end-validator | context.index, plan, state, run_log, handoffs | context_audit, state (done), run_log (final) |

---

## Default full-stack step order

1. navigator  
2. **be-sql-agent** (when plan persistence/schema changes) → be-dev → be-testing-agent  
3. fe-design-navigator (UI tasks)  
4. fe-dev → fe-testing-agent  
5. flow-end-validator (context audit + tests + sign-off)

Bug-fix: navigator → debugger → testing agent → flow-end-validator.

Skip rules (orchestrator): see `@profile:rules.decisions` — e.g. omit be-sql-agent when persistence unchanged; fast-complete testing when handoff has no new exports.

---

## Slot syntax

In agent files and dispatch packs:

- `@profile:context.api_catalog` → resolved from profile `context_slots` (this repo: `docs/context/api-list.md`)
- `@profile:paths.backend_root` → resolved from profile `paths` (this repo: `apps/api`)
- `@profile:artifact.findings` → `docs/working/<TASK-ID>/findings.md`

Orchestrator expands `{paths.*}` and slot names from profile when dispatching. **Agent markdown never embeds resolved paths.**

---

## Agent file contract

Every `.github/agents/*.agent.md` must follow [agent.template.md](../.github/agents/agent.template.md):

| Section | Purpose |
|---------|---------|
| Role + **Boundary** | One job; what to refuse |
| When you run | Triggers from plan/orchestrator |
| Reads | `@profile:` slots only |
| Do not load | Scope limits |
| Steps | Ordered procedure |
| Writes | Code scope + artifacts + catalog slots |
| Verify | Checklist before stop |
| Handoff | Return to orchestrator |
| Never | Hard prohibitions |
