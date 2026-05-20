from datetime import date, datetime
from storage import load_expenses, save_expenses

from logic import (get_available_months, filter_by_month, sum_by_category, delete_expense)


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
        print("\n1) Pievienot\n2) Parādīt\n3) Filtrēt pēc mēneša\n4) Kopsavilkums pa kategorijām\n5) Dzēst izdevumu\n6) Iziet")
        

        choice = input("> ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            if not expenses:
                print("Nav neviena izdevuma.")
                continue

        
        elif choice == "3":
            months = get_available_months(expenses)

            if not months:
                print("Nav izdevumu.")
                continue

            print("\nPieejamie mēneši:")
            for i, m in enumerate(months, 1):
                print(f"{i}) {m}")

            sel = input("Izvēlies mēnesi: ")
            if not sel.isdigit() or not (1 <= int(sel) <= len(months)):
                print("Nepareiza izvēle.")
                continue

            month = months[int(sel) - 1]
            filtered = filter_by_month(expenses, month)

            print(f"\n{month} izdevumi:")
            total = 0

            for e in filtered:
                total += e["amount"]
                print(f'{e["date"]} | {e["amount"]:6.2f} EUR | {e["category"]:<12} | {e["description"]}')

            print(f"Kopā: {total:.2f} EUR ({len(filtered)} ieraksti)")



        elif choice == "4":
            totals = sum_by_category(expenses)

            if not totals:
                print("Nav izdevumu.")
                continue

            print("\nKopsavilkums pa kategorijām:")
            for cat, total in totals.items():
                print(f"{cat:<12} | {total:8.2f} EUR")

        elif choice == "5":
            if not expenses:
                print("Nav izdevumu, ko dzēst.")
                continue
  
            print("\nIzdevumi:")
            for i, e in enumerate(expenses, 1):
                print(f'{i}) {e["date"]} | {e["amount"]:6.2f} EUR | {e["category"]:<12} | {e["description"]}')

            sel = input("Kuru dzēst? (numurs vai 0 lai atceltu): ")

            if sel == "0":
                continue

            if not sel.isdigit():
                print("Nepareiza ievade.")
                continue

            idx = int(sel) - 1
            deleted = delete_expense(expenses, idx)

            if deleted is None:
                print("Nepareizs numurs.")

            else:
                save_expenses(expenses)
                print(f'✓ Dzēsts: {deleted["date"]} | {deleted["amount"]:.2f} EUR | {deleted["category"]} | {deleted["description"]}')






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

