"""
DZIEŃ 3 — ZADANIE 02: Dzień tygodnia po polsku
Tematyka: Dzień tygodnia po polsku.
Źródło: Lab06/zad06.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: day_of_week(d). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date; date.fromisoformat(text): zamiana tekstu RRRR-MM-DD na datę.
- d.weekday(): numer dnia 0..6 (0=poniedziałek).
- Lista lub krotka polskich nazw i indeksowanie [numer]: wybór nazwy.
- input(), return, print(): odczyt, zwrot nazwy, wypisanie.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    d = date.fromisoformat('2020-01-06')
    print(d.weekday())  # 0, czyli poniedziałek

Inny sposób / wariant bez własnych funkcji
Bez listy nazw można użyć if/elif dla numerów albo słownika. Nie trzeba definiować własnej funkcji konwertującej tekst na datę, bo jest fromisoformat. Wymagana własna funkcja day_of_week ma zwracać polski napis.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja day_of_week(d) przyjmuje datetime.date i zwraca małymi literami polską nazwę dnia: poniedziałek,...,niedziela. Wczytaj poprawną datę RRRR-MM-DD i wypisz nazwę. Skorzystaj z weekday; nie polegaj na języku systemu operacyjnego.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024-01-01 -> poniedziałek; 2024-01-07 -> niedziela.

SPRAWDŹ TAKŻE
weekday numeruje od 0; isoweekday od 1; luty roku przestępnego.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
