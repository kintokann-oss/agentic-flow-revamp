# Test gap — TASK-XXX

> Written by **fe-debugger** or **be-debugger** before the fix is marked done.  
> **fe-testing-agent** / **be-testing-agent** implements every test listed below.

## Why this file exists

Feature handoffs list *new* test work. Bugs mean *existing tests failed you*. **test-gap** forces the debugger to explain **why tests missed the bug** and list **mandatory regression tests** — the testing agent cannot skip rows even when a test file already exists.

**Handles:** bug narrative · test failure analysis · exact tests to add · minimal fix scope.  
**Not used on feature tasks** — use be/fe-test-handoff instead.  
**See also:** [ARTIFACTS.md](ARTIFACTS.md#test-gapmd)

## Bug summary

<!-- one paragraph -->

## Reproduction

<!-- failing test name, or minimal steps -->

## Why existing tests did not catch this

<!-- pick what applies -->
- [ ] Missing scenario (edge case not covered)
- [ ] Wrong assertion (test too weak or wrong expected value)
- [ ] Over-mocked (real integration path never exercised)
- [ ] Wrong layer (tested unit but bug was in composition / API / CSS)
- [ ] No test for this symbol yet
- [ ] Other: ...

## Tests to add

| File | Test name | What to assert |
|------|-----------|----------------|
| | | |

## Fix scope (minimal)

<!-- files changed; what was intentionally not refactored -->
