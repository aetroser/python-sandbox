# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad1.py

```text
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
```

## zad2.py

```text
KOLOKWIUM B — ZADANIE 2: Posortowane unikalne adresy
Tematyka: Posortowane unikalne adresy.
Źródło: Lab05/03 Zadania (do przesłania)/zad01.py–zad02.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), range(n), input(): odczyt n adresów.
- address.split('@')[1] i ==: dokładna domena.
- set(), add(), sorted(): różne adresy we wskazanej kolejności.
- len(wyniki) i pętla print(address): liczba oraz kolejne wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    address = 'name@example.net'
    print(address.split('@')[1])  # example.net
    items = set()
    items.add('x')
    items.add('x')
    print(len(items))  # 1

Inny sposób / wariant bez własnych funkcji
Bez własnych funkcji można wykonać całość wprost. Bez set() sprawdzaj, czy adres jest już na liście, i dopisuj tylko nowe. Sam test 'gmail.com' in address nie sprawdza dokładnej domeny.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n poprawnych adresów e-mail, każdy w osobnej linii. Adresy składają się z małych liter ASCII, cyfr i znaków . _ @; każdy ma dokładnie jedno @. Wybierz tylko domenę dokładnie gmail.com, usuń identyczne adresy i posortuj rosnąco całe adresy. W pierwszej linii wypisz ich liczbę, następnie każdy adres osobno. Dla pustego wyniku wypisz tylko 0.

WEJŚCIE PRZYKŁADOWE
4
b@gmail.com
a@gmail.com
b@gmail.com
x@notgmail.com

WYJŚCIE PRZYKŁADOWE
2
a@gmail.com
b@gmail.com

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
```

## zad4.py

```text
KOLOKWIUM B — ZADANIE 4: Średnia, mediana i moda z remisem
Tematyka: Średnia, mediana i moda z remisem.
Źródło: Lab06/zad03.py (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): liczby, import statistics: moduł.
- statistics.mean(), statistics.median(), statistics.multimode(): obliczenia.
- min(lista_mod): najmniejsza moda przy remisie.
- print(f'{x:.2f}'): średnia i mediana z 2 cyframi; modę wypisz bez .2f.
- round(x,2)==0 i x=0.0: zamiana zaokrąglonego ujemnego zera.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.multimode([6, 2, 6, 2]))  # [6, 2]
    print(min([6, 2]))  # 2
    print(f'{3.5:.2f}')  # 3.50

Inny sposób / wariant bez własnych funkcji
Możesz pisać bez def. Bez statistics policz średnią sum()/len(), medianę ze środkowych pozycji sorted(), a modę za pomocą słownika liczności. Nie musisz tworzyć własnych funkcji dla każdego z trzech obliczeń.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną niepustą linię 1..100 int (-1000..1000). Wypisz w 3 liniach średnią z 2 miejscami po kropce, medianę z 2 miejscami i modę jako int. Przy kilku modach wybierz najmniejszą wartość. Wolno używać modułu statistics. Jeśli zaokrąglony wynik jest zerem, wypisz 0.00.

WEJŚCIE PRZYKŁADOWE
4 1 4 1

WYJŚCIE PRZYKŁADOWE
2.50
2.50
1

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
KOLOKWIUM B — ZADANIE 5: Dzień tygodnia i luty
Tematyka: Dzień tygodnia i luty.
Źródło: Lab06/zad06.py, zad14.py, zad17.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): data z tekstu.
- d.weekday() daje 0..6; lista/krotka polskich nazw i [indeks] wybierają napis.
- import calendar; calendar.isleap(d.year): informacja o roku przestępnym.
- if/else: wybór liczby dni lutego; print(): dwa osobne wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    import calendar
    print(date(2020, 1, 6).weekday())  # 0
    print(calendar.isleap(2020))  # True

Inny sposób / wariant bez własnych funkcji
Nie musisz pisać day_of_week ani days_in_february. Bez isleap() użyj podzielności przez 4, 100 i 400. Bez listy nazw możesz użyć if/elif; nie polegaj na strftime('%A'), bo język nazwy zależy od ustawień systemu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj poprawną datę RRRR-MM-DD (rok 1900..2100). W pierwszej linii wypisz polską nazwę dnia tygodnia małymi literami z polskimi znakami (poniedziałek, wtorek, środa, czwartek, piątek, sobota, niedziela). W drugiej wypisz liczbę dni lutego w roku wczytanej daty. Nie korzystaj z języka systemu ani bieżącej daty.

WEJŚCIE PRZYKŁADOWE
2024-02-29

WYJŚCIE PRZYKŁADOWE
czwartek
29

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
```

