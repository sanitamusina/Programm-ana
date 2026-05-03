def A_dala():
    naudas_vienibas = [5, 10, 25, 50, 100, 200, 250]
    naudas_vienibas.append(500)
    naudas_vienibas.remove(25)
    naudas_vienibas.pop(5)
    naudas_vienibas.insert(2,20)
    print(naudas_vienibas)
    print(naudas_vienibas[:3])
    print(naudas_vienibas[-2:])
    print(naudas_vienibas[::2])


    kopsumma = 0
    skaits = 0
    for skaitlis in naudas_vienibas:
        kopsumma = kopsumma + skaitlis
        skaits = skaits + 1
    vidējā_vērtība = kopsumma / skaits
    print ("Kopējā skaitļu summa ir:", kopsumma)
    print ("Vidējā skaitļu summa ir:", vidējā_vērtība)

    kopsumma = sum(naudas_vienibas)
    skaits = len(naudas_vienibas)
    print("Kopsumma ar sum() funkciju ir:", kopsumma)
    print("Skaits ar len() funkciju ir:", skaits)

    skaitlu_virkne = [3,6,8,34,54,55,67,76,79,81,84,86,87,90,91,93,97,100]
    para_skaitli = []
    for skaitlis in skaitlu_virkne:
        if skaitlis % 2 == 0:
            para_skaitli.append(skaitlis)
    print("Pāra skaitļu virkne ir:", para_skaitli)
    pirmie_tris = skaitlu_virkne[ :3]
    pedejie_divi = skaitlu_virkne[-2: ]
    katrs_otrais = skaitlu_virkne[ : :2]
    print("Pirmie trīs skaitļi ir:", pirmie_tris)
    print("Pēdējie divi skaitļi ir:", pedejie_divi)
    print("Katrs otrais skaitlis ir:", katrs_otrais)

def B_dala():
    Studenti = {"Anna": 86, "Inese": 75, "Juris": 59, "Kārlis": 60, "Ina": 94}
    Studenti["Ilze"] = 49
    Studenti["Anna"] = 55
    Studenti["Toms"] = 71
    print(Studenti)

    for name, grade in Studenti.items():
        print(f"Students {name} - atzīme {grade}")

    
    max_grade = 0
    best_student = ""
    for name, grade in Studenti.items():
        if grade > max_grade:
            max_grade = grade
            best_student = name
    print(f"Lielākā atzīme {max_grade} ir studentam: {best_student}")


def C_dala():
    Studenti = [{"name": "Jānis", "grade": 77}, {"name": "Pēteris", "grade": 88}, {"name": "Juris", "grade": 99}, {"name": "Ieva", "grade": 100}]
    for students in Studenti:
        if students["grade"] >= 80:
            print(f"Students {students['name']}, atzīme - {students['grade']}")

    for i, students in enumerate(Studenti):
        print(f"{i+1}. {students["name"]} - {students["grade"]}")


if __name__ == "__main__":
    izvele = input("Ievadi A, B vai C: ")

    if izvele == "A":
        A_dala()
    elif izvele == "B":
        B_dala()
    elif izvele == "C":
        C_dala()
    else:
        print("Nepareiza izvēle")
