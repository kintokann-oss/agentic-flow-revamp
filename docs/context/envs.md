# Environment variables

> **Slot:** `context.envs` · **Rules:** [rules-backend.md](../rules/rules-backend.md), [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** be-dev, fe-dev

## How to use this file

- **Read when:** be-dev or fe-dev needs to know required env vars for local run or tests
- **Write when:** A new env var is introduced — document before merging
- **Section heading:** `## <app-name>` (e.g. `api`, `web-react`)
- **Columns:**

| Column | Meaning |
|--------|---------|
| key | Environment variable name |
| required | `yes` or `no` |
| description | What it controls and default if unset |
| used_in_files | Source files that read this var |

- **Add a row:** 1. Add var to code 2. Add row under correct app section 3. Mention in plan or contract-summary if task-critical

---

## web-react

| key | required | description | used_in_files |
|-----|----------|-------------|---------------|
| VITE_API_URL | no | Backend base URL (default localhost:8000) | apps/web-react/src/api/info.ts, apps/web-react/src/api/toggleState.ts |

## api

| key | required | description | used_in_files |
|-----|----------|-------------|---------------|
| DATABASE_URL | no | SQLite path (`sqlite:///...`) — default `apps/api/data/app.db` | apps/api/src/db.py |
