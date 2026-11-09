"""
KOLOKWIUM C — ZADANIE 4: Jednoczesne rzuty: analiza danych
Tematyka: Jednoczesne rzuty: analiza danych.
Źródło: Lab02/zad08.py; Lab04/zad10.py (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- map(int,input().split()) odczytuje parametry, list(map(...)) odczytuje rundę.
- range(1,r+1): numery od 1; all(x==wartosc for x in runda) sprawdza zgodność wszystkich kości.
- Alternatywa: runda.count(wartosc)==n albo licznik z pętli.
- None jako brak wcześniejszego trafienia, if i zapamiętanie pierwszego wyniku.

Małe przykłady składni — nie są całym rozwiązaniem
    values = [5, 5, 5]
    print(all(x == 5 for x in values))  # True
    print(values.count(5))  # 3

Inny sposób / wariant bez własnych funkcji
Nie potrzeba własnej funkcji ani modułu random — dane są już podane. Bez all()/count() sprawdź elementy pętlą. Po znalezieniu pierwszego trafienia możesz tylko zapamiętać wynik i nie zmieniać go w kolejnych rundach.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n r w jednej linii (n=1..20 kości, r=0..100 rund). Następnie wczytaj r linii po n int 1..6; to gotowe rzuty, nie losuj własnych. Znajdź pierwszą rundę, w której WSZYSTKIE n kości mają 1 albo WSZYSTKIE mają 6. Wypisz numer rundy (od 1) i JEDYNKI lub SZOSTKI. Późniejsze rundy nie zmieniają odpowiedzi. Jeśli taka runda nie wystąpi, wypisz "r BRAK", podstawiając liczbę przeanalizowanych rund. Jedynki lub szóstki w różnych rundach nie łączą się.

WEJŚCIE PRZYKŁADOWE
3 4
1 1 2
6 6 6
1 1 1
2 2 2

WYJŚCIE PRZYKŁADOWE
2 SZOSTKI

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
