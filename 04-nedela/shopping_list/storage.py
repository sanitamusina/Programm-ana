import os
import json

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

def add_item(product, price):
    shopping_list = load_shopping_list()
    shopping_list.append({"product": product, "price": price})
    save_shopping_list(shopping_list)
    print(f"✓ Pievienots: {product} ({price})")