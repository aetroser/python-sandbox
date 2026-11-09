# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad1.py

```text
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
```

## zad2.py

```text
KOLOKWIUM D — ZADANIE 2: Trójki bez powtórnego użycia elementów
Tematyka: Trójki bez powtórnego użycia elementów.
Źródło: Lab05/03 Zadania (do przesłania)/zad04.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())), len(), indeksowanie: odczyt i pełne okna.
- while z indeksem: przesunięcie zależne od wyniku.
- a>b>c, if/else, +=1 lub +=3: warunek i przesunięcia.
- print(*data[i:i+3]): wypisanie okna bez nawiasów; flaga trafienia: BRAK.

Małe przykłady składni — nie są całym rozwiązaniem
    i = 2
    i += 3
    print(i)  # 5
    print(*[9, 6, 3])  # 9 6 3

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz własnych funkcji ani listy wyników, jeśli wypisujesz trójki podczas przeglądania. Bez wycinka wypisz trzy elementy osobno. Do zmiennego przesunięcia użyj while, a nie zmieniania i wewnątrz for z range().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię 0..100 int (-100..100). Skanuj od lewej okna trzech sąsiadów. Jeśli a>b>c, wypisz trójkę i przesuń początek za te trzy elementy. Jeśli warunek nie jest spełniony, przesuń początek o jeden. Każdą znalezioną trójkę wypisz w osobnej linii; przy braku BRAK. Nie wolno ponownie użyć pozycji należącej do już wybranej trójki.

WEJŚCIE PRZYKŁADOWE
1 9 8 7 6 5 4

WYJŚCIE PRZYKŁADOWE
9 8 7
6 5 4

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
KOLOKWIUM D — ZADANIE 3: Aktualizacja książki telefonicznej
Tematyka: Aktualizacja książki telefonicznej.
Źródło: Lab05/01 Data structures/05 - dicts.py–07 - in_keyword.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), input().split(), range(): odczyt wpisów i zapytań.
- book={}, book[name]=number: dodanie albo zastąpienie numeru.
- book.get(name,'BRAK') albo if name in book: wyszukiwanie.
- len(book) liczy różne klucze; print('WPISY',len(book)): końcowy wiersz.
- Numer pozostaje str, aby zachować zera.

Małe przykłady składni — nie są całym rozwiązaniem
    book = {'Ewa': '0007'}
    book['Ewa'] = '0012'
    print(book['Ewa'])  # 0012
    print(len(book))  # 1

Inny sposób / wariant bez własnych funkcji
Możesz napisać całość bez def. Metodę get() można zastąpić warunkiem if/in. Nie trzeba sortować książki, bo wypisujesz odpowiedzi w kolejności zapytań, a nie wszystkie wpisy.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n linii "imie numer". Imię to wyraz ASCII bez spacji; numer to niepusty tekst cyfr (zachowaj zera). Kolejny wpis o tym samym imieniu zastępuje poprzedni numer. Następnie wczytaj q (0..100) i q imion, każde osobno. Dla każdego zapytania wypisz aktualny numer lub BRAK. Na końcu wypisz "WPISY k", gdzie k to liczba różnych imion w książce. Wielkość liter ma znaczenie.

WEJŚCIE PRZYKŁADOWE
3
Ala 001
Ola 222
Ala 003
3
Ala
Ola
Jan

WYJŚCIE PRZYKŁADOWE
003
222
BRAK
WPISY 2

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
KOLOKWIUM D — ZADANIE 4: Progi punktowe z Lab06
Tematyka: Progi punktowe z Lab06.
Źródło: Lab06/zad09.py (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), map(int,input().split()), range(n): dane i rekordy.
- >, <= i if/elif/else: progi od najwyższego do najniższego.
- Procent: 100*punkty/maksimum; alternatywnie porównuj 100*punkty > prog*maksimum.
- Licznik +=1 dla wyniku co najmniej 3; print('ZALICZONE',licznik): podsumowanie.

Małe przykłady składni — nie są całym rozwiązaniem
    points, maximum, threshold = 7, 10, 60
    print(100 * points > threshold * maximum)  # True, bo 70% > 60%

Inny sposób / wariant bez własnych funkcji
Własna calculate_grade jest opcjonalna. Lista progów też nie jest wymagana — wystarczy if/elif. Porównanie iloczynów pozwala obejść obliczanie float i round(), bez zmiany ścisłości progów.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Ćwiczenie progów z laboratorium, odrębne od zasad oceny kolokwium. Wczytaj n (0..100), następnie n linii "punkty maksimum" z int 0<=punkty<=maksimum, 1<=maksimum<=1000. Dla każdego rekordu wypisz: 5 gdy wynik >80%, 4 gdy >60% i <=80%, 3 gdy >50% i <=60%, inaczej 2. Nie zaokrąglaj procentów przed porównaniem. Na końcu wypisz "ZALICZONE k", gdzie k jest liczbą rekordów z oceną co najmniej 3.

WEJŚCIE PRZYKŁADOWE
4
50 100
60 100
80 100
81 100

WYJŚCIE PRZYKŁADOWE
2
3
4
5
ZALICZONE 3

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
```

