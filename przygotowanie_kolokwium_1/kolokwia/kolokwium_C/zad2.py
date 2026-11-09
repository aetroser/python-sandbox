"""
KOLOKWIUM C — ZADANIE 2: Nieparzyste, potem parzyste
Tematyka: Nieparzyste, potem parzyste.
Źródło: Lab06/zad19.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())) albo set(map(...)): wejście, również puste.
- set(): unikalne liczby; %2: parzystość; sorted(): porządek rosnący.
- Dwie listy i + albo sorted(...,key=...): połączenie grup w zadanej kolejności.
- print(*wynik), if not wynik: jedna linia lub PUSTA.

Małe przykłady składni — nie są całym rozwiązaniem
    print(sorted({4, 1, 4, -2}))  # [-2, 1, 4]
    print([1, 3] + [2, 4])  # [1, 3, 2, 4]

Inny sposób / wariant bez własnych funkcji
Bez def i bez lambda: zbuduj oddzielnie dwie grupy zwykłymi pętlami, posortuj i połącz. Bez set() usuń duplikaty testem in przed dopisaniem do listy.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię zawierającą 0..100 int (-100..100). Usuń duplikaty. Wypisz jedną linię: nieparzyste rosnąco, a następnie parzyste rosnąco; liczby oddziel spacją. Dla pustego wejścia wypisz PUSTA. Zero jest parzyste.

WEJŚCIE PRZYKŁADOWE
7 2 3 2 -1 0

WYJŚCIE PRZYKŁADOWE
-1 3 7 0 2

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
