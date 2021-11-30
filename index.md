# Impfstatus Fortschritt Twitter Bot

## Allgemeine Infos

Der Account Impfstatus Fortschritt [@impf_progress](https://twitter.com/impf_progress) tweetet einmal täglich den Anteil der geimpften deutschen Bevölkerung und stellt diesen mit einem Fortschrittsbalken dar. Inspiriert ist die Darstellung durch den Twitter Account [@year_progress](https://twitter.com/year_progress).

<p align="center">
  <img src="https://user-images.githubusercontent.com/83777889/144042044-b6627a03-f3a5-4bad-9037-5d5f206d30bf.png" alt="Screenshot eines Tweets von impf_progress vom 30. November 2021" />
</p>

Die Darstellung der grauen Kästchen mag etwas seltsam erscheinen, und bei gewissen Prozentzahlen überlappen und falsch erscheinen. Die gewählte Darstellung ist etwas "grob", es gibt nur 15 Abstufungen. Etwa alle 6-7 % füllt sich ein weiteres Stück Balken.

## Datenquelle

Ich nutze als Datenquelle die vom Robert Koch-Institut bereitgestellte Daten, zu finden auf Github im Repository ["COVID-19-Impfungen in Deutschland"](https://github.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland/blob/master/Aktuell_Deutschland_Impfquoten_COVID-19.csv). Diese Daten werden unter der [CC-BY 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de) Lizenz veröffentlicht.

Prozentwerte und Zahlen werden außer Sonntags und an Feiertagen täglich aktualisiert und als maschinenlesbare CSV-Tabellen zur Verfügung gestellt. Diese Daten können zum Beispiel auch in Microsoft Excel, LibreOffice Calc oder einem Texteditor geöffnet und eingelesen werden. 

Bis November 2021 wurden Daten von [impfdashboard.de](https://impfdashboard.de/) bezogen, einem Angebot des Bundesministeriums für Gesundheit. Die Datengrundlage ist hierbei ebenfalls das Robert Koch-Institut.

### Hinweise zur Impfquote

Die drei dargestellten Impfquoten werden jeweils an der Gesamtbevölkerung Deutschlands bemessen, siehe dazu auch die Hinweise des RKI und BfG:
- [Impfquotenmonitoring](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring), im Blatt "Erläuterungen"  
  >Die Impfquote "Gesamt" ist der Anteil aller bisher Geimpften in der Gesamtbevölkerung;
- [COVID-19-Impfungen in Deutschland#COVID-19 Impfquoten](https://github.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland#COVID-19-Impfquoten)
- [Zusammen gegen Corona: Impfquote](https://www.zusammengegencorona.de/impfen/logistik-und-recht/impfquote/)

## Tweet-Zeitplan

Der Twitter Bot wird zwischen 12 und 18 Uhr stündlich ausgeführt und prüft dann auf neue Daten. Es wird nicht getweetet, wenn die Zahlen sich zum vorherigen Tweet nicht geändert haben.

## Autor

Der Bot wird als Hobbyprojekt betrieben von [@imbstt](https://twitter.com/imbstt) und ist kein Angebot des Bundesministeriums für Gesundheit, des Robert Koch-Instituts oder anderer staatlicher oder öffentlicher Stellen.

Der Code ist Open Source und auf Github einsehbar: [https://github.com/imbstt/impf-progress-bot](https://github.com/imbstt/impf-progress-bot)

## Mehr Details, Prognosen, Herdenimmunität?

Ich möchte den Bot simpel halten und die Darstellung nicht verändern oder mit Prognosen erweitern. 

Zum Thema Herdenimmunität hat das Bundesministerium für Gesundheit auf der Webseite [Gemeinsam gegen Corona](https://www.zusammengegencorona.de/impfen/logistik-und-recht/impfquote/#id-62eceedb-5921-54a8-94dc-c1e162c8ff46) Informationen bereitgestellt.

Im Folgenden sind einige weitere Bots und Accounts gelistet, die die Impfzahlen ebenfalls bereitstellen, ggf. etwas anders aufbereitet. Einige Accounts versuchen Vorhersagen zu treffen, diese sind meiner Meinung nach mit Vorsicht zu genießen. 

Diese Accounts werden von anderen Personen betrieben und sind unabhängig entstanden.

### Deutschland

* [@CoronaBot_DEU](https://twitter.com/CoronaBot_DEU)
* [@impfupdate](https://twitter.com/impfupdate) (Englisch)
* [@ImpfStatusGER](https://twitter.com/ImpfStatusGER) 
* [@GermanyProgress](https://twitter.com/GermanyProgress)
* [@impffortschritt](https://twitter.com/impffortschritt)

### Belgien

* [@VacBotBE](https://twitter.com/VacBotBE)

### Italien

* [@BVaccini](https://twitter.com/BVaccini)

### Österreich

* [@jaukerlbot](https://twitter.com/jaukerlbot) 

### Schweiz

* [@ImpfstatusS](https://twitter.com/ImpfstatusS)

### USA

* [@vax_progress](https://twitter.com/vax_progress)

### Vereinigtes Königreich

* Es finden sich einige Accounts über die [Twitter Personensuche zu #ukvaccine](https://twitter.com/hashtag/ukvaccine?src=hashtag_click&f=user)
