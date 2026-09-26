"""Tests for the day-01 CSV expense parser."""

import pytest

from expense_parser import (
    budget_status,
    category_totals,
    monthly_totals,
    parse_csv,
    top_expenses,
)

CSV = "sample_expenses.csv"


def test_parse_count_and_total():
    expenses = parse_csv(CSV)
    assert len(expenses) == 8
    assert sum(e.amount for e in expenses) == pytest.approx(1587.50)


def test_monthly_totals():
    assert monthly_totals(parse_csv(CSV)) == {"2026-09": pytest.approx(1587.50)}


def test_category_totals_sorted_desc():
    totals = category_totals(parse_csv(CSV))
    assert totals["Rent"] == pytest.approx(800.00)
    assert totals["Groceries"] == pytest.approx(520.00)
    assert list(totals.values()) == sorted(totals.values(), reverse=True)


def test_top_expenses():
    top = top_expenses(parse_csv(CSV), 2)
    assert [e.amount for e in top] == [pytest.approx(800.00), pytest.approx(320.00)]


def test_budget_status_ok_and_over():
    assert "OK" in budget_status(1587.50, 2000.00)
    assert "OVER BUDGET" in budget_status(1587.50, 1000.00)


def test_bad_header_raises(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text("a,b,c\n1,2,3\n")
    with pytest.raises(ValueError, match="header"):
        parse_csv(bad)


def test_negative_amount_raises(tmp_path):
    bad = tmp_path / "neg.csv"
    bad.write_text("date,description,category,amount\n2026-09-01,x,Food,-5\n")
    with pytest.raises(ValueError, match="amount"):
        parse_csv(bad)
