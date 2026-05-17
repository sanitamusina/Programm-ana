
# Izdevumu izsekotājs – plāns

## A Programmas apraksts
Programma ļauj ievadīt sistēmā veiktos pirkumus - pirkuma datumu, preču nosaukumu, cenu, daudzumu, kopā iztērēto naudu, kategoriju, kādā ietilpst konkrētais pirkums.
Vēlāk no sistēmas var eksportēt uz csv failu dažāda  veida atskaites par to, kurā datumā kas nopirkts, cik daudz naudas iztērēts konkrētā mēnesī vai konkrētām preču kategorijām.

## B Datu struktūra
Katrs izdevums būs vārdnīca ar:
- datumu
- preces nosaukumu
- preces cenu
- kopā iztērēto summu par konkrēto preci
- preces kategoriju

{"date": "22.02.2025.","product": "Zefīrs","amount": 2.50,"price": 3.44,"category": "Saldumi"}

Kopā pirkumu saraksts būs saraksts ar vairākām šādām vārdnīcām.
Pirkumi: ({"date": "22.02.2025.","product": "Zefīrs","amount": 2.50,"price": 3.41,"category": "Saldumi"}, {"date": "13.05.2025.","product": "Kartupeļi","amount": 1.50,"price": 0.80,"category": "Pārtika"})



piemēram: 
22.12.2025. Saldējums 3 1.25 Saldumi
02.02.2026. Elektrība 202 0.23 Komunālie maksājumi

Izvēlējos šādu formu, jo man labāk patīk šāds datums, nekā uzdevumā ieteiktais YYYY.MM.DD, un tas ietver visus uzdevumā nepieciešamos kritērijus.
Vārdnīca - jo konkrētā pirkumā nopirktas konkrētas lietas, kas pieder konkrētai kategorijai, par konkrētu cenu un konkrēts daudzums.
Saraksts ar vārdnīcām - jo vienā reizē var tikt nopirktas dažādas preces.

## C Moduļu plāns

- app.py – lietotāja izvēlne - lietotājs pasaka, ko vēlas no programmas - vai ievadīt kādu informāciju, vai lai sistēma parāda kādu jau ievadīto informāciju.
- storage.py – JSON faili - ielādē un saglabā tos.
- logic.py – filtrēšana, grupēšana un summas aprēķins - formulas.
- export.py – eksportē datus uz CSV failu.
- expenses.json - fails, kas izveidojas automātiski un saglabā izdevumu sarakstu

- plan.md - sākotnējais darba plāns
- DEVLOG.md - izstrādes žurnāls

- README.md - projekta dokumentācija

## D Lietotāja scenāriji
Lietotājs ievada pirkumus, programma tos pārbauda, vai korekti ievadīti un saglabā json failā.
Lietotājs filtrē ievadītos pirkumus pēc mēnešiem - prasa sistēmai parādīt, piem., tikai janvārī veiktos pirkumus - sistēma parāda sarakstu ar tikai janvārī veiktajiem pirkumiem.
Lietotājs prasa, lai sistēma izvada kopā par saldumiem iztērēto naudas summu - sistēma sarēķina, cik daudz naudas kopā iztērēts tieši saldumos un izvada kopsummu.
Lietotājs eksportē CSV failu - pieprasītās atskaites iespējams atvērt ecxel failā.


## E Robežgadījumi
- Ja expenses.json fails neeksistē, sistēma izvada tukšu pirkumu sarakstu: return[].
- Ja lietotājs ievada negatīvu summu, sistēma izmet paziņojumu: "Daudzumam un cenai jābūt pozitīviem skaitļiem".
- Ja lietotājs ievada tukšu aprakstu, sistēma izmet paziņojumu: "Ievadi pirkuma datumu, preces nosaukumu, cenu un kategoriju".
- Ja lietotājs ievada nepareizu datumu, sistēma izmet paziņojumu: "Datums jāievada formātā: DD.MM.YYYY.".
- Ja saraksts ir tukšs un lietotājs izvēlas "parādīt", tad sistēma izmet paziņojumu: "Pirkumu nav".
