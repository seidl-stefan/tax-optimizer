# Kleiner Tax Optimizer von Stefan

Ein Python-basiertes System zur automatisierten Berechnung von Kapitalertragsteuern nach dem FIFO-Prinzip (First-In-First-Out). 

Das Skript identifiziert steuerliche Optimierungspotenziale wie Tax-Loss-Harvesting, um ungenutzte Verluste vor Jahresende (z.B. im Dezember) zu realisieren und so die Steuerlast auf Kursgewinne zu senken.


## Kernfunktionen
* **FIFO-Accounting:** Korrekte steuerliche Behandlung von Wertpapiertranchen gemäß deutscher Rechtsprechung.
* **Tax-Loss-Harvesting:** Automatisierte Identifizierung von Positionen im Verlustbereich.
* **Szenario-Management:** Einlesen von externen Portfoliodaten und Marktpreisen über JSON-Dateien.
* **Qualitätssicherung:** Vollständige Abdeckung der Logik durch automatisierte Unit-Tests.


## Tech Stack
* **Sprache:** Python 3.x
* **Module:** `json` (Datenhandling), `unittest` (Testing)


## Repository klonen:**

```bash
# Repository klonen
git clone [https://github.com/seidl-stefan/tax-optimizer.git](https://github.com/seidl-stefan/tax-optimizer.git)

# Wechsle in den Ordner
cd tax-optimizer

# Führe das Skript oder den Test aus
python tax_engine.py
python test_tax_engine.py