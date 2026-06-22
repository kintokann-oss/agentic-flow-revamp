# Ubiquitous language

> **Shared vocabulary** for this repo — used by you, agents, and context catalogs.  
> **Maintained by:** plan-agent (grill-with-docs) adds or sharpens terms each task; dev agents use these names in code and catalog `purpose` rows.  
> Inspired by [grill-with-docs](https://www.aihero.dev/grill-with-docs) / domain-driven design ubiquitous language.

**Format:** `**Term**:` definition. Link to catalog or code when grounded.

## How to use this file

- **Read when:** Before any task — align vocabulary with plan-agent, navigator, and catalog `purpose` text
- **Write when:** plan-agent grills a new task — add or sharpen terms before writing `plan.md`
- **Do not** duplicate full catalog rows here — link to [INDEX.md](INDEX.md) catalogs instead

---

## Application shell

**App:** Root React page at `apps/web-react/src/App.tsx` — layout shell, flow background, hosts dialogs and controls.

**Flow background:** Full-page gradient driven by toggle state (`--gradient-flow-active` / `--gradient-flow-idle`).

---

## UI components (tiers)

**Base component:** Foundation primitive in `components/Base<Name>/`. Required before an extending component on the same primitive. Catalog: [fe-design-system.md](fe-design-system.md) base table.

**Extending component:** Specialized UI built on a registered base (`extends_base`). Catalog: fe-design-system extending table.

**BaseButton:** Base true/false control — app-wide toggle/button primitive.

**FlowDialog:** Base status dialog shell reflecting flow on/off surface state.

**DetailPanel *(example term)*:** Generic name for an **extending component** nested inside a base dialog — use your domain name in plans and catalogs; not shipped in this repo.

---

## Backend

**Route handler:** FastAPI function in `apps/api/src/routes/` (catalog: [api-list.md](api-list.md)).

**Service:** Domain function in `apps/api/src/services/` (catalog: [be-services.md](be-services.md)).

**Migration:** Versioned SQL file under `apps/api/migrations/` — owned by **be-sql-agent** (catalog: [be-schema.md](be-schema.md)).

**Toggle state:** Persisted boolean (`GET`/`PUT` `/api/toggle-state`); stored in SQLite `app_state`.

**Item *(example term)*:** Generic domain entity for list/CRUD features — placeholder vocabulary for plans; no `/api/items` in this repo yet.

---

## Agent flow terms

**Task:** One user goal executed as `docs/working/<TASK-ID>/` artifacts.

**Findings:** Reuse/create decisions from navigator (+ design findings from fe-design-navigator).

**Handoff:** Test brief from be-dev or fe-dev to the matching testing agent.

**Context catalog:** Durable MD under `docs/context/` indexed by [INDEX.md](INDEX.md).

---

## Relationships

- **App** hosts **FlowDialog** and **BaseButton**.
- **Extending component** → exactly one **Base component** via `extends_base`.
- **Route handler** may call **Service** functions; catalog rows must stay aligned.

---

## Adding terms (plan-agent)

When grilling a new task:

1. Check whether the user’s words match an existing **Term** — challenge collisions (e.g. two meanings of “dialog”).
2. Add new terms here with precise definitions before writing `plan.md`.
3. If a decision is surprising or hard to reverse, add an [ADR](../decisions/INDEX.md) and link it from the term or plan.
