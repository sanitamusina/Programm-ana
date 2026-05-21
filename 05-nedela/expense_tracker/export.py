
import csv

def export_to_csv(expenses, filename):
    if not expenses:
        return 0

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        # Kolonnu nosaukumi
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])

        # Ieraksti rindās
        for e in expenses:
            writer.writerow([e["date"], f"{e['amount']:.2f}", e["category"], e["description"]])

    return len(expenses)
