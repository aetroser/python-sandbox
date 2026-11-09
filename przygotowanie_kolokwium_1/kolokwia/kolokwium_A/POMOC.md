# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad1.py

```text
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
```

## zad2.py

```text
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
```

## zad3.py

```text
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
```

## zad4.py

```text
KOLOKWIUM A — ZADANIE 4: Statystyka słów
Tematyka: Statystyka słów.
Źródło: Lab03/zad06.py; Lab05/02 Strings (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input(), replace(znak,' '), lower(), split(): przygotowanie tekstu.
- Słownik {}, get(word,0) lub if/in: liczenie słów.
- len(lista) i len(slownik): liczby słów i różnych słów.
- max(slownik.values()) oraz min()/sorted() lub pętla porównawcza: zwycięzca z remisem.
- print(slowo,licznik): ostatni wiersz dla niepustych danych.

Małe przykłady składni — nie są całym rozwiązaniem
    print('X,Y'.replace(',', ' ').lower().split())  # ['x', 'y']
    counts = {'bus': 2}
    print(counts.get('car', 0))  # 0

Inny sposób / wariant bez własnych funkcji
Możesz pisać bez def i bez Counter z dodatkowego modułu. Bez get() użyj if. Bez max/min ustal najlepszy wynik pętlą, porównując najpierw liczność, a przy remisie napis.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj linię tekstu długości 0..1000. Zastąp każdy znak z zestawu ,.!?;: spacją, zamień tekst na małe litery, a potem podziel split(). Innych znaków nie usuwaj. Wypisz w osobnych liniach: liczbę wszystkich słów; liczbę różnych słów; najczęstsze słowo i jego liczność rozdzielone spacją. Przy remisie wybierz słowo alfabetycznie najmniejsze według porządku Pythona. Gdy nie ma słów, trzecia linia to BRAK.

WEJŚCIE PRZYKŁADOWE
Kot, pies! KOT pies ala.

WYJŚCIE PRZYKŁADOWE
5
3
kot 2

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
KOLOKWIUM A — ZADANIE 5: Wiek i różnica dat
Tematyka: Wiek i różnica dat.
Źródło: Lab05/03 Zadania (do przesłania)/zad08.py; Lab06/zad07.py–zad08.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): dwie daty.
- .year, .month, .day: pola do wyznaczenia pełnych lat.
- Porównywanie par (miesiąc,dzień), odejmowanie lat, if: uwzględnienie terminu urodzin.
- (koniec-poczatek).days: dokładna liczba dni; print(wiek,dni): jeden wiersz.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    a = date.fromisoformat('2020-01-01')
    b = date.fromisoformat('2020-01-10')
    print((b-a).days)  # 9

Inny sposób / wariant bez własnych funkcji
how_old i osobna funkcja różnicy dat są opcjonalne. Zamiast porównania krotek użyj warunków na miesiącu i dniu. Nie zastępuj pełnych lat dzieleniem przez 365; datetime zajmuje się liczeniem dni za Ciebie.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj datę urodzenia, następnie datę odniesienia, każdą w osobnej linii RRRR-MM-DD. Daty poprawne, lata 1900..2100, urodzenie nie później niż data odniesienia. Wypisz pełny wiek w latach oraz liczbę dni pomiędzy datami w jednej linii. Dnia początkowego nie doliczaj. Dla urodzonych 29 lutego w nieprzestępnym roku wiek zwiększa się 1 marca. Nie korzystaj z daty systemowej.

WEJŚCIE PRZYKŁADOWE
2000-11-13
2026-11-13

WYJŚCIE PRZYKŁADOWE
26 9496

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
```

