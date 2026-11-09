"""
DZIEŃ 3 — ZADANIE 03: Wiek w pełnych latach
Tematyka: Wiek w pełnych latach.
Źródło: Lab05/03 Zadania (do przesłania)/zad08.py; Lab06/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: how_old(birth,today). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date i date.fromisoformat(input()): odczyt obu dat.
- d.year, d.month, d.day: pola daty; - i if: obliczenia i korekta pełnych lat.
- Porównanie krotek (miesiąc,dzień): najpierw miesiąc, przy równości dzień.
- return zwraca int; print(wiek) wypisuje go bez formatowania dziesiętnego.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    d = date(2020, 8, 9)
    print(d.year, d.month, d.day)  # 2020 8 9
    print((2, 28) < (3, 1))  # True

Inny sposób / wariant bez własnych funkcji
Dwie pary pól możesz porównać zwykłymi warunkami zamiast krotek. Nie ma potrzeby date.today() ani dzielenia liczby dni przez 365. Rachunek można przetestować bez def, ale końcowo how_old jest wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja how_old(birth,today) przyjmuje dwie daty, birth<=today. Wczytaj je w dwóch liniach RRRR-MM-DD. Zwróć i wypisz liczbę pełnych lat. Rok zwiększa się w dniu urodzin. Dla 29 lutego w roku nieprzestępnym przyjmij zwiększenie wieku 1 marca. Nie używaj date.today() w tej wersji.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2000-11-13 oraz 2026-11-12 -> 25; dla 2026-11-13 -> 26.

SPRAWDŹ TAKŻE
Dzień przed urodzinami; dzień urodzin; narodziny dziś; 29 lutego.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
