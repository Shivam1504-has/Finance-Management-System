# Contributing to Finance Management System

Thanks for your interest in contributing! 🎉 This project grows through small,
daily, reviewable contributions.

## Ways to contribute

- 🐛 Report bugs / suggest features via [Issues](../../issues)
- 💻 Fix a `good first issue`, improve docs, add tests
- 📦 Add a mini-project under `projects/` (see `projects/README.md`)
- 👀 Review open pull requests

## Ground rules

1. **One change per PR** — small PRs get reviewed and merged fast.
2. **Conventional commits**: `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`.
   Example: `feat: add monthly budget alert to dashboard`
3. **Tests required** for logic changes:
   - Flutter: `flutter test` must pass
   - Python mini-projects: `pytest -q` must pass
4. **Format before pushing**: `dart format .` in `flutter_app/`.
5. Never commit secrets (`.env`, `serviceAccountKey.json`, `google-services.json`).
6. Be kind — see [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Local setup

```bash
# Flutter app
cd flutter_app && flutter pub get && flutter analyze && flutter test

# Firebase scripts
cd firebase && npm install && for f in *.js; do node --check "$f"; done

# A mini-project
cd projects/day-01-csv-expense-parser && pip install pytest && pytest -q
```

## Branch & PR flow

1. Create a branch from `main`: `feat/short-name` or `fix/short-name`.
2. Commit with a conventional message.
3. Push and open a PR using the template checklist.
4. One approval + green CI = merge (squash).

## Adding a daily mini-project

Follow the template in [`projects/README.md`](projects/README.md):
`README + code + tests + sample data`. If CI is green and the README explains
*what / why / how to run*, it ships. 🚢
