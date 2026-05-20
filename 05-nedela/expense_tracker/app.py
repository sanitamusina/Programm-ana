from datetime import date, datetime
from storage import load_expenses, save_expenses

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Apģērbs un apavi", "Našķi", "Higiēna"]

def add_expense(expenses):
    today = date.today()

    today_display = today.strftime("%d.%m.%Y")
    today_storage = today.strftime("%Y-%m-%d")

    user_input = input(f"Datums (DD.MM.YYYY) [{today_display}]: ")

    if user_input:
        try:
            data = datetime.strptime(user_input, "%d.%m.%Y")
            stored_date = data.strftime("%Y-%m-%d")
        except ValueError:
            print("Kļūda: datums jāievada formātā DD.MM.YYYY")
            return
    else:
        stored_date = today_storage

    amount = float(input("Summa EUR: "))

    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
   
    cat = CATEGORIES[int(input("Izvēlies kategoriju: ")) - 1]

    description = input("Apraksts: ")

    expenses.append({"date": stored_date, "amount": amount, "category": cat, "description": description})
    save_expenses(expenses)
    
    display_date = datetime.strptime(stored_date, "%Y-%m-%d").strftime("%d.%m.%Y")
    print(f"✓ Pievienoti izdevumi ({display_date}, {amount:.2f} EUR, {cat}, {description})")

def main():
    expenses = load_expenses()
    while True:
        print("\n1) Pievienot\n2) Parādīt\n3) Iziet")
        choice = input("> ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            if not expenses:
                print("Nav neviena izdevuma.")
                continue

            print(f"{'Datums':<12} | {'Summa (EUR)':>12} | {'Kategorija':<12} | Apraksts")
            print("-" * 80)

            for expense in expenses:
                date_raw = expense["date"]
                amount = expense["amount"]
                category = expense["category"]
                description = expense["description"]

                display_date = datetime.strptime(date_raw, "%Y-%m-%d").strftime("%d.%m.%Y")

                print(f"{display_date:<12} | {amount:>12.2f} | {category:<12} | {description}")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
