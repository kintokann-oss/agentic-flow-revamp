# Project instructions

1. **Project factory:** [`docs/project.profile.yaml`](docs/project.profile.yaml) — paths, stacks, agent bindings.
2. **App architecture:** [`docs/rules/rules-architecture.md`](docs/rules/rules-architecture.md)
3. **Ubiquitous language:** [`docs/context/UBIQUITOUS_LANGUAGE.md`](docs/context/UBIQUITOUS_LANGUAGE.md) — plan-agent maintains shared terms.
4. **Agent template:** [`.github/agents/agent.template.md`](.github/agents/agent.template.md)
5. Read [`docs/context/INDEX.md`](docs/context/INDEX.md) before new code.
6. UI work: [`docs/rules/rules-theming.md`](docs/rules/rules-theming.md) and [`docs/rules/rules-i18n.md`](docs/rules/rules-i18n.md)
7. Tests: [`docs/context/test-writing.md`](docs/context/test-writing.md)
8. Use specialist agents from `.github/agents/`
9. Orchestrator: tiered gates, staleness, `state.yaml` / `run-log.md`
10. **Plan-agent first:** align language + scenarios → `plan.md` → user **proceed** → orchestrator
11. Final step: `flow-end-validator` — context audit + tests + sign-off
12. Bug-fix: debugger → `test-gap.md` → testing agent
