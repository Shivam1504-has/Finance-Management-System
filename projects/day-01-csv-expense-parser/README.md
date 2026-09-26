# Day 01 — CSV Expense Parser

Parse a bank/CSV export into **monthly totals, per-category totals,
top expenses, and budget alerts** — the same summaries the Flutter app
shows, as a tiny dependency-free Python tool.

## Run

```bash
python expense_parser.py sample_expenses.csv --budget 2000
```

Example output:

```
Month 2026-09: total 1587.50 across 8 transactions
Top categories:
  Groceries: 520.00
  Rent: 800.00
  Transport: 167.50
  Dining: 100.00
Top expenses:
  2026-09-01 Rent payment (Rent): 800.00
  2026-09-05 Groceries weekly (Groceries): 320.00
  2026-09-12 Groceries weekly (Groceries): 200.00
Budget check: OK — 1587.50 / 2000.00 (79%)
```

Force an alert demo:

```bash
python expense_parser.py sample_expenses.csv --budget 1000
# Budget check: OVER BUDGET by 587.50 (1587.50 / 1000.00)
```

## CSV format

Header row required: `date,description,category,amount`

- `date`: `YYYY-MM-DD`
- `amount`: positive number (expense)

## Test

```bash
pip install pytest
pytest -q
```
