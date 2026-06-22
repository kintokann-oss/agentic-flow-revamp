# Ubiquitous language

> **Shared vocabulary** for this repo — used by agents and context catalogs.  
> **Maintained by:** plan-agent adds or sharpens terms each task; dev agents use these names in code and catalog `purpose` rows.

**Format:** `**Term**:` definition. Link to [INDEX.md](INDEX.md) catalogs when grounded.

## How to use this file

- **Read when:** Before any task — align vocabulary with plan-agent and catalog `purpose` text
- **Write when:** plan-agent grills a new task — add or sharpen terms before writing `plan.md`
- **Do not** duplicate full catalog rows here — link to catalogs instead
- Terms marked *(example)* are generic placeholders for plans — not shipped code

---

## Application shell

**App:** Root page at `@profile:paths.frontend_root/src/App.tsx` — layout shell for the skeleton; hosts feature UI as tasks add it.

---

## UI components (tiers)

**Base component:** Foundation primitive in `components/Base<Name>/`. Required before an extending component on the same primitive. Catalog: [fe-design-system.md](fe-design-system.md).

**Extending component:** Specialized UI built on a registered base (`extends_base`). Catalog: fe-design-system extending table.

**BaseCard *(example)*:** Generic base surface primitive — use your domain name in plans.

**DetailPanel *(example)*:** Generic extending component nested inside a base shell.

---

## Backend

**Route handler:** HTTP handler in `@profile:paths.backend_root/src/routes/` (catalog: [api-list.md](api-list.md)).

**Service:** Domain function in `@profile:paths.backend_root/src/services/` (catalog: [be-services.md](be-services.md)).

**Migration:** Versioned SQL under `@profile:paths.migrations_root/` — owned by **be-sql-agent** (catalog: [be-schema.md](be-schema.md)).

**Item *(example)*:** Generic domain entity for list/CRUD features — placeholder for plans and catalog examples.

---

## Agent flow terms

**Task:** One user goal executed as `docs/working/<TASK-ID>/` artifacts.

**Findings:** Reuse/create decisions from navigator (+ design findings from fe-design-navigator).

**Handoff:** Test brief from be-dev or fe-dev to the matching testing agent.

**Context catalog:** Durable MD under `docs/context/` indexed by [INDEX.md](INDEX.md).

---

## Relationships

- **Extending component** → exactly one **Base component** via `extends_base`.
- **Route handler** may call **Service** functions; catalog rows must stay aligned.
- Skeleton **App** loads **fetchInfo** only until fe-dev adds feature UI.

---

## Adding terms (plan-agent)

1. Check whether the user's words match an existing **Term** — challenge collisions.
2. Add new terms with precise definitions before writing `plan.md`.
3. If a decision is hard to reverse, add an [ADR](../decisions/INDEX.md) and link it from the term or plan.
