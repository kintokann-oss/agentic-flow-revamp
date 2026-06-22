# Agent decisions (hard rules — plan-agent does not ask the user)

> **Audience:** plan-agent, orchestrator, and all specialists.  
> **Project paths, stack, and commands:** [`docs/project.profile.yaml`](../project.profile.yaml)  
> **Agent contracts:** [`.github/agents/agent.template.md`](../../.github/agents/agent.template.md) · [`docs/AGENT-REGISTRY.md`](../AGENT-REGISTRY.md)

## Agent separation (Layer 1)

Agents are **project-agnostic**. They reference `@profile:` slots only — never literal paths or stack names. Each agent owns one concern; see **Separation of concerns** in [AGENT-REGISTRY.md](../AGENT-REGISTRY.md).

| Concern | Owner agent |
|---------|-------------|
| Plan + glossary | plan-agent |
| Dispatch + state | orchestrator |
| Reuse/create | navigator |
| Design findings | fe-design-navigator |
| Schema / DDL | be-sql-agent |
| Routes + services | be-dev |
| Backend tests | be-testing-agent |
| UI implementation | fe-dev |
| Frontend tests | fe-testing-agent |
| Bug fix + test-gap | debugger |
| Audit + sign-off | flow-end-validator |

## User input vs spec clarifications

| Layer | Who | What |
|-------|-----|------|
| **Goal** | User | One task in plain language |
| **Grill (grill-with-docs)** | Plan-agent + user | Branch-by-branch alignment on terms, scenarios, edge cases — see [grill-with-docs](https://www.aihero.dev/grill-with-docs) |
| **Hard rules** | AI only | Stack, reuse, tests, acceptance, catalog sync, agent routing |

### Plan-agent as grill-with-docs + spec agent

**Read `@profile:context.ubiquitous_language` first.** Then grill before writing `plan.md`:

1. **Challenge fuzzy language** — map user words to glossary terms or propose new definitions  
2. **Surface term collisions** — one term, one meaning  
3. **Concrete scenarios** — given / when / then for edge cases  
4. **Cross-reference catalogs** — cite existing symbols before proposing new ones  
5. **ADRs** — when a decision is hard to reverse, surprising, or a real trade-off → `docs/decisions/ADR-*.md`  
6. **Update glossary** — add or sharpen terms in `UBIQUITOUS_LANGUAGE.md` before plan checkpoint  

**Ask in batches of 1–3 questions.** Continue until design branches for this goal are resolved or the user says to write the plan.

**Ask:** behavior, UX, data meaning, extend vs replace, cardinality, deletion/empty states.  
**Do not ask:** framework choice, test runner, reuse policy, test policy, agent routing.

Record the session in plan **Grill log**, **Glossary delta**, **Scenarios**, and **ADRs** sections.

---

## Defaults (when goal does not say otherwise)

Use [`docs/project.profile.yaml`](../project.profile.yaml) for stack labels and paths. Policy defaults:

| Topic | Default | Source |
|-------|---------|--------|
| Stack | From profile `stack.*` | `project.profile.yaml` |
| Persistence | From profile `defaults.persistence` | `project.profile.yaml` |
| Auth | From profile `defaults.auth` | `project.profile.yaml` |
| Tests | Per `rules-testing.md` + handoff files | Testing agents |
| i18n / theming | Per rules + context catalogs | `rules-i18n`, `rules-theming`, context MDs |
| Reuse | Always prefer existing catalog rows | Navigator + context |

---

## Design system (UI tasks — not user Q&A)

When the goal touches UI, styling, components, or layout:

1. Run **`fe-design-navigator`** (with or right after `navigator`)
2. Read `@profile:context.fe_design_system` — theme tokens, **base** table, then **extending** table
3. Read `@profile:context.fe_i18n` + `@profile:rules.i18n` for user-facing copy
4. **No magic colors** — `@profile:rules.theming`; **no string literals in JSX** — `@profile:rules.i18n`
5. **No extending component without a registered base** — plan must create base first if missing

---

## Reuse (navigator + context — not user Q&A)

**Always** run `navigator` as plan step 1.

Before creating any file or export:

1. Read `@profile:context.index` and open relevant catalog files
2. Search catalog rows by name, path, and purpose
3. Optionally confirm with a quick source search under profile paths

| Catalog signal | Action |
|----------------|--------|
| Row exists with clear `purpose` | **Extend** — read purpose, do not duplicate |
| Callers depend on public shape | **Preserve** API; use refactor agent if rename needed |
| No row, confirmed absent in source | **Create new** — record in `@profile:artifact.findings` |
| Partial overlap | **Reuse** util/hook/service; add only missing pieces |

Write `@profile:artifact.findings` with: what exists, what to reuse, what to create.

---

## Tests (handoff-driven — not user Q&A)

Policy: every **exported** symbol should have a test file (`rules-testing.md`).

**Who writes tests:** `be-testing-agent` / `fe-testing-agent` — not feature dev agents.

**When to include a testing step in the plan:**

| Situation | Plan step |
|-----------|-----------|
| New exports expected (greenfield feature) | Include testing agent after implementation |
| Handoff lists testable behaviors | Testing agent covers every behavior |
| Handoff says no new exports to test | Step may complete immediately — **light** gate |
| `@profile:artifact.test_gap` exists (bug-fix) | Testing agent implements **every** listed test |

Testing agents read **`be-test-handoff.md` / `fe-test-handoff.md`** or **`test-gap.md`** — not an automated index query.

### Regression from debugger (bug-fix tasks)

When goal is fix / bug / broken:

| Step | Agent | done_when |
|------|-------|-----------|
| 1 | navigator | `@profile:artifact.findings` |
| 2 | fe-debugger or be-debugger | minimal fix + **`test-gap.md`** written |
| 3 | fe-testing-agent or be-testing-agent | all tests from test-gap pass |
| 4 | flow-end-validator | test suites green; acceptance met |

Debugger **must** document why existing tests failed to catch the bug. Testing agent **must not** skip test-gap tests because a test file already exists.

---

## Scope inference from goal

| Goal signals | In scope | Out of scope |
|--------------|----------|--------------|
| "database", "schema", "migration", "table", "persist", "SQLite" | be-sql-agent → be-dev | In-memory mock only if plan says so |
| "API", "endpoint", "route" | BE + contract if new surface | FE unless also mentioned |
| "page", "UI", "component", "screen" | FE | BE unless also mentioned |
| "full", "end-to-end", feature name without layer | FE + BE + contract | Deploy, CI, auth |
| "fix", "bug", "broken" | debugger → testing agent | New features |
| "rename", "extract", "move" | refactor agents (if enabled) | Behavior change |

When both FE and BE are implied, order: **BE schema (if needed) → BE dev → BE tests → FE design nav → FE → FE tests → flow-end-validator**.

---

## Plan-agent output

1. `@profile:artifact.plan` — user goal + **what I found** + spec answers + **AI decisions** + **proposed tech & scope** + **user plan review** + steps + acceptance
2. Do **not** write application code

Every plan must:

1. Start with `navigator`
2. When **Proposed tech & scope → Persistence** changes or new tables/columns are needed: insert **`be-sql-agent`** before **`be-dev`** (writes `be-sql-handoff.md`)
3. **`be-dev` implements routes and services** — machine OpenAPI at `@profile:stack.backend.openapi_path` when the app runs; write `contract-summary.md` after routes exist; **no DDL**
4. Put **implementation before testing agents**
4. End with `flow-end-validator` (context catalog audit + test suites + acceptance)
5. Map each acceptance checkbox to at least one `done_when`
6. Set **`gate_tier`** and **`verify_against`** on every step row (defaults in [Gate tiers](#gate-tiers))

---

## Gate tiers (human checkpoints)

| Tier | When to use | Human review |
|------|-------------|--------------|
| **anchor** | plan approval, navigator, design navigator, **be-sql-agent**, contract, main UI dev, debugger, final validator | Full — read artifacts, proceed / revise |
| **light** | be-dev (contract exists), testing agents (handoff exists), mechanical test runs | Quick — skim diff + test output |
| **auto** | Only with `fast_mode: true` in state and mechanical `done_when` met | Orchestrator may dispatch next without pause; still update run-log |

Default per agent:

| Agent | Default gate_tier |
|-------|-------------------|
| plan-agent (approval) | anchor |
| navigator, fe-design-navigator, **be-sql-agent**, fe-dev, debugger | anchor |
| be-dev, be-testing-agent, fe-testing-agent | light |
| flow-end-validator | anchor (final sign-off always anchor) |

---

## Stage contracts (Inputs / Verify)

Each step has an explicit contract in `@profile:artifact.plan` **Stage contracts** (full template: [stage-contract.template.md](../working/stage-contract.template.md)).

| Section | Meaning |
|---------|---------|
| **Inputs L3** | Stable `docs/context/` + `docs/rules/` (via `@profile:` slots) |
| **Inputs L4** | `docs/working/<TASK>/` artifacts |
| **Do not load** | Other tasks, full run-log, unrelated plan sections |
| **Verify** | Checklist before step is `done` — cross-stage alignment |
| **verify_against** | Upstream artifact(s) listed in plan step row |

Specialists run **Verify** before stopping. Orchestrator spot-checks at checkpoint.

---

## Staleness (incremental re-run)

`state.yaml` each step has `inputs[]`, `outputs[]`, `stale`.

**When an input file changes** after step N is `done`:

1. Set step N `status: stale` (or `pending` if re-run needed)
2. Set all steps **after** N whose `inputs` include that file to `stale: true`, `status: pending`
3. Post message: which steps to re-run and from which agent

**On user revise** at checkpoint: if they edited an artifact (e.g. `findings.md`), run staleness pass before next dispatch.

**On startup:** if task artifacts under `docs/working/<TASK>/` were edited outside orchestrator, compare against last completed step outputs and mark downstream stale.

---

## Edit-source loop

When the user **revise**s with the same feedback repeatedly:

1. Record **User revision** + theme in `@profile:artifact.run_log`
2. Increment **Revision patterns** table (same theme → count++)
3. At **count ≥ 3**, orchestrator suggests **Source fix suggested** — e.g. update `@profile:rules.i18n`, `agent-decisions.md`, or specialist `.agent.md`, not only re-run the step

Fix the factory (Layer 3), not only the product (Layer 4).

---

## Scoped context packs

Dispatch and specialists must load **only** files listed in plan `context_files` + step **Inputs** + task Layer 4 artifacts.

**Do not load by default:** other `TASK-*` folders, full plan history, entire `@profile:artifact.run_log`, all of `docs/context/` when only named files apply.

Orchestrator dispatch format includes **Load** and **Do not load** lists (see orchestrator.agent.md).

---

## Orchestrator

- Proceed when `@profile:artifact.plan` exists with user goal and **User plan review → approved**
- Plan approval gate: user reads full plan before step 1 (always **anchor**)
- **Tiered human checkpoints** — `gate_tier` per step from plan
- **Staleness pass** when inputs change or user revises artifacts
- **Edit-source loop** — track revision themes in run-log; suggest rule/context updates after 3 similar revises
- After debugger step: dispatch **testing agent** when `@profile:artifact.test_gap` exists (do not skip)
- Skip or fast-complete testing when handoff lists no new testable exports **and** no test-gap
- Never ask the user to choose stack, reuse, or test policy
- Final sign-off: user **proceed** after `flow-end-validator` before `phase: done`

---

## Specialists

Before writing code, read assigned context catalogs for symbols you plan to add or change.

After writing exports, add `## <file-path>` + `purpose` row in the correct context MD (see profile `agent_bindings.*.context_writes`).

**When `done_when` is met:** run **Verify** checklist, write IR/handoff if required, stop — orchestrator posts tiered checkpoint; user **proceed** before next step (unless `gate_tier: auto` and `fast_mode: true`).
