"""
KOLOKWIUM A — ZADANIE 1: Sumy i liczności w przedziale
Tematyka: Sumy i liczności w przedziale.
Źródło: Lab02/zad03.py; Lab03/zad01.py–zad04.py (względem Labs/ w Labs.zip).
Sugerowany czas: 10 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- map(int,input().split()): dwie liczby; min()/max() lub if i zamiana granic.
- range(lo,hi+1) albo while: przedział z oboma końcami.
- n%2, if/else oraz liczniki i sumy aktualizowane przez +=.
- print(licznik,suma): dwie wartości w wierszu.

Małe przykłady składni — nie są całym rozwiązaniem
    a, b = map(int, input().split())
    print(6 % 2)  # 0
    print(2, 14)  # 2 14

Inny sposób / wariant bez własnych funkcji
Możesz rozwiązać zadanie bez def, list i sum(): wystarczą cztery zmienne wyniku oraz pętla. Własne is_even albo funkcja licząca przedział są opcjonalne.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwa int a b (-1000..1000) w jednej linii. Rozważ wszystkie liczby z domkniętego przedziału między nimi, niezależnie od kolejności granic. Wypisz dwie linie: w pierwszej liczba parzystych i ich suma, w drugiej liczba nieparzystych i ich suma. Zero jest parzyste.

WEJŚCIE PRZYKŁADOWE
-2 3

WYJŚCIE PRZYKŁADOWE
3 0
3 3

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
