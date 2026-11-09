"""
DZIEŃ 3 — ZADANIE 06: Dodawanie dni i poniedziałki
Tematyka: Dodawanie dni i poniedziałki.
Źródło: Lab06/zad15.py–zad16.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: mondays(year) i plus_three_weeks(d). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date,timedelta: daty i odstępy czasu.
- date(year,1,1), d.year, d.weekday(): początek i sprawdzanie dnia.
- timedelta(days=1) / timedelta(days=7): przesuwanie o dzień/tydzień.
- timedelta(weeks=3) i timedelta(days=21): dwie formy tego samego odstępu.
- append() zbiera daty, d.isoformat() zwraca tekst RRRR-MM-DD.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date, timedelta
    d = date(2020, 8, 9)
    print((d + timedelta(days=2)).isoformat())  # 2020-08-11

Inny sposób / wariant bez własnych funkcji
Możesz przechodzić po każdym dniu i wybierać poniedziałki albo znaleźć pierwszy poniedziałek i iść co 7 dni. Nie trzeba pisać własnej obsługi długości miesięcy. Bez def można wykonać próbę, lecz końcowo pozostaw obie funkcje.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj rok (1900..2100). Funkcja mondays(year) zwraca listę dat wszystkich poniedziałków tego roku. Wypisz je po jednej w formacie ISO. Osobno zdefiniuj plus_three_weeks(d) i sprawdź zgodność dodania timedelta(weeks=3) i timedelta(days=21).

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024: pierwsza data 2024-01-01, ostatnia 2024-12-30; jest ich 53.

SPRAWDŹ TAKŻE
Rok zaczynający się innym dniem; nie wypisuj dat kolejnego roku; zmiana miesiąca.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
