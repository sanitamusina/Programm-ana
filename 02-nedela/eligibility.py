age_input = input("Ievadi savu vecumu: ").strip()
car_licence_input = input("Vai tev ir autovadītāja apliecība? (jā/nē): ").strip().lower()
veteran_input = input ("Vai esi kara veterāns? (jā/nē): ").strip().lower()
student_input = input ("Vai esi students? (jā/nē): ").strip().lower()
True = "jā"
False = "nē"
if age_input >= "18":
print ("Tu esi pilngadīgs, tāpēc tu vari balsot.")
else:
    print ("Tu neesi pilngadīgs, tāpēc tu nevar balsot.")
If age_input >= "21" and car_licence_input == "jā":
    print ("Tu vari nomāt auto.")
elif age_input >= "21" and car_licence_input == "nē":
    print ("Tu nevari nomāt auto, jo tev nav autovadītāja apliecības")
elif age_input < "21" and car_licence_input == "jā"
    print ("Tu nevari nomāt auto, jo tu neesi pietiekami vecs.")
else print ("Tu nevari nomāt auto, jo tu neesi pietiekami vecs un tev nav autovadītāja apliecības.")

if age_input >=65 or veteran_input == "jā":
 print ("Tu vari saņemt seniora atlaidi")
else: print ("Tu nekvalificējies seniora atlaidei")

if 16 <=age_input <= 26 and student_input == "jā":
    print ("Tu vari saņemt studentu atlaidi")
    elif 16 <=age_input <= 26 and student_input == "nē":
        print ("Tu nevari saņemt studentu atlaidi, jo tu neesi students.")
    elif age_input < 16 or age_input > 26 and student_input == "jā":
        print ("Tu nevari saņemt studentu atlaidi, jo tu neesi vecumā no 16 līdz 26 gadiem.")
    else: print ("Tu nevari saņemt studentu atlaidi, jo tu neesi vecumā no 16 līdz 26 gadiem un tu neesi students.")