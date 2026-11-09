"""
KOLOKWIUM B — ZADANIE 3: Unikalne pary kwadratów
Tematyka: Unikalne pary kwadratów.
Źródło: Lab06/zad01.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())), len(), range(): dane i sąsiednie indeksy.
- **2: kwadrat liczby; (a,b): para jako krotka.
- set(), in, add(): zbiór widzianych par; lista append() lub wypisywanie od razu zachowuje kolejność.
- print(a,b): para bez nawiasów.

Małe przykłady składni — nie są całym rozwiązaniem
    pair = (-4, 16)
    print(pair[0] ** 2 == pair[1])  # True
    print(*pair)  # -4 16

Inny sposób / wariant bez własnych funkcji
square_pairs jest opcjonalna. Bez set() użyj listy już znalezionych par i testu not in. Nie sortuj zbioru wyników, bo polecenie wymaga kolejności pierwszego wystąpienia.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię 0..100 int (-100..10000). Znajdź sąsiadujące pary (a,b), dla których b=a**2. Pary mogą się nakładać. Wypisz każdą różną parę tylko raz, w kolejności pierwszego wystąpienia, po jednej w linii. Przy braku BRAK. (-2,4) i (2,4) to różne pary.

WEJŚCIE PRZYKŁADOWE
2 4 2 4 -2 4

WYJŚCIE PRZYKŁADOWE
2 4
-2 4

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
