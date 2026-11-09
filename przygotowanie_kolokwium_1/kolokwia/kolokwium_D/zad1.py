"""
KOLOKWIUM D — ZADANIE 1: Statystyka liczb pierwszych
Tematyka: Statystyka liczb pierwszych.
Źródło: Lab03/zad05.py (względem Labs/ w Labs.zip).
Sugerowany czas: 10 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): lista; for/while: przegląd liczb i dzielników.
- %, ==, if: test podzielności; warunek n<2 odrzuca wartości niepierwsze.
- Licznik += 1 i suma += n: zliczanie z uwzględnieniem powtórzeń.
- Opcjonalnie math.isqrt(n) wyznacza całkowitą granicę sprawdzania dzielników.

Małe przykłady składni — nie są całym rozwiązaniem
    print(21 % 7)  # 0
    print(23 % 7)  # 2
    import math
    print(math.isqrt(30))  # 5

Inny sposób / wariant bez własnych funkcji
Własna is_prime pomaga uporządkować kod, ale nie jest wymagana. Bez math użyj warunku d*d<=n albo sprawdzaj więcej dzielników. Nie zamieniaj wejścia na set(), bo powtórzenia liczb pierwszych mają się liczyć.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię 0..100 int (-100..1000). Zlicz wszystkie elementy będące liczbami pierwszymi, zachowując ich wielokrotność. Wypisz liczność i sumę w jednej linii. Liczby mniejsze niż 2 nie są pierwsze. Pusta lista daje 0 0.

WEJŚCIE PRZYKŁADOWE
-2 0 1 2 3 4 3 9

WYJŚCIE PRZYKŁADOWE
3 8

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
