# Projekta apraksts

Šajā projektā tika izveidoti vairāki faili - viens, kas glabā ievadītos izdevumus, otrs, kas komunicē ar lietotāju, piedāvājot dažādas izvēlnes - ko darīt, trešais rēķina izdevumu kopsummas pa mēnešiem vai kategorijām, un ceturtais eksportē izvēlētos izdevumus uz csv failu.
Lietotājs var pievienot izdevumus, apskatīt tos, filtrēt pēc mēneša, redzēt izmaksu kopsavilkumu pa kategorijām un eksportēt datus uz exceli.

# Uzstādīšana

```bash
git clone https://github.com/sanitamusina/Programm-ana.git
cd expense_tracker
python app.py
```

# Lietošana
programma piedāvā šādas komandas:

1) Pievienot izdevumu - lietotājs var ievadīt, kad, cik iztērējis un par ko
2) Parādīt visus izdevumus - programma parāda visus iepriekš ievadītos izdevumus ar datumu, summu, izdevumu kategoriju un aparkstu
3) Filtrēt izdevumus pēc mēneša - programma parāda tikai tos izdevumus, kas iztērēti izvēlētajā mēnesī
4) Kopsavilkums pa kategorijām - programma parāda, cik naudas iztērēts kopā konkrētajā izdevumu kategorijā
5) Dzēst izdevumu - lietotājam ir iespēja izdzēst kādu no ievadītajiem izdevumiem
6) Eksportēt izdevumus CSV failā - lietotājs izvēlas faila nosaukumu un eksportē izdevumus uz exceli
7) Iziet no programmas - programma beidz komunicēt ar lietotāju

# Autors
Sanita Musina un gudrais draugs-padomdevējs AI (M365 Copilot)