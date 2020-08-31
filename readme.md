# Wofür ist das gut?

Mithilfe des scripts lässt sich eine CSV für Logineo-LMS aus dem Logineo-XML-Export des Programms Schild erzeugen.

Die mithilfe der CSV erstellten User werden automatisch globalen Gruppen innerhalb von Logineo-LMS zugeordnet, die den Kurszugehörigkeiten in Schild entsprechen.

Auf diesem Weg lassen sich (die richtigen Einstellungen innerhalb Logineo-LMS vorausgesetzt) auch Gruppenzugehörigkeiten mithilfe der CSV ändern, dies ist bei normalen Moodleinstallationen nicht möglich (Feature von Eledia-Instanzen).

# Installation

pip install -r requirements.txt

schildxml2csv.py -i schild.xml -o lms.csv

# Wichtig!

ICH ÜBERNEHME KEINE VERANTWORTUNG, es handelt sich um ein "proof of concept"
