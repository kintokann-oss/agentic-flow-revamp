# Run log — TASK-XXX

> Per-step trace: **agent**, **files read**, **files written**, **outcome**.  
> Orchestrator updates after each step. See also `state.yaml` for machine-readable fields.

## Why this file exists

Same story as `state.yaml`, but in a table you can skim in a PR or presentation. **plan-agent** also reads the previous task's run-log when picking the next TASK id.

**Handles:** per-step audit · **edit-source** revision patterns · optional summary.  
**See also:** [ARTIFACTS.md](ARTIFACTS.md#run-logmd)

| Step | Agent | Gate | Status | Files read | Files written | Outcome | User revision | Source fix suggested |
|------|-------|------|--------|------------|---------------|---------|---------------|----------------------|
| 1 | navigator | anchor | pending | | | | | |

**Gate** = `anchor` \| `light` \| `auto` from plan.md.

## Revision patterns (edit-source loop)

> Orchestrator appends rows when the user **revise**s with feedback. After **3 similar revisions** on the same theme, suggest updating the **source** file (rules/context/agent), not only re-running the step.

| Theme | Count | Suggested source fix |
|-------|-------|----------------------|
| | | |

## Summary

- **Task:** 
- **Started:** 
- **Completed:** 
