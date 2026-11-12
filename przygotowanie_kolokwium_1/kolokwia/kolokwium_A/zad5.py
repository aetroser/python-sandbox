"""
Kol. A.5: Wiek i różnica dat | Lab05, Lab06
Wczytaj datę urodzenia i odniesienia (ISO, pierwsza≤druga); wypisz pełne lata oraz różnicę dni.
Własne funkcje opcjonalne; 29.02 w zwykłym roku → urodziny 1.03; dnia początkowego nie doliczaj.
Wejście/próba: 2000-11-13 / 2026-11-13
Wynik: 26 9496
Przydatne: from datetime import date; fromisoformat(), .year/.month/.day, porównania, (koniec-start).days.
"""

# Tutaj napisz swoje rozwiązanie.

from datetime import date

data_urodzenia, data_odniesienia = map(date.fromisoformat, input().split())

wiek = data_odniesienia.year - data_urodzenia.year - ((data_odniesienia.month, data_odniesienia.day) < (data_urodzenia.month, data_urodzenia.day))
roznica_dni = (data_odniesienia - data_urodzenia).days

print(wiek, roznica_dni)