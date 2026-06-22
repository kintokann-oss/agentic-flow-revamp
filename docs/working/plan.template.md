# Plan — TASK-001

> Written by **plan-agent (grill-with-docs)** from user goal + [`agent-decisions.md`](../rules/agent-decisions.md).  
> **Glossary:** [`UBIQUITOUS_LANGUAGE.md`](../context/UBIQUITOUS_LANGUAGE.md) · **Profile:** [`project.profile.yaml`](../project.profile.yaml)  
> **User must review this entire file** and reply **proceed** or **revise** before orchestrator runs step 1.

## Why this file exists

Single document for **aligned language** (grill), **why** (decisions), and **what** (agent steps). Orchestrator executes the **Steps** table after user approval.

**See also:** [ARTIFACTS.md](ARTIFACTS.md#planmd) · [stage-contract.template.md](stage-contract.template.md)

---

## User goal (verbatim)

> <!-- Paste exactly what the user said -->

## What we found

<!-- Recon: catalog hits, glossary terms reused, gaps — 2–5 bullets -->

## Grill log

<!-- Questions you asked + user answers, branch by branch. "None — goal was unambiguous" if skipped. -->

| # | Topic | Question | Answer |
|---|-------|----------|--------|
| 1 | | | |

## Glossary delta

<!-- Terms added or sharpened in UBIQUITOUS_LANGUAGE.md this task. "None" if unchanged. -->

| Term | Change | Definition (short) |
|------|--------|-------------------|
| | new \| updated | |

## Scenarios

<!-- Given / when / then — drives acceptance checkboxes -->

| ID | Given | When | Then |
|----|-------|------|------|
| S1 | | | |

## ADRs

<!-- Links to docs/decisions/ADR-*.md or "None" -->

| ADR | Title | Why needed |
|-----|-------|------------|
| | | |

## AI decisions

> Derived from `agent-decisions.md`, glossary, and catalog scan — not from user stack/test/reuse choices.

| Decision | Value | Basis |
|----------|-------|-------|
| Stack | | profile defaults |
| In scope | | goal + scenarios |
| Out of scope | | agent-decisions defaults |
| API surfaces | | goal + api-list / glossary |
| UI surfaces | | goal + design-system / glossary |
| Data / env | | defaults or envs.md |
| Reuse strategy | | catalogs + navigator |
| Test strategy | | handoff + rules-testing |

## Proposed tech & scope (user reviews)

> User reviews proposals below — reply **revise** with changes before **proceed**.

| Topic | Proposal | User notes |
|-------|----------|------------|
| Persistence | | |
| New API endpoints | | paths + methods |
| New UI components | | names + tier (base/extending) |
| Other | | |

## User plan review

| Field | Value |
|-------|-------|
| **Status** | `pending` \| `approved` \| `revision_requested` |
| **Reviewed at** | |
| **User notes** | |

Orchestrator sets **approved** after user replies **proceed**. Do not start step 1 while **pending** or **revision_requested**.

---

## Acceptance

- [ ] <!-- map to Scenario S1, S2, … -->

## Steps

| # | agent | task | context_files | scope | done_when | gate_tier | verify_against |
|---|-------|------|---------------|-------|-----------|-----------|----------------|
| 1 | navigator | Scan catalogs; write reuse/create findings | context.index, context.ubiquitous_language | read-only | findings.md written | anchor | plan acceptance |
| 2 | be-sql-agent | Migrations + schema handoff (when persistence changes) | context.be_schema, context.envs | `@profile:paths.migrations_root/**`, db.py | be-sql-handoff.md; be-schema rows | anchor | findings.md, scenarios, persistence proposal |
| 3 | be-dev | Routes + contract-summary + handoff + catalog rows | context.api_catalog, context.be_services | `@profile:paths.backend_root/**` (no migrations/db.py) | contract-summary.md; be-test-handoff.md | light | findings.md, be-sql-handoff.md, scenarios |
| 4 | be-testing-agent | Tests from be-test-handoff | context.be_tests, context.test_writing | `@profile:paths.backend_tests/**` | `@profile:commands.be_test` pass | light | be-test-handoff.md |
| 5 | fe-design-navigator | Design findings | context.fe_design_system, context.fe_i18n | read-only | Design findings in findings.md | anchor | findings.md |
| 6 | fe-dev | UI per scenarios + glossary terms | context.fe_components, context.fe_i18n | `@profile:paths.frontend_root/**` | ui-summary; fe-test-handoff | anchor | findings, contract-summary, scenarios |
| 7 | fe-testing-agent | Tests from fe-test-handoff | context.fe_tests, context.test_writing | `@profile:paths.frontend_root/**` | `@profile:commands.fe_test` pass | light | fe-test-handoff.md |
| 8 | flow-end-validator | Context audit + tests + sign off | context.index | read-only | audit pass; tests pass | anchor | acceptance |

> **Omit step 2** when persistence is unchanged. Omit other rows per goal (BE-only, FE-only, bug-fix).

## Stage contracts (abbreviated)

> Full shape: [stage-contract.template.md](stage-contract.template.md).

### Step 1 — navigator

- **Inputs L3:** `@profile:context.index`, `@profile:context.ubiquitous_language` · **L4:** plan (acceptance, scenarios, glossary delta)
- **Outputs:** `@profile:artifact.findings`
- **Verify:** reuse/create covers acceptance; terms match glossary

### Step 2 — be-sql-agent (when persistence changes)

- **Inputs L3:** `@profile:context.be_schema`, `@profile:context.envs`, `@profile:rules.sql` · **L4:** findings, scenarios, persistence proposal
- **Outputs:** migrations, db.py, `@profile:artifact.be_sql_handoff`, be-schema catalog rows
- **Verify:** scenarios satisfied at schema layer; handoff **Kind** values correct

### Step 3 — be-dev

- **Inputs L3:** api_catalog, be_schema, be_services, types, envs · **L4:** findings, be-sql-handoff (if step 2 ran), scenarios, plan API surfaces
- **Outputs:** backend routes/services, contract-summary, be-test-handoff, catalog rows
- **Verify:** scenarios S* satisfied at API layer; no DDL; handoff **Kind** values correct for context audit

### Step 8 — flow-end-validator

- **Command:** `@profile:commands.context_audit` · **Verify:** exit 0; acceptance met

## Bug-fix variant (fix / bug / broken)

| # | agent | task | context_files | scope | done_when | gate_tier | verify_against |
|---|-------|------|---------------|-------|-----------|-----------|----------------|
| 1 | navigator | findings | context.index | read-only | findings.md | anchor | plan acceptance |
| 2 | fe-debugger or be-debugger | test-gap + minimal fix | context.*_tests | profile scope | test-gap.md; fix applied | anchor | findings, scenarios |
| 3 | fe-testing-agent or be-testing-agent | regression from test-gap | context.test_writing | profile scope | test-gap tests pass | light | test-gap.md |
| 4 | flow-end-validator | audit + sign off | context.index | read-only | audit pass; tests pass | anchor | acceptance |

## Notes

<!-- skipped steps, grill shortcuts -->
