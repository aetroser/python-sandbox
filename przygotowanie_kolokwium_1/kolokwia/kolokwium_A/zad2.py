"""
KOLOKWIUM A — ZADANIE 2: Rozwiązania równania kwadratowego
Tematyka: Rozwiązania równania kwadratowego.
Źródło: Lab03/zad08.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- map(int,input().split()), **, *, /: współczynniki i wzory.
- import math; math.sqrt(d): pierwiastek dla d>=0; if/elif/else: przypadki delty.
- sorted([x,y]) albo porównanie i zamiana: rosnąca kolejność.
- f'{x:.2f}': 2 cyfry; round(x,2)==0 pozwala rozpoznać wynik zaokrąglający się do zera.

Małe przykłady składni — nie są całym rozwiązaniem
    import math
    print(math.sqrt(36))  # 6.0
    x = -0.0001
    if round(x, 2) == 0:
        x = 0.0
    print(f'{x:.2f}')  # 0.00

Inny sposób / wariant bez własnych funkcji
Własna real_roots jest opcjonalna. Bez sorted() porównaj dwa pierwiastki. Bez math.sqrt można obliczyć d**0.5 dla nieujemnego d; nie używaj ^. Sama funkcja round nie zastępuje formatowania .2f.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj całkowite a b c (-100..100), a!=0. Rozwiąż a*x**2+b*x+c=0 w liczbach rzeczywistych. W pierwszej linii wypisz liczbę różnych pierwiastków: 0, 1 lub 2. Potem wypisz każdy pierwiastek w osobnej linii rosnąco, z dokładnie 2 miejscami po kropce. Jeśli wynik po zaokrągleniu do 2 miejsc jest zerem, wypisz 0.00 zamiast -0.00. Nie wypisuj dodatkowej linii przy braku pierwiastków.

WEJŚCIE PRZYKŁADOWE
1 -3 2

WYJŚCIE PRZYKŁADOWE
2
1.00
2.00

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
