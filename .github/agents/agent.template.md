---
name: agent-name
description: One-line role summary — no stack, framework, or repo path names.
---

# Agent Title

## Role

<!-- One paragraph: what this agent does. Project-agnostic. -->

**Boundary:** <!-- One sentence — what this agent owns vs what it must never do. -->

## When you run

<!-- Plan position, prerequisites, orchestrator triggers. Use agent names and @profile slots only. -->

## Reads

Resolve paths from [`docs/project.profile.yaml`](../../docs/project.profile.yaml). Use `@profile:` slot names below — **never** hardcode paths like `apps/` or stack names like FastAPI/React.

### Rules (Layer 3)

| Slot | Purpose |
|------|---------|
| `@profile:rules.decisions` | Orchestration and reuse policy (sections as needed) |
| | |

### Context (Layer 3)

| Slot | Purpose |
|------|---------|
| `@profile:context.index` | Catalog index — read relevant rows only |
| | |

### Working artifacts (Layer 4)

| Slot | Purpose |
|------|---------|
| `@profile:artifact.plan` | Goal, acceptance, step scope (sections as listed in dispatch) |
| | |

### Commands (from profile)

| Slot | When |
|------|------|
| `@profile:commands.be_test` | After BE test changes (when profile defines it) |
| | |

## Do not load

- Other tasks under `@profile:paths.working_root` (not current TASK-ID)
- Full `@profile:artifact.run_log` unless orchestrator summary is needed
- Entire context tree — only slots listed above
- Forbidden scopes from `@profile:agent_bindings.<this-agent>.forbidden_globs`

## Steps

1. <!-- Numbered procedure -->
2. <!-- Run Verify before handoff -->

## Writes

### Code / contract

| Target | Slot |
|--------|------|
| | `@profile:agent_bindings.<this-agent>.scope_glob` |

### Working artifacts (Layer 4)

| Artifact | Template |
|----------|----------|
| | `@profile:templates.<name>` |

### Context catalog (Layer 3)

| Slot | When |
|------|------|
| | Add or update `## <file-path>` row with required `purpose` |

## Verify

- [ ] <!-- Cross-stage check -->
- [ ] <!-- Handoff complete -->
- [ ] <!-- Consistent with verify_against from dispatch -->

## Handoff

Stop. Tell the user: *"Step complete — return to **orchestrator** for review before `<next-agent>`."*

## Never

- <!-- Hard prohibitions — especially work owned by another agent -->
- Edit forbidden scopes from profile bindings
- Name project stacks, frameworks, or literal repo paths (use `@profile:` slots)
