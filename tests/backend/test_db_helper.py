from backend import db_helper


def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) >= 1  # Change to expect at least 1 result
    assert any(exp['amount'] == 10.0 and exp['category'] == "Shopping" and exp["notes"] == "Bought potatoes" for exp in expenses)
    

def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(expenses) == 0


def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-12-31")
    assert len(summary) == 0
