# Application architecture

**Slot:** `rules.architecture` · **Terms:** [UBIQUITOUS_LANGUAGE.md](../context/UBIQUITOUS_LANGUAGE.md)

## What this repo ships today

A **minimal skeleton** — not a product demo. The sample app exists only to run the agent workflow against real paths:

| Layer | Shipped today | Added per task by agents |
|-------|---------------|---------------------------|
| Backend | Health + info routes, connection module, empty migration placeholder | Routes, services, migrations, tables |
| Frontend | Root **App** shell + info API client | Components, hooks, clients, i18n keys |
| Store | Connection helper only — **no feature tables yet** | be-sql-agent adds DDL |

Feature examples in context catalogs (`Item`, `DetailPanel`, `/api/items`, …) are **generic templates** — not implemented until a task adds them.

## Boundaries

| Layer | Profile path | Responsibility |
|-------|--------------|----------------|
| Client | `@profile:paths.frontend_root` | Pages, components, hooks, API clients, i18n, theme tokens |
| Server | `@profile:paths.backend_root` | HTTP routes, domain services |
| Schema | `@profile:paths.migrations_root`, connection module | DDL, seeds, init (**be-sql-agent**) |
| Store | From `@profile:stack.backend.db` + `DATABASE_URL` | Tables added by migrations |

Client calls server over HTTP JSON. Server reads and writes the store through services only.

## Backend layout

```
@profile:paths.backend_root/
├── migrations/     # be-sql-agent — sorted SQL files
├── src/
│   ├── db.py       # connection + init_db (be-sql-agent)
│   ├── main.py     # app entry, mount routers
│   ├── routes/     # be-dev — thin handlers
│   └── services/   # be-dev — domain + queries
└── tests/          # be-testing-agent
```

| Module (skeleton) | Role |
|-------------------|------|
| `routes/health.py` | Liveness |
| `routes/info.py` | Name/version for client header |

**Rule:** routes call services; services run SQL. No SQL in routes; no HTTP types in services.

Catalogs: [be-schema.md](../context/be-schema.md) · [api-list.md](../context/api-list.md)

## Frontend layout

```
@profile:paths.frontend_root/src/
├── App.tsx           # root shell (skeleton)
├── api/              # one module per backend resource
├── components/       # fe-dev — Base* and extending tiers
├── hooks/            # fe-dev
├── styles/theme.css  # tokens only file with raw colors
└── i18n/locales/
```

| Piece (skeleton) | Role |
|------------------|------|
| **App** | Root page — loads info client on mount |
| **fetchInfo** | GET `/api/info` client |

Design tiers: [fe-design-system.md](../context/fe-design-system.md)

## Persistence (skeleton)

No feature tables in the initial migration placeholder. be-sql-agent adds migrations per task; document each in [be-schema.md](../context/be-schema.md).

## Out of scope

| Topic | Policy |
|-------|--------|
| Auth | `defaults.auth` in profile |
| Deploy / CI | Not in task artifacts |
| E2E | [rules-testing.md](rules-testing.md) unless plan adds it |

## When to edit

Update when module boundaries or store shape change. Per-feature detail stays in context catalogs and **UBIQUITOUS_LANGUAGE**.
