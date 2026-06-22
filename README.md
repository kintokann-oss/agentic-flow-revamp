# agentic-flow-revamp

Multi-agent workflow with generic agents, a project profile, and an app under `apps/`.

Repository: [kintokann-oss/agentic-flow-revamp](https://github.com/kintokann-oss/agentic-flow-revamp)

---

## What this is

Specialist agents run in sequence. Each step reads and writes files under `docs/working/<TASK-ID>/`. You approve the plan and checkpoints; agents do not share context in chat.

Paths, commands, and stack labels live in [`docs/project.profile.yaml`](docs/project.profile.yaml). Agent roles stay in [`.github/agents/`](.github/agents/) and use `@profile:` slots — not hardcoded paths.

---

## What it offers

| Piece | Location |
|-------|----------|
| Agents | [`.github/agents/`](.github/agents/) |
| Profile (paths, bindings, commands) | [`docs/project.profile.yaml`](docs/project.profile.yaml) |
| Orchestration | [`docs/rules/agent-decisions.md`](docs/rules/agent-decisions.md) |
| Coding rules | [`docs/rules/`](docs/rules/) |
| Export catalogs | [`docs/context/`](docs/context/) |
| Task artifacts | [`docs/working/<TASK-ID>/`](docs/working/) |
| Glossary | [`docs/context/UBIQUITOUS_LANGUAGE.md`](docs/context/UBIQUITOUS_LANGUAGE.md) |
| Handoff audit | [`scripts/validate_context_catalog.py`](scripts/validate_context_catalog.py) |

Roster and step order: [`docs/AGENT-REGISTRY.md`](docs/AGENT-REGISTRY.md) · Artifacts: [`docs/working/ARTIFACTS.md`](docs/working/ARTIFACTS.md)

---

## Layers

| Layer | Location | Role |
|-------|----------|------|
| 1 | `.github/agents/` | Generic agent roles |
| 2 | `docs/rules/agent-decisions.md` | Gates, reuse, routing |
| 3 | `project.profile.yaml`, `docs/rules/`, `docs/context/` | Project-specific config and catalogs |
| 4 | `docs/working/<TASK-ID>/` | One task’s plan, handoffs, state |

---

## App under `apps/`

Single page: user toggles **Toggle state** on/off; UI and **FlowDialog** follow that state; optional **Saved time** inside **FlowDialog**. Module layout: [`docs/rules/rules-architecture.md`](docs/rules/rules-architecture.md). Run/test commands: `commands.*` in the profile.

---

## Start a task

1. **plan-agent** → `docs/working/TASK-001/plan.md`
2. You reply **proceed**
3. **orchestrator** runs plan steps
4. **flow-end-validator** — catalog audit + tests + sign-off

Index: [`docs/working/INDEX.md`](docs/working/INDEX.md)

---

## Port to another repo

Copy agents and `docs/`. Edit `project.profile.yaml`, rules, and context for the new product. Keep `.github/agents/` unchanged.
