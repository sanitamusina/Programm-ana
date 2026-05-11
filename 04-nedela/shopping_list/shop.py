import sys
from storage import load_shopping_list, save_shopping_list

def add_item(product, price):
    shopping_list = load_shopping_list()
    shopping_list.append({"product": product, "price": price})
    save_shopping_list(shopping_list)
    print(f"✓ Pievienots: {product} ({price:.2f} EUR)")

def list_shopping_list():
    shopping_list = load_shopping_list()
    if not shopping_list:
        print("Iepirkumu saraksts ir tukšs.")
        return
    print("Iepirkumu saraksts:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item['product']} — {item['price']:.2f} EUR}")


def total_sum():
    items = load_shopping_list()
    total = sum(item["price"] for item in items)
    print(f"Kopā: {total:.2f} EUR")


def clear_list():
    save_shopping_list([])
    print("Iepirkumu saraksts ir iztukšots.")   

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("  python shop.py add <produkts> <cena>")
        print("  python shop.py list")
        print("  python shop.py total")
        print("  python shop.py clear")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        product = sys.argv[2]
        price = float(sys.argv[3])
        add_item(product, price)

    elif command == "list":
        list_shopping_list()

    elif command == "total":
        total_sum()

    elif command == "clear":
        clear_list()

    else:
        print("Nezināma komanda.")