KM_TO_MI = 0.621371
KG_TO_LBS = 2.20462 
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020 

print("Vienību konvertors")
print("1) Kilometri ↔ Jūdzes")
print("2) Kilogrami ↔ Mārciņas")
print("3) Litri ↔ Galoni")
print("4) USD ↔ EUR")
choice = input("Izvēlies konversiju (1-4): ").strip()

direction = input("Virziens (1 = uz priekšu, 2 = atpakaļ): ").strip()

raw_value = input("Ievadi vērtību: ").strip()

try:
    value = float(raw_value.replace(",", "."))
except ValueError:
    print("Kļūda: jāievada skaitlis (piem., 10 vai 1.73).")
    raise SystemExit

if choice == "1":
    coef = KM_TO_MI
    unit_a = "km"
    unit_b = "mi"
elif choice == "2":
    coef = KG_TO_LBS
    unit_a = "kg"
    unit_b = "lbs"  
elif choice == "3":
    coef = L_TO_GAL
    unit_a = "L"
    unit_b = "gal"
elif choice == "4":
    coef = USD_TO_EUR
    unit_a = "USD"
    unit_b = "EUR"
else:
    print("Kļūda: jāizvēlas 1, 2, 3 vai 4.")
    raise SystemExit

if direction == "1":
    result = value * coef
    print(f"{value:.2f} {unit_a} = {result:.2f} {unit_b}")
elif direction == "2":
    result = value / coef
    print(f"{value:.2f} {unit_b} = {result:.2f} {unit_a}")
else:
    print("Kļūda: virziens jāizvēlas 1 vai 2.")

