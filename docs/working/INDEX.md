# Working tasks

| Task | Goal | Status | Run log |
|------|------|--------|---------|
| *(none yet)* | | | |

New tasks start with **plan-agent** → `docs/working/TASK-001/plan.md` (then TASK-002, …).

---

## Task artifacts (per `docs/working/<TASK-ID>/`)

**Full guide:** [ARTIFACTS.md](ARTIFACTS.md)

| File | Writer | Reader | Why (one line) |
|------|--------|--------|----------------|
| `plan.md` | plan-agent | you, orchestrator | Goal + steps (`gate_tier`, `verify_against`) + stage contracts |
| `state.yaml` | orchestrator | orchestrator | Save-state, staleness, tiered gates |
| `run-log.md` | orchestrator | you, plan-agent | Audit trail + edit-source revision patterns |
| `findings.md` | navigator, fe-design-navigator | fe-dev, be-sql-agent, you | Reuse/create + design findings |
| `be-sql-handoff.md` | be-sql-agent | be-dev, you | Schema summary before routes/services |
| `contract-summary.md` | be-dev | fe-dev, be-testing-agent, you | Readable API IR (be-dev writes after routes) |
| `be-test-handoff.md` | be-dev | be-testing-agent | BE test brief |
| `ui-summary.md` | fe-dev | you | Readable UI checkpoint summary |
| `fe-test-handoff.md` | fe-dev | fe-testing-agent | FE test brief |
| `test-gap.md` | debugger | testing agent | Bug-fix regressions |
| `context-audit.md` | flow-end-validator | you | Catalog audit report (script output) |

Templates: [`plan.template.md`](plan.template.md) · [`state.template.yaml`](state.template.yaml) · [`run-log.template.md`](run-log.template.md) · [`stage-contract.template.md`](stage-contract.template.md) · [`contract-summary.template.md`](contract-summary.template.md) · [`be-sql-handoff.template.md`](be-sql-handoff.template.md) · [`ui-summary.template.md`](ui-summary.template.md) · [`findings.template.md`](findings.template.md) · [`be-test-handoff.template.md`](be-test-handoff.template.md) · [`fe-test-handoff.template.md`](fe-test-handoff.template.md) · [`test-gap.template.md`](test-gap.template.md) · [`context-audit.template.md`](context-audit.template.md)

Testing workflow: [`test-writing.md`](../context/test-writing.md) · Gate tiers: [`agent-decisions.md`](../rules/agent-decisions.md#gate-tiers)
