import sys
    
if len(sys.argv) < 2:
    print("Kļūda: nav norādīts N.")
    print("Lietošana: python fizzbuzz.py 15")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda: N nav vesels skaitlis.")
    print("Piemērs: python fizzbuzz.py 15")
    sys.exit(1)


noteikumi = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Jazz")
]

rezultati = []

for i in range(1, N + 1):
    out = ""
    for dalitajs, vards in noteikumi:
        if i % dalitajs == 0:
            out += vards
    if out == "":
        out = str(i)

    rezultati.append(out)

print(", ".join(rezultati))
