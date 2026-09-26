# 🧪 Daily mini-projects

Small, **finished**, tested tools that complement the Finance Management
System. One folder per day — each is a complete, shippable unit.

## Rules

1. Folder name: `day-NN-short-name` (e.g. `day-02-budget-calculator`).
2. Every project **must** contain:
   - `README.md` — what / why / how to run / example output
   - source file(s)
   - `test_*.py` (Python) or equivalent tests
   - sample data if relevant
3. Tests run in CI (`projects-tests` job) — keep them green.
4. Prefer stdlib-only dependencies so anyone can run them in 2 minutes.

## Index

| Day | Project | Stack | What it does |
|-----|---------|-------|--------------|
| 01 | [`day-01-csv-expense-parser`](day-01-csv-expense-parser/) | Python | Parse a bank CSV export → monthly + category totals, budget alerts |

## Suggest the next one

Open a [feature request](../../issues/new?template=feature_request.md) with the
`projects/` checkbox ticked. Ideas live in [`ROADMAP.md`](../ROADMAP.md) Week 3.
