"""
DZIEŃ 3 — ZADANIE 04: Różnica dni i pełne tygodnie
Tematyka: Różnica dni i pełne tygodnie.
Źródło: Lab06/zad08.py, zad13.py; Lab05/03 Zadania (do przesłania)/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: date_distance(start,end). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): daty wejściowe.
- end-start daje timedelta; (end-start).days daje podpisaną liczbę dni.
- abs(liczba) to wartość bezwzględna, // oznacza dzielenie całkowite.
- return dni,tygodnie zwraca krotkę; print(*wynik) wypisuje dwie liczby.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    span = date(2020, 1, 10) - date(2020, 1, 1)
    print(span.days)  # 9
    print(abs(-9) // 7)  # 1

Inny sposób / wariant bez własnych funkcji
Zamiast abs() można zmienić znak ujemnej liczby warunkiem if. Odejmowania dat nie trzeba implementować ręcznie. Wariant bez własnej funkcji jest możliwy, lecz końcowa wersja wymaga date_distance.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja date_distance(start,end) zwraca krotkę: podpisana różnica dni end-start oraz liczba pełnych tygodni w bezwzględnej różnicy dni. Wczytaj dwie daty, wypisz dwie liczby. Nie doliczaj dnia początkowego.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024-01-01 i 2024-01-16 -> 15 2. Zamiana dat -> -15 2.

SPRAWDŹ TAKŻE
Ta sama data; 6 i 7 dni; przejście przez 29 lutego.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
