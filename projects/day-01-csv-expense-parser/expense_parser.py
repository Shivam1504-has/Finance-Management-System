"""Day 01 — CSV expense parser.

Reads a bank CSV export (date,description,category,amount) and prints:
monthly totals, per-category totals, top expenses, and a budget check.

Usage:
    python expense_parser.py expenses.csv --budget 2000 --top 3
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Expense:
    date: date
    description: str
    category: str
    amount: float


def parse_csv(path: str | Path) -> list[Expense]:
    """Parse expenses from a CSV file. Raises ValueError on bad rows."""
    expenses: list[Expense] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"date", "description", "category", "amount"}
        if set(reader.fieldnames or []) != required:
            raise ValueError(f"header must be exactly: {sorted(required)}")
        for i, row in enumerate(reader, start=2):
            try:
                expenses.append(
                    Expense(
                        date=date.fromisoformat(row["date"].strip()),
                        description=row["description"].strip(),
                        category=row["category"].strip() or "Uncategorized",
                        amount=float(row["amount"]),
                    )
                )
            except (ValueError, AttributeError) as e:
                raise ValueError(f"row {i}: invalid data ({e})") from e
            if expenses[-1].amount < 0:
                raise ValueError(f"row {i}: amount must be >= 0")
    return expenses


def monthly_totals(expenses: list[Expense]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for e in expenses:
        totals[e.date.strftime("%Y-%m")] += e.amount
    return dict(sorted(totals.items()))


def category_totals(expenses: list[Expense]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))


def top_expenses(expenses: list[Expense], n: int = 3) -> list[Expense]:
    return sorted(expenses, key=lambda e: e.amount, reverse=True)[:n]


def budget_status(total: float, budget: float) -> str:
    if total <= budget:
        pct = (total / budget * 100) if budget else 0
        return f"Budget check: OK — {total:.2f} / {budget:.2f} ({pct:.0f}%)"
    return f"Budget check: OVER BUDGET by {total - budget:.2f} ({total:.2f} / {budget:.2f})"


def report(expenses: list[Expense], budget: float, top_n: int = 3) -> str:
    lines: list[str] = []
    for month, total in monthly_totals(expenses).items():
        count = sum(1 for e in expenses if e.date.strftime("%Y-%m") == month)
        lines.append(f"Month {month}: total {total:.2f} across {count} transactions")
    lines.append("Top categories:")
    for cat, total in category_totals(expenses).items():
        lines.append(f"  {cat}: {total:.2f}")
    lines.append("Top expenses:")
    for e in top_expenses(expenses, top_n):
        lines.append(f"  {e.date} {e.description} ({e.category}): {e.amount:.2f}")
    lines.append(budget_status(sum(e.amount for e in expenses), budget))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse a CSV of expenses.")
    parser.add_argument("csv_file", help="path to expenses CSV")
    parser.add_argument("--budget", type=float, default=2000.0, help="monthly budget")
    parser.add_argument("--top", type=int, default=3, help="number of top expenses")
    args = parser.parse_args()
    print(report(parse_csv(args.csv_file), args.budget, args.top))


if __name__ == "__main__":
    main()
