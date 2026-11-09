"""
DZIEŃ 2 — ZADANIE 09: Zbiory i deterministyczna kolejność
Tematyka: Zbiory i deterministyczna kolejność.
Źródło: Lab05/01 Data structures/10 - set.py; Lab05/03 Zadania (do przesłania)/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: unique_char_count(text) w osobnej części; program zbiorów może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- set(map(int,input().split())): zbiór liczb; pusta linia daje pusty zbiór.
- A | B: suma zbiorów, A & B: część wspólna, A - B: różnica.
- sorted(wynik) i print(*wynik): stała kolejność liczb na wyjściu.
- set(text) zawiera różne znaki, len(zbior) liczy elementy.

Małe przykłady składni — nie są całym rozwiązaniem
    a = {1, 3}
    b = {3, 5}
    print(sorted(a & b))  # [3]
    print(len(set('aba ')))  # 3, bo spacja również jest znakiem

Inny sposób / wariant bez własnych funkcji
Operacje można zastąpić pętlami i testami in, a unikalne znaki zbierać w liście. Nie jest potrzebny żaden moduł; jednak użycie set jest tu właściwym tematem do przećwiczenia. Zostaw wymaganą unique_char_count.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwie linie liczb int (pusta linia oznacza zbiór pusty). Wypisz w 3 liniach sumę zbiorów, część wspólną i różnicę A-B. W każdej linii liczby rosnąco, bez duplikatów; dla pustego wyniku BRAK. Osobno zdefiniuj unique_char_count(text), licząc także spacje i rozróżniając duże litery.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
A: 1 2 2 3; B: 2 4. Wynik: 1 2 3 4 / 2 / 1 3.

SPRAWDŹ TAKŻE
Dwa puste zbiory; A=B; unikalne znaki to liczba różnych znaków, a nie tylko tych występujących raz.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
