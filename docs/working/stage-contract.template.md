# Stage contract — Step N / `<agent>`

> Per-step contract (ICM-style). Plan-agent copies abbreviated rows into `plan.md`; specialists follow this shape.  
> **Layer 3** = `@profile:context.*` + `@profile:rules.*` · **Layer 4** = `@profile:artifact.*`  
> **Profile:** [`project.profile.yaml`](../project.profile.yaml)

## Reads

### Rules (Layer 3)

| Slot | Purpose |
|------|---------|
| | `@profile:rules.*` |

### Context (Layer 3)

| Slot | Purpose |
|------|---------|
| | `@profile:context.*` |

### Working artifacts (Layer 4)

| Slot | Purpose |
|------|---------|
| | `@profile:artifact.*` |

## Do not load

- Other tasks under `@profile:paths.working_root`
- Full `@profile:artifact.run_log` (orchestrator summary only if needed)
- Entire plan when only acceptance rows are required
- Forbidden scopes from `@profile:agent_bindings.<agent>.forbidden_globs`

## Steps

<!-- What this agent does — from plan.md task column -->

## Writes

| Target | Slot / kind |
|--------|-------------|
| | file / handoff / summary / catalog row |

## Verify (before marking step done)

- [ ] <!-- cross-stage check -->
- [ ] <!-- handoff lists every new export -->
- [ ] <!-- consistent with verify_against from plan.md -->

## Gate

| Field | Value |
|-------|-------|
| **gate_tier** | `anchor` \| `light` \| `auto` |
| **verify_against** | <!-- upstream artifact(s) --> |
