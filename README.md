# Agentic flow

Multi-agent delivery workflow: generic specialist agents, a project profile, and file-based handoffs between steps.

---

## What this is

You state a goal. Agents align on vocabulary, produce a reviewed plan, then run in sequence. Each agent reads and writes markdown/YAML under `docs/working/<TASK-ID>/`. You approve the plan and checkpoints at tiered gates.

Application code, stack, and paths are **not** in agent files. They live in [`docs/project.profile.yaml`](docs/project.profile.yaml). Agents reference slots as `@profile:paths.backend_root`, `@profile:rules.backend`, `@profile:artifact.plan`, etc. The orchestrator resolves slots when dispatching.

---

## What it offers

| Piece | Location |
|-------|----------|
| Agent roles + boundaries | [`.github/agents/`](.github/agents/) · [AGENT-REGISTRY.md](docs/AGENT-REGISTRY.md) |
| Profile (paths, commands, bindings) | [`docs/project.profile.yaml`](docs/project.profile.yaml) |
| Orchestration policy | [`docs/rules/agent-decisions.md`](docs/rules/agent-decisions.md) |
| Project rules | [`docs/rules/`](docs/rules/) — coding, architecture, testing, … |
| Export catalogs | [`docs/context/`](docs/context/) — durable inventory per task |
| Task run | [`docs/working/<TASK-ID>/`](docs/working/) — plan, findings, handoffs, state |
| Agent roster + separation matrix | [`docs/AGENT-REGISTRY.md`](docs/AGENT-REGISTRY.md) |
| Artifact guide | [`docs/working/ARTIFACTS.md`](docs/working/ARTIFACTS.md) |
| Catalog audit script | [`scripts/validate_context_catalog.py`](scripts/validate_context_catalog.py) |

---

## Layers

| Layer | Location | Role |
|-------|----------|------|
| 1 | `.github/agents/` | Generic roles (Reads / Steps / Writes via `@profile:`) |
| 2 | `docs/rules/agent-decisions.md` | Step order, gates, reuse, staleness |
| 3 | `project.profile.yaml` + `docs/rules/` + `docs/context/` | **Your project** — paths, rules, catalogs, glossary |
| 4 | `docs/working/<TASK-ID>/` | **One task** — plan, handoffs, audit trail |

Layer 1–2 port unchanged. Layer 3–4 are replaced or extended per product.

---

## Default task flow

1. **plan-agent** — grill, glossary, `plan.md` → you **proceed**
2. **orchestrator** — steps from plan, `state.yaml`, `run-log.md`
3. **navigator** — reuse/create → `findings.md`
4. Specialists per plan (schema, backend, backend tests, design, frontend, frontend tests, …)
5. **flow-end-validator** — catalog audit + test commands + sign-off

Details and agent list: [`docs/AGENT-REGISTRY.md`](docs/AGENT-REGISTRY.md). Task index: [`docs/working/INDEX.md`](docs/working/INDEX.md).

---

## Adopt in another repository

1. Copy `.github/agents/` and `docs/` layout (rules templates, working templates, agent-decisions).
2. Author [`docs/project.profile.yaml`](docs/project.profile.yaml) — paths, stack, `agent_bindings`, `context_slots`.
3. Fill `docs/rules/` and `docs/context/` for your product (including `rules-architecture.md` and `UBIQUITOUS_LANGUAGE.md` if used).
4. Leave agent markdown unchanged; only profile and Layer 3 docs vary by project.

Run and test commands are defined under `commands.*` in the profile — not in the README.

---

## `@profile:` slots

Placeholders in agent and template files. Resolved from [`docs/project.profile.yaml`](docs/project.profile.yaml) at dispatch time.

| Example slot | Typical use |
|--------------|-------------|
| `@profile:paths.backend_root` | Backend source root |
| `@profile:rules.backend` | Backend coding rules |
| `@profile:context.api_catalog` | Route/export catalog |
| `@profile:artifact.be_test_handoff` | Task handoff file path |
| `@profile:commands.be_test` | Test command for sign-off |

Full binding matrix: profile `agent_bindings` and [`docs/AGENT-REGISTRY.md`](docs/AGENT-REGISTRY.md).
