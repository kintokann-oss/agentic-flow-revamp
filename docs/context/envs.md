# Environment variables

> **Slot:** `context.envs` · **Rules:** [rules-backend.md](../rules/rules-backend.md), [rules-frontend.md](../rules/rules-frontend.md) · **Writers:** be-dev, fe-dev

## How to use this file

- **Section heading:** `## <app-name>` (logical app id from profile paths)
- Document vars before merging code that reads them

---

## api

| key | required | description | used_in_files |
|-----|----------|-------------|---------------|
| DATABASE_URL | no | Override SQLite file path | `@profile:paths.backend_root/src/db.py` |

## web-react

| key | required | description | used_in_files |
|-----|----------|-------------|---------------|
| VITE_API_URL | no | Backend base URL (default localhost:8000) | `@profile:paths.frontend_root/src/api/info.ts` |

---

## Example format (generic — not in this repo)

| key | required | description | used_in_files |
|-----|----------|-------------|---------------|
| FEATURE_FLAG_X | no | Enables experimental UI panel | `@profile:paths.frontend_root/src/components/DetailPanel/DetailPanel.tsx` |
