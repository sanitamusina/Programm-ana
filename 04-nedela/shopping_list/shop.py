
import sys
from storage import (load_shopping_list, save_shopping_list, get_price, set_price)
from utils import calc_line_total, calc_grand_total, count_units


def ask_price():
    while True:
        try:
            price = float(input("Ievadi cenu: "))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Kļūda: cena jābūt pozitīvam skaitlim")

def add_item(product, qty):
    price = get_price(product)
    
    if price is not None:
        print(f"Atrasta cena: {price:.2f} EUR/gab.")
        choice = input("[A]kceptēt / [M]ainīt? ").strip().lower()

        
        if choice == "m":
            price = ask_price()
            set_price(product, price)
            print(f"✓ Cena atjaunināta: {product} → {price:.2f} EUR")


    else:
        print("Cena nav zināma.")
        price = ask_price()
        set_price(product, price)
        print(f"✓ Cena saglabāta: {product} ({price:.2f} EUR)")


    shopping_list = load_shopping_list()
    item = {"product": product, "qty": qty, "price": price}

    shopping_list.append(item)
    save_shopping_list(shopping_list)
    line_total = calc_line_total(item)
    print(f"✓ Pievienots: {product} x {qty} " f"({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

def list_shopping_list():
    shopping_list = load_shopping_list()
    if not shopping_list:
        print("Iepirkumu saraksts ir tukšs.")
        return
    print("Iepirkumu saraksts:")
    for i, item in enumerate(shopping_list, start=1):
        line_total = calc_line_total(item)
        print(f"  {i}. {item['product']} × {item['qty']} - " f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")



def total_sum():
    items = load_shopping_list()
    if not items:
        print("Kopā: 0.00 EUR (0 vienības, 0 produkti)")
        return
    total = calc_grand_total(items)
    units = count_units(items)
    products = len(items)
    print(f"Kopā: {total:.2f} EUR ({units} vienības, {products} produkti)")
     


def clear_list():
    save_shopping_list([])
    print("Iepirkumu saraksts ir iztukšots.")   

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("  python shop.py add <produkts> <daudzums>")
        print("  python shop.py list")
        print("  python shop.py total")
        print("  python shop.py clear")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Kļūda: add prasa 2 argumentus: nosaukums, daudzums")
            sys.exit(1)
        product = sys.argv[2]

        try:
            qty = int(sys.argv[3])
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Kļūda: daudzumam jābūt pozitīvam veselam skaitlim")
            sys.exit(1)
        add_item(product, qty)

    elif command == "list":
        list_shopping_list()

    elif command == "total":
        total_sum()

    elif command == "clear":
        clear_list()

    else:
        print("Nezināma komanda.")