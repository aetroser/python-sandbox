"""
KOLOKWIUM A — ZADANIE 3: Malejące trójki z nakładaniem
Tematyka: Malejące trójki z nakładaniem.
Źródło: Lab05/03 Zadania (do przesłania)/zad03.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): lista; pusta linia daje [].
- len(), range() lub while, indeksy i porównanie a>b>c: pełne okna.
- Wycinek data[i:i+3] oraz print(*okno): wypisanie elementów okna.
- Zmienna bool albo lista wyników pozwala ustalić, czy trzeba wypisać BRAK.

Małe przykłady składni — nie są całym rozwiązaniem
    data = [11, 8, 5, 2]
    print(*data[1:4])  # 8 5 2
    print(8 > 5 > 2)  # True

Inny sposób / wariant bez własnych funkcji
Własna funkcja i gromadzenie wyników w liście nie są obowiązkowe; możesz wypisywać trafienia podczas przeglądania. Bez wycinków odczytaj trzy sąsiednie indeksy osobno.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię zawierającą od 0 do 100 int (-100..100). Znajdź wszystkie trzy sąsiadujące elementy a>b>c. Okna mogą się nakładać. Wypisz każdą trójkę w osobnej linii w kolejności indeksu początku, elementy rozdziel spacjami. Nie usuwaj powtarzających się trójek w różnych miejscach. Jeśli brak, wypisz BRAK.

WEJŚCIE PRZYKŁADOWE
5 4 3 2 1

WYJŚCIE PRZYKŁADOWE
5 4 3
4 3 2
3 2 1

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
