# Impfstatus Fortschritt Twitter Bot

## Allgemeine Infos

Der Account Impfstatus Fortschritt [@impf_progress](https://twitter.com/impf_progress) tweetet einmal täglich den Anteil der geimpften deutschen Bevölkerung und stellt diese mit einem Fortschrittsbalken dar. Inspiriert ist die Darstellung durch den Twitter Account [@year_progress](https://twitter.com/year_progress). 

Die Darstellung der grauen Kästchen mag etwas seltsam erscheinen, und bei gewissen Prozentzahlen überlappen und falsch erscheinen. Die gewählte Darstellung ist etwas "grob", es gibt nur 15 Abstufungen. Etwa alle 6-7 % füllt sich ein weiteres Stück Balken (schaut euch @year_progress kurz an oder hier [meine Erklärung mit Screenshots](https://twitter.com/imbstt/status/1369054005461147658)).

## Datenquelle

Ich nutze als Datenquelle die Daten von [impfdashboard.de](https://impfdashboard.de/), einem Angebot des Bundesministeriums für Gesundheit. Die Rohdaten sind im unteren Teil der Seite verlinkt, oder direkt hier abrufbar: [https://impfdashboard.de/daten](https://impfdashboard.de/daten)

Prozentwerte und Zahlen auf dem Impfdashboard werden außer Sonntags und an Feiertagen täglich aktualisiert und als maschinenlesbare TSV-Tabellen (Tab-separierte Tabellen im Textformat) zur Verfügung gestellt. Diese Daten können zum Beispiel in Microsoft Excel, LibreOffice Calc oder einem Texteditor geöffnet und eingelesen werden. 

## Tweet-Zeitplan

Der Twitter Bot wird zwischen 12 und 18 Uhr stündlich ausgeführt und prüft dann beim Impfdashboard auf neue Daten. Es wird nicht getweetet, wenn die Zahlen sich zum vorherigen Tweet nicht oder nur geringfügig ändern. Dabei wird auf die erste Nachkommastelle des Prozentwertes gerundet.

Der tägliche Aktualisierungszeitpunkt des Impfdashboard schwankt etwas, und somit auch die Uhrzeit des täglichen Tweets. Meistens werden bis 12 Uhr die neuen Daten für den vorherigen Tag veröffentlicht, hin und wieder dauert es etwas länger. 

## Autor

Der Bot wird als Hobbyprojekt betrieben von [@imbstt](https://twitter.com/imbstt) und ist kein Angebot des Bundesministeriums für Gesundheit, des RKI oder anderer staatlicher oder öffentlicher Stellen.

Der Code Open Source und auf Github einsehbar: [https://github.com/imbstt/impf-progress-bot](https://github.com/imbstt/impf-progress-bot)

## Mehr Details, Prognosen, Herdenimmunität?

Ich möchte den Bot simpel halten und die Darstellung nicht verändern. 

Im Folgenden sind einige weitere Bots und Accounts gelistet, die die Impfzahlen ebenfalls bereitstellen, ggf. etwas anders aufbereitet. Einige Accounts versuchen Vorhersagen zu treffen, diese sind meiner Meinung nach mit mit Vorsicht zu genießen. 

Diese Accounts werden von anderen Personen betrieben und sind unabhängig entstanden.

### Deutschland

* [@impfstatus](https://twitter.com/impfstatus) 
* [@ImpfStatusGER](https://twitter.com/ImpfStatusGER) 
* [@BotImpf](https://twitter.com/BotImpf)
* [@GermanyProgress](https://twitter.com/GermanyProgress)
* [@impftracker](https://twitter.com/impftracker)
* [@CoronaBot_DEU](https://twitter.com/CoronaBot_DEU)
* [@VaccinesGermany](https://twitter.com/VaccinesGermany/) (Englisch)
* [@impffortschritt](https://twitter.com/impffortschritt)

### Belgien

* [@VacBotBE](https://twitter.com/VacBotBE)

### Österreich

* [@jaukerlbot](https://twitter.com/jaukerlbot) 
* [@impfbot](https://twitter.com/impfbot)

### Schweiz

* [@ImpfstatusS](https://twitter.com/ImpfstatusS)

### USA

* [@vax_progress](https://twitter.com/vax_progress)

### Vereinigtes Königreich

* Es finden sich einige Accounts über die [Twitter Personensuche zu #ukvaccine](https://twitter.com/hashtag/ukvaccine?src=hashtag_click&f=user)
