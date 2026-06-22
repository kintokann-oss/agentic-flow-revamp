# Context files — index

Read **one** relevant catalog before opening source code.  
**Project paths and slots:** [`docs/project.profile.yaml`](../project.profile.yaml)

## Catalog conventions

### Section headings

- Format: `## <repo-relative-source-path>` (e.g. `## apps/api/src/routes/toggle_state.py`)
- One section per source file
- **Must match** the `File` column in test handoffs — `validate_context_catalog.py` uses exact heading match at task end

### Tables

- One row per export (route, service, component, hook, test file, i18n key, etc.)
- **`purpose` is human-written and required** where the column exists — audit rejects empty, `tbd`, `(sync — add purpose)`
- Agents add/update rows after implementation; humans may refine `purpose` text

### Who reads / writes

| Role | Reads | Writes |
|------|-------|--------|
| plan-agent, navigator | Relevant catalogs + ubiquitous language | — |
| be-dev, fe-dev | Scoped catalogs for reuse | Export rows in matching catalog |
| be/fe-testing-agent | Test catalogs + handoffs | Test file rows in be-tests / fe-tests |
| flow-end-validator | All handoffs vs catalogs | — (audit only) |

### Audit mapping (`project.profile.yaml` → `context_routing`)

| Handoff kind | Routes to catalog |
|--------------|-------------------|
| BE: `route` | api-list.md |
| BE: `service` | be-services.md |
| BE: `pydantic_model` | types.md |
| SQL: `migration`, `table`, `db_module` | be-schema.md |
| FE: `component` | fe-components.md |
| FE: `hook` | fe-utils.md |
| FE: `api client` | fe-services.md |
| FE i18n keys | fe-i18n.md |
| Suggested BE tests | be-tests.md |
| Suggested FE tests | fe-tests.md |

---

## Catalog index

| File | Slot | When to read | Primary readers | Primary writers |
|------|------|--------------|-----------------|-----------------|
| [UBIQUITOUS_LANGUAGE.md](UBIQUITOUS_LANGUAGE.md) | `context.ubiquitous_language` | **Before any task** — shared domain terms | plan-agent, navigator, all specialists | plan-agent |
| [test-writing.md](test-writing.md) | `context.test_writing` | How to create/run tests | be/fe-testing-agent, debuggers | humans |
| [fe-utils.md](fe-utils.md) | `context.fe_utils` | Helpers, hooks, pure functions | fe-dev, fe-debugger, fe-testing-agent | fe-dev |
| [fe-components.md](fe-components.md) | `context.fe_components` | UI components | fe-dev, fe-design-navigator, fe-testing-agent | fe-dev |
| [fe-design-system.md](fe-design-system.md) | `context.fe_design_system` | Theme paths, base vs extending | fe-design-navigator, fe-dev | fe-dev |
| [fe-i18n.md](fe-i18n.md) | `context.fe_i18n` | Locale keys and namespaces | fe-design-navigator, fe-dev, fe-testing-agent | fe-dev |
| [fe-services.md](fe-services.md) | `context.fe_services` | API clients, stores | fe-dev, fe-debugger | fe-dev |
| [api-list.md](api-list.md) | `context.api_catalog` | HTTP routes, handlers | be-dev, be-testing-agent | be-dev |
| [be-schema.md](be-schema.md) | `context.be_schema` | SQLite migrations, tables, db.py | be-sql-agent, be-dev | be-sql-agent |
| [be-services.md](be-services.md) | `context.be_services` | Backend service/domain | be-dev, be-debugger | be-dev |
| [fe-tests.md](fe-tests.md) | `context.fe_tests` | Frontend test catalog | fe-testing-agent, fe-debugger | fe-testing-agent |
| [be-tests.md](be-tests.md) | `context.be_tests` | Backend test catalog | be-testing-agent, be-debugger | be-testing-agent |
| [envs.md](envs.md) | `context.envs` | Environment variables | be-dev, fe-dev | humans |
| [types.md](types.md) | `context.types` | Shared types, DTOs | be-dev, fe-dev | be-dev |

### Column reference (by file)

| File | Columns |
|------|---------|
| api-list.md | method, path, handler, request_type, response_type, tests |
| be-schema.md | migration: file, purpose, tables · table: column, type, constraints, purpose · db.py: name, kind, purpose |
| be-services.md | name, purpose, tests, depends_on |
| types.md | name, kind, used_by |
| fe-components.md, fe-utils.md | name, purpose, tests, depends_on |
| fe-services.md | name, purpose, tests, api_calls |
| fe-i18n.md | namespace, key, purpose, used_in |
| be-tests.md, fe-tests.md | covers_symbol, covers_file, kind |
| envs.md | key, required, description, used_in_files |

**Maintained by:** dev and testing agents after exports change — update the relevant catalog row manually.
