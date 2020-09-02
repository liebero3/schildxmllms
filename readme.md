# Wofür ist das gut?

Mithilfe des scripts lässt sich eine CSV für Logineo-LMS aus dem Logineo-XML-Export des Programms Schild erzeugen.

Die mithilfe der CSV erstellten User werden automatisch globalen Gruppen innerhalb von Logineo-LMS zugeordnet, die den Kurszugehörigkeiten in Schild entsprechen.

Auf diesem Weg lassen sich (die richtigen Einstellungen innerhalb Logineo-LMS vorausgesetzt) auch Gruppenzugehörigkeiten mithilfe der CSV ändern, dies ist bei normalen Moodleinstallationen nicht möglich (Feature von Eledia-Instanzen).

# Installation und Ausführung

dependencies installieren

```
pip install -r requirements.txt
```

script ausführen

```
schildxml2csv.py -i <schild.xml> -o <lms.csv>
```

# Vorgehen innerhalb von Logineo LMS

Einstellungen des Eledia-Blocks "globale Gruppen" anpassen

![Block: globale Gruppen](https://github.com/liebero3/schildxmllms/blob/master/images/globale-gruppen.png)

Obige Seite erreicht man Über

![Pfad zu globale Gruppen](https://github.com/liebero3/schildxmllms/blob/master/images/path_gl-gruppen.png)

Über Website-Administration / Nutzer / Nutzerkonten / Nutzerliste hochladen die mit dem script erstellte csv hochladen.

Beim Hochladen müssen müssen folgende Einstellungen vorgenommen werden:

![Einstellungen Upload](https://github.com/liebero3/schildxmllms/blob/master/images/upload_einstellungen.png)

# Wichtig!

ICH ÜBERNEHME KEINE VERANTWORTUNG, es handelt sich um ein "proof of concept"

# License:

Keine, tu was immer du willst damit.
