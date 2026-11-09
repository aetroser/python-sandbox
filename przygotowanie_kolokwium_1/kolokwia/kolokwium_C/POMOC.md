# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad1.py

```text
KOLOKWIUM C — ZADANIE 1: Konwersja temperatury
Tematyka: Konwersja temperatury.
Źródło: Lab04/zad03.py (względem Labs/ w Labs.zip).
Sugerowany czas: 10 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input().upper(): C/F niezależnie od wielkości liter; int(input()): temperatura.
- if/else i operatory *, /, +, -: wybranie kierunku i przeliczenie.
- print(f'{wynik:.2f}'): dokładnie dwie cyfry po kropce.
- round(wynik,2)==0 i przypisanie 0.0: normalizacja ujemnego zera.

Małe przykłady składni — nie są całym rozwiązaniem
    print('f'.upper())  # F
    value = 12.5
    print(f'{value:.2f}')  # 12.50

Inny sposób / wariant bez własnych funkcji
Nie potrzeba modułów ani własnych funkcji. c_to_f/f_to_c są opcjonalnym podziałem programu. Zamiast f-stringa możesz użyć format(wynik,'.2f'); samo round nie dopisuje zer na wyjściu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj w pierwszej linii literę C lub F (może być mała), w drugiej liczbę całkowitą -100..100. C oznacza, że wejście jest w Celsjuszach i należy przeliczyć je na Fahrenheity; F oznacza odwrotnie. F=C*9/5+32. Wypisz sam wynik z 2 miejscami po kropce. Zaokrąglone zero zapisuj 0.00.

WEJŚCIE PRZYKŁADOWE
c
20

WYJŚCIE PRZYKŁADOWE
68.00

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
```

## zad2.py

```text
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
```

## zad3.py

```text
KOLOKWIUM C — ZADANIE 3: Zestawienie sprzedaży
Tematyka: Zestawienie sprzedaży.
Źródło: Lab05/01 Data structures/05 - dicts.py; Lab06/zad02.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), input().split(): liczba rekordów i trzy pola.
- int(ilosc), int(cena), *: wartość jednego rekordu w groszach.
- Slownik {}, get(nazwa,0), przypisanie: sumy dla produktów.
- sorted(slownik): klucze alfabetycznie; sum(slownik.values()): łączna kwota.
- print(nazwa,kwota), print('SUMA',kwota): wymagane wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    name, quantity, price = 'kask 2 1250'.split()
    value = int(quantity) * int(price)
    print(name, value)  # kask 2500

Inny sposób / wariant bez własnych funkcji
Nie musisz definiować aggregate. Bez get() użyj if/in, a bez sum() gromadź kwotę w zmiennej. Wystarczą int — float nie jest tu potrzebny.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n linii "produkt ilosc cena". Produkt jest niepustym wyrazem z małych liter ASCII; ilosc i cena są int 0..10000. Cena to grosze za sztukę. Zsumuj ilosc*cena dla każdego produktu. Wypisz produkty alfabetycznie, po jednym wierszu "produkt wartosc_grosze". Zachowaj też produkty o sumie 0. Na końcu zawsze wypisz "SUMA wartosc_wszystkich_groszy". Nie przeliczaj na złote.

WEJŚCIE PRZYKŁADOWE
3
sok 2 350
chleb 1 400
sok 1 300

WYJŚCIE PRZYKŁADOWE
chleb 400
sok 1000
SUMA 1400

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
```

## zad4.py

```text
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
```

## zad5.py

```text
KOLOKWIUM C — ZADANIE 5: Najbliższe urodziny
Tematyka: Najbliższe urodziny.
Źródło: Lab05/03 Zadania (do przesłania)/zad08.py–zad09.py; Lab06/zad08.py, zad16.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): data odniesienia.
- map(int,input().split()): miesiąc i dzień; date(rok,miesiac,dzien): data urodzin w wybranym roku.
- Porównania dat < i >= oraz if: decyzja o bieżącym albo kolejnym roku.
- d.isoformat(): RRRR-MM-DD; (d-today).days: odległość w dniach.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    candidate = date(2020, 8, 9)
    print(candidate.isoformat())  # 2020-08-09
    print(candidate.year)  # 2020

Inny sposób / wariant bez własnych funkcji
Nie musisz tworzyć własnej funkcji do urodzin. Można też przesuwać datę timedelta(days=1) aż do szukanego miesiąca/dnia, ale konstrukcja daty w wybranym roku jest krótsza. Nie korzystaj z date.today().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj datę odniesienia RRRR-MM-DD (rok 1900..2099), następnie miesiąc i dzień urodzin jako dwa int w jednej linii. Taka data istnieje w każdym roku (wykluczamy 29 lutego). Znajdź najbliższe urodziny przypadające dziś albo później. Wypisz ich datę ISO i liczbę dni od daty odniesienia w jednej linii. Dziś oznacza różnicę 0. Nie korzystaj z daty systemowej.

WEJŚCIE PRZYKŁADOWE
2026-11-12
11 13

WYJŚCIE PRZYKŁADOWE
2026-11-13 1

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
```

