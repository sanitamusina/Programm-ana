

for N in range(1,16):
    if N % 3 == 0 and N % 5 == 0 and N % 7 == 0:
        print("FizzBuzzJazz", end=" ")
    elif N % 3 == 0 and N % 7 == 0:
        print("FizzJazz", end=" ")
    elif N % 5 == 0 and N % 7 == 0:
        print("BuzzJazz", end=" ")
    elif N % 3 == 0 and N % 5 == 0:
        print("FizzBuzz", end=" ")
    elif N % 3 == 0:
        print("Fizz", end=" ")
    elif N % 5 == 0:
        print("Buzz", end=" ")
    elif N % 7 == 0:
        print("Jazz", end=" ")   
    else:
        print(N, end=" ")




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
