"""Tester kolokwium A: stdout, komplet zadań i ocena 2.0–5.0.
Tematyka: narzędzie do sprawdzenia własnych programów z tego arkusza.
Źródło zadań: Lab02–Lab06; szczegóły w zad1.py–zad5.py.
Uruchom: python sprawdz.py; pomoc: python sprawdz.py --help.
Wymaga zachowania folderu ../../narzedzia. Python 3.10+, bez pakietów.
"""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "narzedzia"))
from sprawdzarka import main

if __name__ == "__main__":
    raise SystemExit(main(HERE))
