naudas_vienibas = [5, 10, 25, 50, 100, 200, 250]
naudas_vienibas.append(500)
naudas_vienibas.remove(25)
naudas_vienibas.pop(5)
naudas_vienibas.insert(2,20)
print(naudas_vienibas)
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