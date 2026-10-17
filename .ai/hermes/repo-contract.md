## Repository identity

- Repository: `/opt/ai/projects/agent-pipeline-test`
- Purpose: Small Python test repo for validating Hermes pipeline behavior.
- Risk: Low

## Allowed paths

Hermes workers may modify only:

- `app.py`
- `tests/`
- `README.md`
- `ARCHITECTURE.md`
- `PROJECT.md`
- `TODO.md`
- `.gitignore`
- `.ai/hermes/repo-contract.md`

## Forbidden paths

Hermes workers must not modify or access as implementation targets:

- `.git/`
- `.venv/`
- Secrets, tokens, or credentials
- Systemd configuration
- Docker production configuration
- Live Hermes configuration
- Files outside `/opt/ai/projects/agent-pipeline-test`

## Test command

```sh
.venv/bin/python -m pytest -q
```

## Review requirements

- All changes require review.
- Review must return PASS before a human creates a commit.
- Review must confirm that changes are limited to allowed paths and do not affect forbidden paths.
- Review must confirm that the required test command passes when tests are applicable.
- The tracked `.gitignore` must contain the exact rooted rule `/.ai/reviews/` before final review; other `.ai/` paths must remain visible to repository-state checks.

## Commit policy

Hermes workers must not commit. Human commits are allowed only after review PASS.

## Push policy

No push is allowed without explicit human approval.

## Rollback procedure

Prefer reverting the change. Do not use `git reset --hard` without explicit human approval.
