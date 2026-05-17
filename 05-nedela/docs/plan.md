
# Izdevumu izsekotājs – plāns

## A Programmas apraksts
Programma ļauj ievadīt sistēmā izdevumus - tēriņu datumu, kopā iztērēto summu, kategoriju, kādā ietilpst konkrētie izdevumi un pirkuma aprakstu.
Vēlāk no sistēmas var eksportēt uz csv failu dažāda  veida atskaites par to, kurā datumā kas nopirkts, cik daudz naudas iztērēts konkrētā mēnesī vai pa konkrētām izdevumu kategorijām.

## B Datu struktūra
Katrs izdevums būs vārdnīca ar:
- datumu
- kopā iztērēto summu
- izdevumu kategoriju
- pirkuma aprakstu (kas tieši nopirkts)

{"date": "22.02.2025","amount": 3.88, "category": "Saldumi", "Description": Zefīri}

Kopā izdevumu saraksts būs saraksts ar vairākām šādām vārdnīcām.
Pirkumi: ({"date": "22.02.2025","amount": 3.88, "category": "Saldumi", "Description": "Zefīri"}, {"date": "29.05.2025","amount": 18.63, "category": "Higiēna", "Description": "Šampūns, zobu pasta, tualetes papīrs")

piemēram: 
22.12.2025 1.34 Saldumi Saldējums
02.02.2026 184.22 Komunālie maksājumi Elektrība 482 kW

Izvēlējos šādu formu, jo man labāk patīk šāds datums, nekā uzdevumā ieteiktais YYYY-MM-DD.
Izdevumi = vārdnīca - jo konkrētā datumā iztērēta konkrēta summa par konkrētām precēm, kas ietilpst konkrētā izdevumu kategorijā.
Izdevumu saraksts = saraksts ar vārdnīcām - jo vienā reizē var tikt iztērēta nauda par dažādām preču kategorijām.

## C Moduļu plāns

- app.py – lietotāja izvēlne - lietotājs pasaka, ko vēlas no programmas - vai ievadīt kādu informāciju, vai lai sistēma parāda kādu jau ievadīto informāciju.
- storage.py – darbs ar JSON failiem - sistēma ielādē (nolasa) un saglabā (pārraksta) tos.
- logic.py – filtrēšana, grupēšana un summas aprēķins - formulas.
- export.py – eksportē datus uz CSV failu.
- expenses.json - fails, kas izveidojas automātiski un saglabā izdevumu sarakstu

- plan.md - sākotnējais darba plāns
- DEVLOG.md - izstrādes žurnāls

- README.md - projekta dokumentācija

## D Lietotāja scenāriji
Lietotājs ievada izdevumus, programma tos pārbauda, vai korekti ievadīti un saglabā json failā.
Lietotājs filtrē ievadītos izdevumus pēc mēnešiem - prasa sistēmai parādīt, piem., tikai janvārī veiktos pirkumus - sistēma parāda sarakstu ar tikai janvārī veiktajiem pirkumiem.
Lietotājs prasa, lai sistēma izvada kopā par saldumiem iztērēto naudas summu - sistēma sarēķina, cik daudz naudas kopā iztērēts tieši saldumos un izvada kopsummu.
Lietotājs eksportē CSV failu - pieprasītās atskaites iespējams atvērt ecxel failā.


## E Robežgadījumi
- Ja expenses.json fails neeksistē, sistēma izvada tukšu pirkumu sarakstu: return[].
- Ja lietotājs ievada negatīvu summu, sistēma izmet paziņojumu: "izdevumu summai jābūt pozitīvam skaitlim".
- Ja lietotājs ievada tukšu aprakstu, sistēma izmet paziņojumu: "Ievadi izdevumu datumu, iztērēto summu, izdevumu kategoriju un aprakstu".
- Ja lietotājs ievada nepareizu datumu, sistēma izmet paziņojumu: "Datums jāievada formātā: DD.MM.YYYY".
- Ja saraksts ir tukšs un lietotājs izvēlas "parādīt", tad sistēma izmet paziņojumu: "Izdevumu nav".
