# Project instructions

1. **Project factory:** [`docs/project.profile.yaml`](docs/project.profile.yaml) — paths, stacks, agent bindings.
2. **Ubiquitous language:** [`docs/context/UBIQUITOUS_LANGUAGE.md`](docs/context/UBIQUITOUS_LANGUAGE.md) — plan-agent (grill-with-docs) maintains shared terms.
3. **Agent template:** [`.github/agents/agent.template.md`](.github/agents/agent.template.md)
4. Read [`docs/context/INDEX.md`](docs/context/INDEX.md) and [`UBIQUITOUS_LANGUAGE.md`](docs/context/UBIQUITOUS_LANGUAGE.md) before new code.
5. UI work: [`docs/rules/rules-theming.md`](docs/rules/rules-theming.md) and [`docs/rules/rules-i18n.md`](docs/rules/rules-i18n.md)
6. Tests: [`docs/context/test-writing.md`](docs/context/test-writing.md)
7. Use specialist agents from `.github/agents/`
8. Orchestrator: tiered gates, staleness, `state.yaml` / `run-log.md`
9. **Plan-agent first (grill-with-docs):** align language + scenarios → **`plan.md`** → user **proceed** → orchestrator
10. Final step: `flow-end-validator` — context audit + tests + sign-off
11. Bug-fix: debugger → `test-gap.md` → testing agent
