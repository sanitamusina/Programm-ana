import os
import json

SHOPPING_FILE = "shopping.json"
PRICES_FILE = "prices.json"

def load_shopping_list(shopping_list_fails = 'shopping.json'):
    """Load shopping_list from the JSON file. If the file does not exist, return an empty list."""
    if not os.path.exists(shopping_list_fails):
        return []
    with open(shopping_list_fails, 'r', encoding='utf-8') as fails:
        return json.load(fails)

def save_shopping_list(saraksts_ar_iepirkumiem, iepirkumu_fails = 'shopping.json'):
    """Save the shopping list to the JSON file."""
    with open(iepirkumu_fails, 'w', encoding='utf-8') as kkk:
        json.dump(saraksts_ar_iepirkumiem,kkk, ensure_ascii=False, indent=2)

        
def load_prices(prices_file=PRICES_FILE):
    if not os.path.exists(prices_file):
        return {}
    with open(prices_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_prices(prices, prices_file=PRICES_FILE):
    with open(prices_file, 'w', encoding='utf-8') as f:
        json.dump(prices, f, ensure_ascii=False, indent=2)


def get_price(product):
    prices = load_prices()
    return prices.get(product)


def set_price(product, price):
    prices = load_prices()
    prices[product] = price
    save_prices(prices)
