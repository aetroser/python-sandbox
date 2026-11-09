"""
KOLOKWIUM B — ZADANIE 1: Wczytywanie do zera
Tematyka: Wczytywanie do zera.
Źródło: Lab02/zad06.py; Lab03/zad01.py–zad02.py (względem Labs/ w Labs.zip).
Sugerowany czas: 10 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), while True, if i break: wczytywanie do wartości kończącej.
- n>0, n<0, n%2==0 i and: wybieranie kategorii.
- += 1 aktualizuje licznik, += n aktualizuje sumę.
- print(a,b,c): trzy wartości oddzielone spacjami.

Małe przykłady składni — nie są całym rozwiązaniem
    count = 0
    count += 1
    print(4 % 2 == 0)  # True
    print(count, 10, 0)  # 1 10 0

Inny sposób / wariant bez własnych funkcji
Nie trzeba definiować funkcji ani przechowywać danych w liście. sum() również nie jest potrzebna — sumę aktualizuj przy odczycie. Zero musi zakończyć analizę, zanim zostanie potraktowane jako dana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytuj po jednym int (-1000..1000) w kolejnych liniach aż do pierwszego 0; zero nie jest daną. Jest najwyżej 100 liczb przed zerem i zero zawsze występuje. Wypisz w jednej linii: liczbę dodatnich parzystych, ich sumę, liczbę liczb ujemnych. Dodatnie nieparzyste pomijaj. Liczb ujemnych nie dodawaj do sumy.

WEJŚCIE PRZYKŁADOWE
-2
4
3
6
-1
0

WYJŚCIE PRZYKŁADOWE
2 10 2

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
