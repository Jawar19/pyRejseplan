# AGENTS

This file helps coding agents work effectively in this repository.

## Project Snapshot

- Python package: `py_rejseplan`
- Source root: [`src/py_rejseplan`](src/py_rejseplan)
- Tests root: [`tests`](tests)
- Build/release config: [`pyproject.toml`](pyproject.toml)

## Fast Start Commands

- Create/sync environment: `uv sync --dev`
- Run tests (default): `pytest`
- Run tests that avoid live auth calls: `pytest -m "not auth_req"`
- Lint: `ruff check .`
- Format: `ruff format .`
- Build package: `uv build` (or `python -m build`)

## Repo-Specific Pitfalls

- Some tests require a valid API key and are marked `auth_req` in [`pyproject.toml`](pyproject.toml).
- Auth key fixture reads `rejseplan.key` in repo root; expected line format is `KEY: <token>` in [`tests/conftest.py`](tests/conftest.py).
- If `rejseplan.key` is missing, tests may fall back to `DUMMY_KEY`; do not assume live API behavior in that case.
- Ignore generated artifacts in [`build`](build) and `dist` when making code changes.

## Architecture Boundaries

- API clients live in [`src/py_rejseplan/api`](src/py_rejseplan/api).
- XML-backed models live in [`src/py_rejseplan/dataclasses`](src/py_rejseplan/dataclasses).
- Custom exception hierarchy lives in [`src/py_rejseplan/exceptions`](src/py_rejseplan/exceptions).

When implementing API changes:

1. Update API client behavior in [`src/py_rejseplan/api`](src/py_rejseplan/api).
2. Keep XML parsing and model validation in [`src/py_rejseplan/dataclasses`](src/py_rejseplan/dataclasses).
3. Raise package exceptions from [`src/py_rejseplan/exceptions`](src/py_rejseplan/exceptions) rather than raw `requests` exceptions.

## Testing Guidance

- Keep unit tests near current patterns in:
  - [`tests/dataclasses`](tests/dataclasses)
  - [`tests/depatures`](tests/depatures)
  - [`tests/exceptions`](tests/exceptions)
- Prefer fixture-driven tests (`conftest.py`) over duplicated setup.
- For network-facing changes, include both:
  - one isolated test with mocked HTTP behavior
  - one integration-style test marked `auth_req` when relevant

## Release Notes

- Release automation script: [`scripts/release.ps1`](scripts/release.ps1)
- CI publish workflow: [`.github/workflows/build_release.yml`](.github/workflows/build_release.yml)
- Tag format expected by workflow: `v<major>.<minor>.<patch>`

## Working Style Expectations For Agents

- Make minimal, targeted changes.
- Do not modify generated output under [`build`](build) unless explicitly requested.
- Run `pytest` and `ruff check .` before finalizing when changes affect runtime behavior.
- Prefer links to existing docs/files over duplicating long explanations.