
import random

while True:  # ārējais cikls – spēlēt vēlreiz
    slepenais_skaitlis = random.randint(1, 100)
    meginajumi = 0

    while True:  # viena spēle
        try:
            minejums = int(input("Mini skaitli no 1 līdz 100: "))
        except ValueError:
            print("Kļūda: Lūdzu, ievadi veselu skaitli no 1 līdz 100")
            continue

        meginajumi += 1

        if minejums < slepenais_skaitlis:
            print("Par mazu")
        elif minejums > slepenais_skaitlis:
            print("Par lielu")
        else:
            print(f"Pareizi! Tu uzminēji ar {meginajumi} mēģinājumiem.")
            break

        if meginajumi == 10:
            print("Pārāk daudz mēģinājumu. Tu zaudēji.")
            print(f"Pareizais skaitlis bija: {slepenais_skaitlis}")
            break

    atbilde = input("Vai gribi spēlēt vēlreiz? (jā / nē): ").lower()
    if atbilde != "jā":
        print("Paldies par spēli!")
        break
