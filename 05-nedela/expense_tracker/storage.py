import json
import os

FILE = "expense_tracker/expenses.json"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as fails:
        return json.load(fails)

def save_expenses(expenses):
    with open(FILE, "w", encoding="utf-8") as fails:
        json.dump(expenses, fails, ensure_ascii=False, indent=2)
