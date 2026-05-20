from collections import defaultdict
from datetime import datetime


def get_available_months(expenses):
    months = set()

    for expense in expenses:
        month = expense["date"][:7]  # 'YYYY-MM'
        months.add(month)

    return sorted(months)



def filter_by_month(expenses, year_month):
    return [e for e in expenses if e["date"].startswith(year_month)]


def sum_by_category(expenses):
    totals = defaultdict(float)

    for expense in expenses:
        totals[expense["category"]] += expense["amount"]

    return dict(totals)


def delete_expense(expenses, index):
    if index < 0 or index >= len(expenses):
        return None

    return expenses.pop(index)
