# Application architecture

**Slot:** `rules.architecture` · **Terms:** [UBIQUITOUS_LANGUAGE.md](../context/UBIQUITOUS_LANGUAGE.md)

## What the app does

One page (**App**). The user sets **Toggle state** on or off with **BaseButton**. **Toggle state** is stored on the server (`GET`/`PUT` `/api/toggle-state`).

| Toggle state | UI |
|--------------|-----|
| **On** | **Flow background** uses the active gradient; **FlowDialog** uses active styling. |
| **Off** | Idle gradient and idle **FlowDialog** styling. |

No **extending components** are shipped yet. When added, register them in [fe-design-system.md](../context/fe-design-system.md) with `extends_base` (see generic **DetailPanel** example there).

## Boundaries

| Layer | Profile path | Responsibility |
|-------|--------------|----------------|
| Client | `@profile:paths.frontend_root` | **App**, components, hooks, API clients, i18n, theme tokens |
| Server | `@profile:paths.backend_root` | HTTP routes, domain services |
| Schema | `@profile:paths.migrations_root`, `src/db.py` | DDL, seeds, connection helpers (**be-sql-agent**) |
| Store | SQLite file (`DATABASE_URL`) | `app_state` |

Client calls server over HTTP JSON. Server reads and writes the store through services only.

## Backend layout

```
@profile:paths.backend_root/
├── migrations/     # be-sql-agent
├── src/
│   ├── db.py       # get_connection, init_db, key constants
│   ├── main.py     # app entry, mount routers, init_db on startup
│   ├── routes/     # be-dev — parse, call service, return model
│   └── services/   # be-dev — parameterized SQL only
└── tests/          # be-testing-agent
```

| Module | Role |
|--------|------|
| `routes/health.py` | Liveness |
| `routes/info.py` | Name/version for client header |
| `routes/toggle_state.py` | **Toggle state** API |
| `services/toggle_state.py` | `app_state` row for toggle key |

**Rule:** routes call services; services run SQL. No SQL in routes; no HTTP types in services.

Catalogs: [be-schema.md](../context/be-schema.md) · [api-list.md](../context/api-list.md) (see **Example format** sections for generic CRUD templates).

## Frontend layout

```
@profile:paths.frontend_root/src/
├── App.tsx           # shell, flow background class, hosts controls
├── api/              # one module per backend resource
├── hooks/            # useToggleState
├── components/
│   ├── BaseButton/   # base — boolean control
│   └── FlowDialog/   # base — flow on/off dialog shell
├── styles/theme.css
└── i18n/locales/
```

| Piece | Role |
|-------|------|
| **App** | Applies `flow-active` / `flow-idle` shell class from toggle |
| **BaseButton** | Sets **Toggle state** via `useToggleState` |
| **FlowDialog** | Surface reflects toggle state |
| **useToggleState** | Load on mount; PUT on change |

Tiers and tokens: [fe-design-system.md](../context/fe-design-system.md)

## Persistence (current)

| Table | Key | Value |
|-------|-----|-------|
| `app_state` | `toggle` | `0` or `1` |

## Out of scope

| Topic | Policy |
|-------|--------|
| Auth | `defaults.auth` in profile |
| Multi-tenant data | Single global toggle |
| Deploy / CI | Not in task artifacts |
| E2E | [rules-testing.md](rules-testing.md) |

## When to edit

Update when module boundaries or store shape change. Feature-level detail stays in context catalogs and **UBIQUITOUS_LANGUAGE**.
