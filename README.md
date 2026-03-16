# Kleiner Tax Optimizer von Stefan

Ein Python-basiertes System zur automatisierten Berechnung von Kapitalertragsteuern nach dem FIFO-Prinzip (First-In-First-Out). 

Das Skript identifiziert steuerliche Optimierungspotenziale wie Tax-Loss-Harvesting, um ungenutzte Verluste vor Jahresende (z.B. im Dezember) zu realisieren und so die Steuerlast auf Kursgewinne zu senken.


# Was kann das Script:
FIFO-Accounting
Tax-Loss-Harvesting
Automatisierte Tests
Einlesen von externen Positionen


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