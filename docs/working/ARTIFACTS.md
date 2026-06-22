# Task artifacts — why each file exists

> Every file under `docs/working/<TASK-ID>/` is a **handoff between agents or between agents and you**.  
> Agents do not message each other in chat — they read and write these files.

**Quick index:** [working/INDEX.md](INDEX.md) · Templates in this folder · Registry: [AGENT-REGISTRY.md](../AGENT-REGISTRY.md) · Profile: [project.profile.yaml](../project.profile.yaml)

---

## Overview — the problem they solve

Without these files, a multi-agent run would lose:

- **What you asked for** vs **what the AI decided** (scope, stack, out-of-scope)
- **Which step we are on** and whether you approved the last step
- **What already exists** in the repo vs what must be created
- **What to test** after dev agents finish (separate BE/FE lanes)
- **What tests were missing** when a bug slipped through

Each artifact has one primary job. `state.yaml` and `run-log.md` serve different audiences (machine vs human).

---

## `plan.md`

| | |
|---|---|
| **Written by** | `plan-agent` |
| **Read by** | **You (must approve before step 1)**, `orchestrator` (every step) |
| **Template** | [plan.template.md](plan.template.md) |
| **Immutable for** | `orchestrator` — wrong plan → back to `plan-agent` |

### Why it exists

**Single planning document.** Records why we are doing the task **and** the agent runbook. You review the **whole file** — goal, AI decisions, **proposed tech & scope**, steps — before orchestrator runs step 1.

### What it handles

- **User goal (verbatim)** — what you said
- **What we found** — recon from catalogs + glossary
- **Grill log** — plan-agent interview (grill-with-docs): questions + answers per branch
- **Glossary delta** — terms added/sharpened in `UBIQUITOUS_LANGUAGE.md`
- **Scenarios** — given / when / then (drives acceptance)
- **ADRs** — links to non-obvious decisions in `docs/decisions/`
- **AI decisions** — scope, stack, reuse, tests (AI-only)
- **Proposed tech & scope** — persistence, endpoints, components — **you review and revise**
- **User plan review** — `pending` \| `approved` \| `revision_requested`
- **Acceptance** — maps to scenarios
- **Steps** — agent table with **`gate_tier`**, **`verify_against`**, stage contracts

### User review (required)

Plan-agent sets **User plan review → `pending`**. Orchestrator must not start step 1 until you reply **proceed** and status is **`approved`**.

---

## `state.yaml`

| | |
|---|---|
| **Written by** | `orchestrator` (ongoing), `flow-end-validator` (final `phase: done`) |
| **Read by** | `orchestrator` only (you do not edit unless debugging) |
| **Template** | [state.template.yaml](state.template.yaml) |

### Why it exists

`run-log.md` is for humans. The orchestrator needs **structured state** to resume after interruptions: current step, per-step status, human gate approval, blockers, timestamps.

### What it handles

- **`phase`** — `planning` \| `executing` \| `awaiting_human` \| `done` \| `blocked`
- **`current_step`** — which plan row is active
- **`steps[]`** — per agent: `status`, `gate_tier`, `inputs`, `outputs`, `stale`, `gate_status`
- **`fast_mode`** — optional; enables `gate_tier: auto` steps
- **`human_gate` / `awaiting_human`** — tiered pauses (anchor / light / auto)
- **`blocker`** — why the task is stuck

### Reason it exists

Multi-step work spans many chat sessions. `state.yaml` is the **save game** so the orchestrator never asks *"which step were we on?"*

---

## `run-log.md`

| | |
|---|---|
| **Written by** | `orchestrator` (each step), `flow-end-validator` (final row) |
| **Read by** | You, `plan-agent` (previous task's log when planning the next TASK) |
| **Template** | [run-log.template.md](run-log.template.md) |

### Why it exists

Same events as `state.yaml`, but in a **table you can read in a PR or demo** without parsing YAML.

### What it handles

- Per step: **agent**, **gate**, **status**, files, **outcome**, **user revision**, **source fix suggested**
- **Revision patterns** — edit-source loop (same feedback 3× → suggest rule/context update)
- Optional **summary** — task name, started/completed dates
- Audit trail for demos and post-task review

### Reason it exists alongside `state.yaml`

| `state.yaml` | `run-log.md` |
|--------------|--------------|
| Machine-readable | Human-readable |
| Orchestrator logic | Demos, reviews, history |
| Gate flags, phases | "What files did be-dev touch?" |

---

## `findings.md`

| | |
|---|---|
| **Written by** | `navigator` (reuse/create), `fe-design-navigator` (appends **Design findings**) |
| **Read by** | You (checkpoints), `fe-dev` (Design findings required), orchestrator |
| **Template** | [findings.template.md](findings.template.md) |

### Why it exists

Before writing code, agents must know **what to reuse vs create**. Context catalogs hold symbols; findings translate that into **task-specific actions** for this TASK only.

### What it handles

**From navigator (step 1):**

- Catalog search results
- **Reuse** — extend existing files/symbols
- **Create** — new paths and purpose (BE, FE, contract)

**From fe-design-navigator (UI tasks, before fe-dev):**

- **Design findings** — theme tokens, i18n keys, base/extending components to reuse
- **Gaps** — new tokens, keys, or components `fe-dev` must create

### Reason it exists

`plan.md` says *"add settings panel"*. Findings say *"reuse existing list component; add one new API route"*. Design findings add *"reuse theme tokens and i18n keys from catalog; extend registered base component"*.

**Overlap with navigator:** navigator lists FE paths at file level; design-navigator goes deeper on **how** UI must be built (theme/i18n/tiers). Same file, different sections.

---

## `be-sql-handoff.md`

| | |
|---|---|
| **Written by** | `be-sql-agent` (when persistence/schema changes) |
| **Read by** | You (checkpoint), `be-dev` |
| **Template** | [be-sql-handoff.template.md](be-sql-handoff.template.md) |

### Why it exists

**be-sql-agent** owns migrations and `db.py`; **be-dev** owns routes/services. This handoff tells be-dev which tables, columns, and constants exist — without be-dev editing DDL.

### What it handles

- Migration files under `@profile:paths.migrations_root/`
- Schema summary (tables, columns, seeds)
- `db.py` constants for service imports
- Notes for query patterns (parameterized SQL only)

### Reason it exists

Mirrors the split between design findings (UI structure) and fe-dev (implementation): schema layer is isolated so API changes do not entangle with migration files.

---

## `be-test-handoff.md`

| | |
|---|---|
| **Written by** | `be-dev` (required after BE implementation) |
| **Read by** | You (checkpoint), `be-testing-agent` |
| **Template** | [be-test-handoff.template.md](be-test-handoff.template.md) |

### Why it exists

`be-dev` must **not** write tests. Something must tell `be-testing-agent` **what behaviors matter** for the exports that just landed — without the testing agent re-reading all of `@profile:paths.backend_root/`.

### What it handles

- Files changed under `@profile:paths.backend_root/`
- New/changed **exports** (routes, services, models)
- **Testable behaviors** — status codes, JSON shape, persistence, errors
- Suggested test paths under `@profile:paths.backend_tests/`
- Notes — fixtures, temp DB, env vars

### Reason it is separate from `fe-test-handoff.md`

Backend and frontend are **different lanes**: separate test commands, agents, and templates. One shared handoff file caused overwrite confusion — split keeps BE and FE test scope explicit.

---

## `fe-test-handoff.md`

| | |
|---|---|
| **Written by** | `fe-dev` (required after FE implementation) |
| **Read by** | You (checkpoint), `fe-testing-agent` |
| **Template** | [fe-test-handoff.template.md](fe-test-handoff.template.md) |

### Why it exists

Same pattern as BE handoff: `fe-dev` implements UI; `fe-testing-agent` owns tests. Handoff lists **observable UI behaviors**, new **i18n keys**, and mock requirements.

### What it handles

- Files changed under `@profile:paths.frontend_root/`
- Components, hooks, API clients
- Testable behaviors — render, click, hook state, mocked fetch
- **i18n keys added** — so tests use `i18n.t()`, not hardcoded strings
- Suggested colocated test paths

### Reason it exists

Frontend tests need **i18n and mock context** that BE handoff does not cover. FE lane stays self-contained for `@profile:commands.fe_test`.

---

## `contract-summary.md`

| | |
|---|---|
| **Written by** | `be-dev` |
| **Read by** | You (anchor checkpoint), `fe-dev`, `be-testing-agent`, orchestrator |
| **Template** | [contract-summary.template.md](contract-summary.template.md) |

Human-readable **intermediate representation** of OpenAPI changes — paths, breaking changes, notes for implementation. Checkpoint-friendly one-pager (ICM-style IR).

---

## `ui-summary.md`

| | |
|---|---|
| **Written by** | `fe-dev` |
| **Read by** | You (anchor checkpoint), orchestrator |
| **Template** | [ui-summary.template.md](ui-summary.template.md) |

One-page summary of UI work: components touched, i18n keys, theme tokens, demo steps. Complements `fe-test-handoff.md` for review, not for test authoring.

---

## Gate tiers & staleness

| Concept | Where | Meaning |
|---------|-------|---------|
| **gate_tier** | `plan.md`, `state.yaml` | `anchor` = full review · `light` = quick · `auto` = only if `fast_mode` |
| **verify_against** | `plan.md` step row | Upstream artifact this step must match |
| **stale** | `state.yaml` step | Input file changed — re-run required |
| **Stage contract** | `plan.md` + [stage-contract.template.md](stage-contract.template.md) | Inputs / Verify / Outputs per step |

See [agent-decisions.md § Gate tiers](../rules/agent-decisions.md#gate-tiers).

---

## `test-gap.md`

| | |
|---|---|
| **Written by** | `be-debugger` or `fe-debugger` (bug-fix tasks only) |
| **Read by** | You, `be-testing-agent` or `fe-testing-agent`, `orchestrator` (never skip testing step) |
| **Template** | [test-gap.template.md](test-gap.template.md) |

### Why it exists

When a bug ships, the process failed twice: **the code** and **the tests**. `test-gap.md` forces the debugger to document **why existing tests did not catch it** and **exactly which regression tests to add**.

### What it handles

- Bug summary and reproduction
- **Why tests missed it** — missing scenario, weak assertion, over-mock, wrong layer, no test yet
- **Tests to add** — file, test name, assertion (mandatory list)
- **Fix scope** — minimal change; what was intentionally not refactored

### Reason it exists

`test-gap.md` documents **why existing tests failed** and **exactly which regression tests to add**. Test-gap overrides handoff-only policy — testing agent must implement **every row**, even if a test file already exists.

**Not used on feature tasks** — use `be-test-handoff.md` / `fe-test-handoff.md` instead.

---

## Flow — when each file appears

Default full-stack order (omit steps per plan):

1. **plan-agent** → `plan.md` → you **proceed**
2. **orchestrator** → `state.yaml`, `run-log.md`
3. **navigator** → `findings.md`
4. **be-sql-agent** → `be-sql-handoff.md` (schema changes only)
5. **be-dev** → `contract-summary.md`, `be-test-handoff.md`
6. **be-testing-agent** → tests + `be-tests` catalog
7. **fe-design-navigator** → Design section in `findings.md`
8. **fe-dev** → `ui-summary.md`, `fe-test-handoff.md`
9. **fe-testing-agent** → tests + `fe-tests` catalog
10. **flow-end-validator** → `context-audit.md`, final state

Bug-fix: navigator → debugger → `test-gap.md` → testing agent → flow-end-validator.

---

## Who reads what (summary)

| File | Writer | Primary readers |
|------|--------|-----------------|
| `plan.md` | plan-agent | you, orchestrator |
| `state.yaml` | orchestrator, flow-end-validator | orchestrator |
| `run-log.md` | orchestrator, flow-end-validator | you, plan-agent |
| `findings.md` | navigator, fe-design-navigator | you, fe-dev, be-sql-agent, orchestrator |
| `be-sql-handoff.md` | be-sql-agent | you, be-dev, orchestrator |
| `contract-summary.md` | be-dev | you, fe-dev, be-testing-agent |
| `be-test-handoff.md` | be-dev | you, be-testing-agent |
| `ui-summary.md` | fe-dev | you, orchestrator |
| `fe-test-handoff.md` | fe-dev | you, fe-testing-agent |
| `test-gap.md` | be/fe-debugger | you, be/fe-testing-agent |
| `context-audit.md` | flow-end-validator | you | Catalog audit report |

Specialists usually receive **scope and task from orchestrator** (copied from `plan.md`), not by opening `plan.md` themselves.

---

## `context-audit.md`

| | |
|---|---|
| **Written by** | `flow-end-validator` |
| **Read by** | You (final anchor checkpoint) |
| **Template** | [context-audit.template.md](context-audit.template.md) |

Output of `validate_context_catalog.py` — confirms handoff exports are in the correct context catalog with human `purpose`. Task cannot close while audit exit code is 1.

---

## What is NOT in this folder

| Location | Role |
|----------|------|
| `docs/context/*.md` | Long-lived catalog — maintained by dev/testing agents; audited by flow-end-validator |
| `docs/project.profile.yaml` | Project paths, stacks, agent bindings, context routing |
| `@profile:paths.backend_root/**`, `@profile:paths.frontend_root/**` | Application source — changed by dev agents |

Task artifacts are **ephemeral per TASK**; context MDs are **durable across tasks**.
