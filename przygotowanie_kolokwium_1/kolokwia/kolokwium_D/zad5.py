"""
KOLOKWIUM D — ZADANIE 5: Suma pól prostokątów
Tematyka: Suma pól prostokątów.
Źródło: Lab04/zad07.py–zad08.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- map(int,input().split()): granice i liczba części.
- /, *, **, +: szerokość, punkt i pole prostokąta.
- range(n) albo while: dokładnie n lewych końców.
- suma += pole albo sum(...): dodawanie; f'{wynik:.4f}': 4 miejsca.
- round(wynik,4)==0 i wynik=0.0: normalizacja zera.

Małe przykłady składni — nie są całym rozwiązaniem
    for i in range(3):
        print(i)  # kolejne wiersze: 0, 1, 2
    print(f'{1.25:.4f}')  # 1.2500

Inny sposób / wariant bez własnych funkcji
Nie musisz tworzyć własnej rectangle_sum ani osobnej funkcji f(x). Bez sum() użyj zmiennej i +=. Nie trzeba żadnego modułu do całkowania; wykonujesz tylko opisaną sumę działań.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj w jednej linii całkowite a b n, -10<=a<b<=10 i 1<=n<=1000. Dla f(x)=x**2 podziel przedział [a,b] na n równych części szerokości h=(b-a)/n. Oblicz sumę n prostokątów h*f(a+i*h), gdzie i=0,...,n-1 (lewe końce części). Wypisz sumę z dokładnie 4 miejscami po kropce. Nie trzeba znać rachunku całkowego: wystarczy policzyć wskazaną sumę. Zaokrąglone zero zapisuj 0.0000.

WEJŚCIE PRZYKŁADOWE
0 2 2

WYJŚCIE PRZYKŁADOWE
1.0000

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
