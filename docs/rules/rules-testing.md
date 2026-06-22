# Testing rules

Policy details and examples: [`test-writing.md`](../context/test-writing.md)  
Commands: [`project.profile.yaml`](../project.profile.yaml)

## Placement (colocated)

**Every test file lives in the same directory as the source it covers** — component folder, hook file, API client, route module, or service module. No separate test trees for symbol-level tests.

| Source | Test file (same folder) |
|--------|------------------------|
| `components/Foo/Foo.tsx` | `components/Foo/Foo.test.tsx` |
| `hooks/useBar.ts` | `hooks/useBar.test.ts` |
| `api/client.ts` | `api/client.test.ts` |
| `routes/items.py` | `tests/test_items.py` |
| `services/items.py` | covered via route tests or `tests/test_*.py` |

**Do not** use `__tests__/`, repo-root test mirrors, or distant folders for per-symbol tests.

**Exception:** shared setup only (`test-setup.ts`, pytest `conftest.py`) at app config paths.

## Naming

- `Foo.tsx` → `Foo.test.tsx`
- `useBar.ts` → `useBar.test.ts`
- Route/service coverage → `tests/test_<feature>.py`

## Stack

See `@profile:stack.*` in [`project.profile.yaml`](../project.profile.yaml).

| Layer | Tool (this project) |
|-------|---------------------|
| FE | Vitest + React Testing Library + jsdom |
| BE | pytest + FastAPI TestClient |
| E2E | Out of scope unless profile/plan adds it |

## Required

- Every exported symbol → colocated test file documented in `fe-tests.md` / `be-tests.md`
- After adding tests: run `@profile:commands.be_test` or `@profile:commands.fe_test` until green
- Update test catalog rows when adding test files

## When to write tests

| Situation | Agent | Action |
|-----------|-------|--------|
| Greenfield / new exports | fe-testing-agent / be-testing-agent | Cover all handoff behaviors |
| Bug-fix task | fe/be-debugger → testing agent | **`test-gap.md`** — implement **every** listed test |
| Symbol already has tests + test-gap exists | testing agent | **Extend** file — do not skip |

## AAA pattern (mandatory)

Every test uses **Arrange → Act → Assert** with comments.

## FE i18n in tests

- Import `./i18n` or rely on `test-setup.ts`
- Assert UI copy with `i18n.t('namespace:key')` when key exists in `fe-i18n.md`
- Do not hardcode user-facing strings in assertions

See [`rules-i18n.md`](rules-i18n.md).

## Handoff

fe-dev writes [`fe-test-handoff.template.md`](../working/fe-test-handoff.template.md); be-dev writes [`be-test-handoff.template.md`](../working/be-test-handoff.template.md) — one file per lane, before the matching testing step.

## Regression from debugger

When `docs/working/<TASK-ID>/test-gap.md` exists:

1. **fe-debugger** / **be-debugger** writes test-gap (why tests missed the bug + tests to add)
2. **fe-testing-agent** / **be-testing-agent** implements **every** listed test
3. Fix is not done until test-gap tests pass

Template: [`test-gap.template.md`](../working/test-gap.template.md)

## Commands

See `@profile:commands.*` in [`project.profile.yaml`](../project.profile.yaml).

## Anti-patterns

- Hardcoded locale strings in FE test assertions
- Skipping test-gap tests because a test file already exists
- Testing implementation details instead of observable behavior
- Marking testing step done while test command fails
