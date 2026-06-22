# Test writing

> **Type:** Procedural context (patterns and examples) — **not** a symbol-per-file catalog. Test inventory lives in [be-tests.md](be-tests.md) and [fe-tests.md](fe-tests.md).  
> **Policy:** [`rules-testing.md`](../rules/rules-testing.md) · **Agents:** `fe-testing-agent` / `be-testing-agent` · **Commands:** [`project.profile.yaml`](../project.profile.yaml) → `commands.be_test`, `commands.fe_test`

Colocated unit/integration tests only. No E2E unless plan adds it. Stack: `@profile:stack.*` in profile.

---

## Test stack

| Layer | Tool | Location | What it tests |
|-------|------|----------|---------------|
| FE unit / integration | Vitest + RTL | `@profile:paths.frontend_root/**/*.test.{ts,tsx}` | Hooks, API clients, components, App |
| BE integration | pytest + TestClient | `@profile:paths.backend_tests/test_*.py` | Routes, services, DB persistence |
| Shared FE setup | — | `src/test-setup.ts` under frontend root | jest-dom + i18n init |

---

## When tests get written (agent flow)

| Trigger | Input | Agent | Then |
|---------|-------|-------|------|
| Feature / new exports | `be-test-handoff.md` / `fe-test-handoff.md` | be/fe-testing-agent | Run `@profile:commands.*_test`; update test catalog |
| Bug-fix | `test-gap.md` | be/fe-testing-agent | Implement every listed test |
| No new exports in handoff | — | orchestrator | May skip testing step (see agent-decisions) |

---

## How to run

See `@profile:commands.fe_test` and `@profile:commands.be_test` in [`project.profile.yaml`](../project.profile.yaml). Run from the `cwd` given in each command block.

### After adding tests

1. Run the test command until green
2. Add or update rows in `@profile:context.fe_tests` or `@profile:context.be_tests`

---

## Creating tests — step-by-step (testing agents)

### 1. Determine scope

- If `@profile:artifact.test_gap` exists → read it **first**; implement **every** listed test
- Else read `@profile:artifact.be_test_handoff` or `@profile:artifact.fe_test_handoff`

### 2. Read sources

- Export under test (component, hook, route, service)
- Existing colocated test file (extend) or create sibling
- [`rules-testing.md`](../rules/rules-testing.md), [`rules-i18n.md`](../rules/rules-i18n.md) (FE)
- [`fe-i18n.md`](fe-i18n.md) for locale keys

### 3. Identify behaviors

| Kind | Test |
|------|------|
| API client | fetch/PUT URL/body; error on non-ok |
| Hook | initial load, persist/update, error rollback |
| Component | render states, user events, aria/testids |
| Route | status code, JSON body, persistence |
| i18n UI | `i18n.t('namespace:key')` — not hardcoded strings |

### 4. Write tests (AAA)

Every test uses **Arrange → Act → Assert** comments.

### 5. Run until green

Fix failures in test files unless the bug is in production code (hand off to debugger).

### 6. Update catalog

Add row in `@profile:context.be_tests` or `@profile:context.fe_tests` for new test files.

---

## FE patterns

Use `@profile:stack.frontend` test tools from the profile. Examples below use placeholder names.

### API client

```typescript
import { afterEach, describe, expect, it, vi } from 'vitest'
import { fetchItems } from './items'

afterEach(() => {
  vi.unstubAllGlobals()
})

describe('items API', () => {
  it('fetchItems returns JSON', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ items: [] }),
    }))
    await expect(fetchItems()).resolves.toEqual({ items: [] })
  })
})
```

### Hook

```typescript
import { act, renderHook, waitFor } from '@testing-library/react'
import { vi } from 'vitest'
import * as itemsApi from '../api/items'
import { useItems } from './useItems'

it('persists updated value', async () => {
  vi.spyOn(itemsApi, 'fetchItems').mockResolvedValue({ items: [] })
  vi.spyOn(itemsApi, 'saveItem').mockResolvedValue({ id: '1' })

  const { result } = renderHook(() => useItems())
  await waitFor(() => expect(result.current.loading).toBe(false))

  await act(async () => {
    await result.current.save({ id: '1' })
  })

  expect(itemsApi.saveItem).toHaveBeenCalledWith({ id: '1' })
})
```

### Component (with i18n)

```typescript
import { render, screen } from '@testing-library/react'
import i18n from '../../i18n'
import { PrimaryAction } from './PrimaryAction'

it('renders label from locale', () => {
  render(<PrimaryAction onClick={vi.fn()} />)
  expect(screen.getByText(i18n.t('app:actions.save'))).toBeInTheDocument()
})
```

### Selector priority (RTL)

1. `getByRole` (with accessible name)
2. `getByTestId`
3. `getByText` via `i18n.t(...)`

---

## BE patterns

Use `@profile:stack.backend` test tools from the profile.

### Route + isolated DB

```python
@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    db_file = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_file}")
    init_db()
    with TestClient(app) as test_client:
        yield test_client

def test_list_items_empty(client: TestClient):
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json() == {"items": []}
```

Colocate: `tests/test_<module>.py` covers routes/services in scope.

---

## Regression from debugger (`test-gap.md`)

1. Debugger fills [`test-gap.template.md`](../working/test-gap.template.md)
2. Must include **Why existing tests did not catch this**
3. Testing agent adds each listed test
4. Task not done until test-gap tests pass

---

## Anti-patterns

| Avoid | Do instead |
|-------|------------|
| Hardcoded locale strings in FE assertions | `i18n.t('namespace:key')` |
| Tests in `__tests__/` or distant folders | Colocate next to source |
| One test covering many unrelated flows | One behavior per test |
| Skipping test-gap tests | Implement every row |
| Marking step done before test command passes | Run `@profile:commands.*_test` |

---

## Handoff from dev agents

| Lane | Dev writes | Testing agent reads |
|------|------------|---------------------|
| Backend | `be-test-handoff.md` | `be-testing-agent` |
| Frontend | `fe-test-handoff.md` | `fe-testing-agent` |

Full-stack: **BE handoff → be-testing → FE handoff → fe-testing** (separate files).

---

## Catalogs (reference)

- [`fe-tests.md`](fe-tests.md)
- [`be-tests.md`](be-tests.md)
