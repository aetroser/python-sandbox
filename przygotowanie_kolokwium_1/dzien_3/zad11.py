"""
DZIEŃ 3 — ZADANIE 11: Reguły i zbiory objawów jako dane
Tematyka: Reguły i zbiory objawów jako dane.
Źródło: Lab06/zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: classify(tokens). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(): lista tokenów, set(tokens): zbiór bez powtórzeń.
- 'token' in symptoms: obecność; == porównuje całe zbiory.
- if/elif/else oraz and/not: wyrażanie reguł, od bardziej szczegółowych.
- return 'NAPIS' zwraca etykietę, print(...) wypisuje wynik funkcji.

Małe przykłady składni — nie są całym rozwiązaniem
    tokens = set('a b a'.split())
    print('a' in tokens)  # True
    print(tokens == {'a', 'b'})  # True

Inny sposób / wariant bez własnych funkcji
Zamiast set() możesz użyć trzech zmiennych bool oznaczających obecność tokenów. Moduły nie są potrzebne. Reguły można przetestować bez def, ale końcowo classify pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
To wyłącznie ćwiczenie reguł tekstowych. Wczytaj jedną linię tokenów: goraczka, miesnie, oslabienie; pusta linia dozwolona. Powtórzenia ignoruj. Funkcja classify(tokens) zwraca GRYPA dla wszystkich trzech; PRZEZIEBIENIE dla goraczka i oslabienie bez miesnie; PRZETRENOWANIE dla samego miesnie; OK dla pustego zbioru lub samego oslabienie; INNE dla pozostałych kombinacji. Wypisz wynik. Nie jest to narzędzie medyczne.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
goraczka oslabienie miesnie -> GRYPA; miesnie -> PRZETRENOWANIE.

SPRAWDŹ TAKŻE
Sprawdź wszystkie 8 możliwych podzbiorów trzech tokenów; reguła szczegółowa przed ogólną.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
