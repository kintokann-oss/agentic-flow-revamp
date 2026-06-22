# Project instructions

**Layers:** Agents (`.github/agents/`) = generic, `@profile:` slots only. Rules + context + profile = project-specific.

1. **Project factory:** [`docs/project.profile.yaml`](docs/project.profile.yaml) — paths, stacks, agent bindings.
2. **Orchestration:** [`docs/rules/agent-decisions.md`](docs/rules/agent-decisions.md) — gates, reuse, agent routing.
3. **Agent roster:** [`docs/AGENT-REGISTRY.md`](docs/AGENT-REGISTRY.md) — separation of concerns matrix.
4. **Agent template:** [`.github/agents/agent.template.md`](.github/agents/agent.template.md)
5. Read [`docs/context/INDEX.md`](docs/context/INDEX.md) before new code.
6. App architecture: [`docs/rules/rules-architecture.md`](docs/rules/rules-architecture.md)
7. Ubiquitous language: [`docs/context/UBIQUITOUS_LANGUAGE.md`](docs/context/UBIQUITOUS_LANGUAGE.md)
8. UI: [`docs/rules/rules-theming.md`](docs/rules/rules-theming.md), [`docs/rules/rules-i18n.md`](docs/rules/rules-i18n.md)
9. Tests: [`docs/context/test-writing.md`](docs/context/test-writing.md)
10. **Plan-agent first** → user **proceed** → **orchestrator** → specialists → **flow-end-validator**

Do not hardcode stack or repo paths in agent files — use `@profile:` slots from the profile.
