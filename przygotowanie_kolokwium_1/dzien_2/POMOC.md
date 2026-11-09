# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad01.py

```text
DZIEŃ 2 — ZADANIE 01: Indeksy i slicing
Tematyka: Indeksy i slicing.
Źródło: Lab05/01 Data structures/01 - lists.py; Lab05/02 Strings/03–07 (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input(): odczyt całego tekstu wraz ze spacjami; len(text): długość.
- text[index]: pojedynczy znak; text[start:stop:step]: wycinek, bez pozycji stop.
- Indeks -1 oznacza ostatni znak. // to dzielenie całkowite.
- Krok -1 odwraca kierunek; brak start i stop obejmuje cały napis.

Małe przykłady składni — nie są całym rozwiązaniem
    s = 'abcdefgh'
    print(s[1])     # b
    print(s[2:5])   # cde
    print(s[::3])   # adg
    print(s[::-1])  # hgfedcba

Inny sposób / wariant bez własnych funkcji
Nie są potrzebne moduły ani własne funkcje. Te same wybory znaków da się zbudować pętlą, ale tu przećwicz indeksowanie i wycinki. Nie stosuj strip(), jeśli chcesz zachować spacje wejściowe.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepusty napis długości co najmniej 4. Wypisz w osobnych liniach: pierwszy znak, ostatni, pierwszą połowę (len//2 znaków), co drugi znak od indeksu 0, napis odwrócony. Spacje są zwykłymi znakami.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Python: P / n / Pyt / Pto / nohtyP.

SPRAWDŹ TAKŻE
Długość parzysta i nieparzysta; ujemne indeksy; koniec wycinka nie należy do wyniku.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad02.py

```text
DZIEŃ 2 — ZADANIE 02: Kopia listy i współdzielenie danych
Tematyka: Kopia listy i współdzielenie danych.
Źródło: Lab05/01 Data structures/08 - basic operations on lists.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- a=[...]: lista; b=a: druga nazwa tego samego obiektu.
- a[:] albo a.copy(): płytka kopia listy; append(x): dopisanie na końcu.
- lista[i]=x: zmiana elementu; print(lista): reprezentacja z nawiasami.
- == porównuje zawartość, is sprawdza tożsamość obiektu; id(obiekt) może pomóc w obserwacji.

Małe przykłady składni — nie są całym rozwiązaniem
    a = [10, 20]
    b = a
    c = a.copy()
    print(a is b)  # True
    print(a is c)  # False

Inny sposób / wariant bez własnych funkcji
Wystarczą przypisania, wycinek i append; nie trzeba pisać def ani importować modułu. copy.deepcopy to inny rodzaj kopiowania i nie zastępuje obserwacji płytkiej kopii wymaganej w tym zadaniu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz a=[2,4,6], b=a i c=a[:]. Wykonaj b.append(8), następnie c[0]=99. Przed uruchomieniem zapisz przewidywane wartości a,b,c w komentarzu. Potem wypisz każdą listę w osobnej linii. W dodatkowej próbie z listą [[1],[2]] sprawdź, co robi płytka kopia, gdy modyfikujesz wewnętrzną listę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Pierwsza próba: [2, 4, 6, 8] / [2, 4, 6, 8] / [99, 4, 6].

SPRAWDŹ TAKŻE
Różnica przypisania i kopiowania; a==c i a is c oznaczają różne pytania.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad03.py

```text
DZIEŃ 2 — ZADANIE 03: Operacje na liście i indeksy wystąpień
Tematyka: Operacje na liście i indeksy wystąpień.
Źródło: Lab05/01 Data structures/02–03; Lab06/zad11.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): odczyt listy, int(input()): szukana wartość.
- enumerate(lista): pary (indeks,wartość); append(): zbieranie pasujących indeksów.
- x in lista: bezpieczne sprawdzenie przed lista.remove(x), które usuwa pierwsze wystąpienie.
- sorted(lista): posortowana kopia; print(*lista): liczby bez nawiasów.
- if not lista: przypadek pustego wyniku.

Małe przykłady składni — nie są całym rozwiązaniem
    for index, value in enumerate([10, 20]):
        print(index, value)  # wiersze: 0 10 oraz 1 20
    print(*[6, 8])  # 6 8, bez nawiasów

Inny sposób / wariant bez własnych funkcji
Zamiast enumerate możesz użyć for i in range(len(lista)) albo while z indeksem. Usunięcie można wykonać przez znalezienie indeksu i del lista[i]. Własne funkcje są opcjonalne.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepustą listę int z jednej linii i x z drugiej. Wypisz indeksy wszystkich x albo BRAK. Następnie usuń tylko pierwsze wystąpienie x, jeśli istnieje, i wypisz pozostałe elementy albo PUSTA. W trzeciej linii wypisz posortowaną kopię po usunięciu. Nie zmieniaj kolejności oryginalnych pozostałych elementów w drugiej linii.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Lista 7 2 7 1, x=7: 0 2 / 2 7 1 / 1 2 7.

SPRAWDŹ TAKŻE
Brak x; tylko jeden element równy x; kolejne duplikaty.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad04.py

```text
DZIEŃ 2 — ZADANIE 04: Krotka i bezpieczny odczyt indeksu
Tematyka: Krotka i bezpieczny odczyt indeksu.
Źródło: Lab05/01 Data structures/04 - tuples.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- tuple('abcdefghijklmnopqrstuvwxyz'): krotka kolejnych liter; można też wpisać litery ręcznie.
- int(input()), porównania i if/else: sprawdzenie indeksu przed odczytem.
- len(), krotka[i], krotka[start:stop]: długość, element i wycinek.
- print(*wycinek): litery osobno, oddzielone spacjami.

Małe przykłady składni — nie są całym rozwiązaniem
    letters = tuple('abcd')
    print(letters[-1])  # d
    print(*letters[1:3])  # b c

Inny sposób / wariant bez własnych funkcji
Nie trzeba własnej funkcji ani importu. Zamiast tworzyć krotkę przez tuple() możesz użyć literału ('a','b',...), ale tutaj materiałem ćwiczenia ma być krotka, nie lista.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz tuple liter a..z. Wczytaj indeks i (int). Dla -26<=i<26 wypisz odpowiednią literę, w przeciwnym razie BLAD. Następnie wypisz długość krotki i litery indeksów 10..15 w jednej linii. Nie modyfikuj krotki.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
i=-1: z / 26 / k l m n o p.

SPRAWDŹ TAKŻE
-26 i 25 są poprawne; -27 i 26 nie są poprawne; indeksowanie od zera.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad05.py

```text
DZIEŃ 2 — ZADANIE 05: Kategorie znaków i formatowanie
Tematyka: Kategorie znaków i formatowanie.
Źródło: Lab05/02 Strings/01–10; Lab06/zad20.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: char_stats(text). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input(): zachowuje wiersz i jego spacje. for char in text: przegląd znaków.
- char == ' ': dosłowna spacja; char.isupper(), char.islower(): litery duże/małe.
- if/elif/else i liczniki += 1: rozłączne kategorie.
- return a,b,c,d zwraca krotkę; print(*wynik) wypisuje jej elementy.
- text.upper(): cały napis wielkimi literami.

Małe przykłady składni — nie są całym rozwiązaniem
    print('Ą'.isupper())  # True
    print('7'.islower())  # False
    print('rower'.upper())  # ROWER

Inny sposób / wariant bez własnych funkcji
Możesz policzyć kategorie bez def, ale końcowa wersja wymaga char_stats. Nie zastępuj testu char==' ' metodą isspace(), bo ta uznaje też tabulatory za białe znaki, a zadanie zalicza je do pozostałych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj cały wiersz tekstu (może być pusty). Funkcja char_stats(text) zwraca (spacje,duze,male,pozostale). Spacja to dokładnie znak " "; litery klasyfikuj isupper i islower; pozostałe obejmują cyfry i interpunkcję. Wypisz 4 liczby w jednej linii, a w drugiej text.upper(). Kategorie mają być rozłączne i sumować się do len(text).

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Tekst Ala 2!: 1 1 2 2 / ALA 2!.

SPRAWDŹ TAKŻE
Pusty tekst; polskie litery; cyfry; tabulator należy do pozostałych.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad06.py

```text
DZIEŃ 2 — ZADANIE 06: Odwracanie bez wycinka
Tematyka: Odwracanie bez wycinka.
Źródło: Lab06/zad18.py; Lab05/02 Strings/05 - slicing.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: reverse_str(text) i palindrome(text). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- Pętla po znakach albo po indeksach; + skleja napisy.
- text.lower() ujednolica litery; text.replace(' ','') usuwa zwykłe spacje.
- == porównuje napisy; funkcja palindrome zwraca bool.
- if/else wybiera wypisanie TAK albo NIE. W reverse_str zakazane są [::-1] i reversed().

Małe przykłady składni — nie są całym rozwiązaniem
    print('A B'.lower())       # a b
    print('A B'.replace(' ', ''))  # AB
    piece = 'x'
    print(piece + 'yz')  # xyz

Inny sposób / wariant bez własnych funkcji
Bez reversed() i bez wycinka użyj własnej pętli i sklejania znaków. Zapis bez def jest możliwy do przećwiczenia, ale końcowo zostaw obie wymagane funkcje. Nie usuwaj innych znaków niż spacje.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj reverse_str(text) bez [::-1] i bez reversed(). Zwróć napis odwrócony. Funkcja palindrome(text) ignoruje spacje i wielkość liter, pozostałych znaków nie usuwa; zwraca bool. Wczytaj linię i wypisz odwrócony tekst, a potem TAK lub NIE zależnie od palindrome.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kajak: kajaK / TAK. Tekst a b a też jest palindromem.

SPRAWDŹ TAKŻE
Pusty tekst uznaj za palindrom; jeden znak; różna wielkość liter.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad07.py

```text
DZIEŃ 2 — ZADANIE 07: Normalizacja słów i częstotliwości
Tematyka: Normalizacja słów i częstotliwości.
Źródło: Lab03/zad06.py; Lab05/02 Strings/09 - string_methods.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- replace(znak,' '), lower(), split(): kolejno zastępowanie, małe litery, podział na słowa.
- {} tworzy słownik; counts.get(word,0) daje dotychczasową liczbę lub 0.
- len(words) liczy wszystkie słowa, len(counts) liczy różne klucze.
- max(counts.values()) wyznacza największą liczność; sorted() albo min() pomaga rozstrzygnąć remis.
- Przed max()/min() sprawdź, czy słownik nie jest pusty.

Małe przykłady składni — nie są całym rozwiązaniem
    print('X,Y!'.replace(',', ' '))  # X Y!
    counts = {}
    counts['rower'] = counts.get('rower', 0) + 1
    print(counts['rower'])  # 1

Inny sposób / wariant bez własnych funkcji
Słownik liczności możesz zbudować pętlą; collections.Counter nie jest konieczny. Zamiast get() użyj if word in counts. Nie musisz definiować funkcji. Jeśli nie znasz klucza sortowania, wybierz zwycięzcę przez prostą pętlę z porównaniem liczności i nazwy.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj wiersz. Zastąp każdy ze znaków ,.!?;: spacją, zamień litery na małe i zastosuj split(). Policz słowa, różne słowa i najczęstsze słowo. Przy remisie wybierz alfabetycznie najmniejsze. Wypisz 3 linie: liczba słów, liczba różnych, "słowo licznik"; dla pustego tekstu ostatnia linia BRAK.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kot, pies! KOT pies ala.: 5 / 3 / kot 2.

SPRAWDŹ TAKŻE
Sama interpunkcja; kilka spacji; remis; znak łącznika pozostaje częścią słowa.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad08.py

```text
DZIEŃ 2 — ZADANIE 08: Słownik jako książka telefoniczna
Tematyka: Słownik jako książka telefoniczna.
Źródło: Lab05/01 Data structures/05 - dicts.py–07 - in_keyword.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()) oraz input().split(): liczba wpisów i para tekstów.
- book={} oraz book[name]=number: dodanie albo aktualizacja klucza.
- book.get(name,'BRAK') lub if name in book: bezpieczne wyszukanie.
- sorted(book): klucze w porządku alfabetycznym; print(name,book[name]): wiersz wyniku.

Małe przykłady składni — nie są całym rozwiązaniem
    name, number = 'Ewa 007'.split()
    book = {}
    book[name] = number
    print(book.get('Jan', 'BRAK'))  # BRAK

Inny sposób / wariant bez własnych funkcji
Własne funkcje nie są obowiązkowe. Bez get() użyj if/in i indeksowania słownika. Numer pozostaw jako str — int('007') dałoby 7 i zgubiłoby zera.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n, potem n linii "imię numer"; numer jest tekstem, żeby zachować zera. Powtórzenie imienia aktualizuje numer. Wczytaj szukane imię; wypisz jego numer albo BRAK. Następnie wypisz wszystkie wpisy po jednym wierszu "imię numer", alfabetycznie po imieniu. Imiona to pojedyncze wyrazy, rozróżniaj wielkość liter.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / Ala 001 / Ola 222 / Ala 003 / Ala: wynik 003, potem Ala 003 i Ola 222.

SPRAWDŹ TAKŻE
n=0; aktualizacja istniejącego klucza nie zwiększa liczby wpisów; in sprawdza klucze.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad09.py

```text
DZIEŃ 2 — ZADANIE 09: Zbiory i deterministyczna kolejność
Tematyka: Zbiory i deterministyczna kolejność.
Źródło: Lab05/01 Data structures/10 - set.py; Lab05/03 Zadania (do przesłania)/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: unique_char_count(text) w osobnej części; program zbiorów może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- set(map(int,input().split())): zbiór liczb; pusta linia daje pusty zbiór.
- A | B: suma zbiorów, A & B: część wspólna, A - B: różnica.
- sorted(wynik) i print(*wynik): stała kolejność liczb na wyjściu.
- set(text) zawiera różne znaki, len(zbior) liczy elementy.

Małe przykłady składni — nie są całym rozwiązaniem
    a = {1, 3}
    b = {3, 5}
    print(sorted(a & b))  # [3]
    print(len(set('aba ')))  # 3, bo spacja również jest znakiem

Inny sposób / wariant bez własnych funkcji
Operacje można zastąpić pętlami i testami in, a unikalne znaki zbierać w liście. Nie jest potrzebny żaden moduł; jednak użycie set jest tu właściwym tematem do przećwiczenia. Zostaw wymaganą unique_char_count.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwie linie liczb int (pusta linia oznacza zbiór pusty). Wypisz w 3 liniach sumę zbiorów, część wspólną i różnicę A-B. W każdej linii liczby rosnąco, bez duplikatów; dla pustego wyniku BRAK. Osobno zdefiniuj unique_char_count(text), licząc także spacje i rozróżniając duże litery.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
A: 1 2 2 3; B: 2 4. Wynik: 1 2 3 4 / 2 / 1 3.

SPRAWDŹ TAKŻE
Dwa puste zbiory; A=B; unikalne znaki to liczba różnych znaków, a nie tylko tych występujących raz.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad10.py

```text
DZIEŃ 2 — ZADANIE 10: Adresy, duplikaty i sortowanie
Tematyka: Adresy, duplikaty i sortowanie.
Źródło: Lab05/03 Zadania (do przesłania)/zad01.py–zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: gmail_addresses(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(input()), input(), for z range(n): odczyt adresów.
- address.split('@')[1] pobiera domenę; porównuj przez ==, a nie wyszukiwanie podnapisu.
- set() i add() usuwają identyczne powtórzenia; sorted() daje listę w kolejności.
- if not wynik: brak adresów; for address in wynik: wypisanie po jednym.

Małe przykłady składni — nie są całym rozwiązaniem
    address = 'ewa@example.org'
    print(address.split('@')[1])  # example.org
    print(sorted({'b', 'a', 'b'}))  # ['a', 'b']

Inny sposób / wariant bez własnych funkcji
Bez set() zbieraj adresy do listy tylko wtedy, gdy jeszcze ich w niej nie ma. Możesz też sprawdzić końcówkę endswith('@gmail.com'). Obliczenia da się rozpisać wprost, lecz końcowa wersja wymaga gmail_addresses.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n, potem n poprawnych adresów e-mail małymi literami. Zachowaj wyłącznie te z domeną dokładnie gmail.com (tekst po @). Usuń duplikaty, posortuj rosnąco cały adres i wypisz każdy w osobnej linii; przy braku BRAK. Funkcja gmail_addresses(data) zwraca listę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 4 / b@gmail.com / a@gmail.com / b@gmail.com / x@notgmail.com. Wynik: a@gmail.com / b@gmail.com.

SPRAWDŹ TAKŻE
n=0; gmail.com.pl nie jest gmail.com; identyczny adres kilka razy.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad11.py

```text
DZIEŃ 2 — ZADANIE 11: Malejące trójki z nakładaniem
Tematyka: Malejące trójki z nakładaniem.
Źródło: Lab05/03 Zadania (do przesłania)/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: triples(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- list(map(int,input().split())): dane, również pusta lista.
- len(data), indeksy i range(): przejście tylko po początkach pełnych okien długości 3.
- Porównanie łańcuchowe a>b>c jest skrótem dla a>b and b>c.
- data[i:i+3]: wycinek okna; wynik.append(okno): zbieranie znalezionych trójek.
- print(*trojka): trzy liczby w jednym wierszu.

Małe przykłady składni — nie są całym rozwiązaniem
    data = [10, 20, 30, 40]
    print(data[1:4])  # [20, 30, 40]
    print(9 > 6 > 2)  # True

Inny sposób / wariant bez własnych funkcji
Zamiast range użyj while z indeksem. Zamiast wycinka możesz zbudować listę z trzech odczytanych elementów. Okna można wypisywać wprost bez def, ale w końcowej wersji triples ma zwrócić zebrane wyniki.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja triples(data) znajduje każde okno trzech sąsiadujących elementów spełniających a>b>c. Okna mogą się nakładać. Wczytaj listę int z jednej linii, również pustą. Wypisz każdą trójkę w osobnej linii w kolejności początku, albo BRAK. Nie eliminuj identycznych trójek w różnych miejscach.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
5 4 3 2 1: 5 4 3 / 4 3 2 / 3 2 1.

SPRAWDŹ TAKŻE
Lista krótsza od 3; równe wartości przerywają ścisłe malenie; koniec listy.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad12.py

```text
DZIEŃ 2 — ZADANIE 12: Malejące trójki bez nakładania
Tematyka: Malejące trójki bez nakładania.
Źródło: Lab05/03 Zadania (do przesłania)/zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: triples(data) jako wersję bez nakładania, zgodnie z zadaniem 11. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- while i zmienny indeks początku: wygodne, gdy przesunięcie zależy od trafienia.
- len(data), indeksy, porównanie a>b>c i data[i:i+3]: ocena pełnego okna.
- i += 1 lub i += 3: różne przesunięcia, zgodnie z poleceniem.
- append() zbiera trójki; print(*trojka) wypisuje ich elementy.

Małe przykłady składni — nie są całym rozwiązaniem
    index = 4
    index += 3
    print(index)  # 7; += zmienia aktualną wartość zmiennej

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz modułów ani dodatkowej funkcji do sprawdzania okna. Pętlę możesz przetestować bez def, ale końcowo zastosuj funkcję analogiczną do zadania 11. Samo for i in range(...) nie reaguje na zmianę i wewnątrz pętli — do sterowanego przesunięcia wybierz while.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Jak zadanie 11, ale po znalezieniu trójki zużyj te trzy elementy; dalsze szukanie zaczyna się za nią. Gdy okno nie pasuje, przesuń początek tylko o jeden. Wynik ma zależeć od skanowania od lewej, bez szukania globalnie najlepszego podziału.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
5 4 3 2 1: tylko 5 4 3. Dla 1 9 8 7 6 5 4: 9 8 7 / 6 5 4.

SPRAWDŹ TAKŻE
Różnica między przesunięciem o 1 i o 3; dwa sąsiednie rozłączne okna.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad13.py

```text
DZIEŃ 2 — ZADANIE 13: Sąsiadujące kwadraty bez duplikatów
Tematyka: Sąsiadujące kwadraty bez duplikatów.
Źródło: Lab06/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: square_pairs(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- len(data), range(), data[i], data[i+1]: sąsiednie elementy.
- a**2 oblicza kwadrat; (a,b) tworzy krotkę opisującą parę.
- seen=set(), pair in seen i seen.add(pair): wykrywanie duplikatów par.
- Osobna lista z append() zachowuje kolejność pierwszego znalezienia.
- print(*pair): dwa elementy w jednym wierszu.

Małe przykłady składni — nie są całym rozwiązaniem
    pair = (5, 25)
    seen = set()
    seen.add(pair)
    print(pair in seen)  # True

Inny sposób / wariant bez własnych funkcji
Nie musisz używać set(): można sprawdzać pair not in lista_wynikow, a potem append. Zbiór przyspiesza sprawdzanie, lista zachowuje kolejność. Końcowe rozwiązanie ma mieć square_pairs, choć samą pętlę można rozpisać bez def.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Zdefiniuj square_pairs(data): szukaj sąsiadów (a,b), dla których b=a**2. Każdą parę wypisz tylko raz, w kolejności pierwszego znalezienia. Wczytaj listę int z jednej linii. Wypisz pary w osobnych liniach albo BRAK. Para (-2,4) jest inna od (2,4); (0,0) jest poprawna.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2 4 2 4 -2 4: 2 4 / -2 4.

SPRAWDŹ TAKŻE
Pusta lista; para na końcu; duplikaty; (1,1); nie pomijaj nakładających się par.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad14.py

```text
DZIEŃ 2 — ZADANIE 14: Filtrowanie typów i statystyki ręczne
Tematyka: Filtrowanie typów i statystyki ręczne.
Źródło: Lab06/zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: integer_stats(data); możesz nazwać drugą wersję integer_stats_manual(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- type(x) is int odróżnia int od bool; isinstance(x,str) rozpoznaje tekst.
- strip() usuwa białe znaki z końców tekstu, indeksowanie/wycinek pozwalają sprawdzić pojedynczy znak + lub -.
- Porównanie '0'<=char<='9' sprawdza cyfrę ASCII; all(...) albo pętla sprawdza cały fragment.
- int(text) konwertuje dopiero po weryfikacji; append() buduje listę liczb.
- W pierwszej wersji: sum(), len(), min(), max(). W ręcznej: licznik, suma, porównania i None.

Małe przykłady składni — nie są całym rozwiązaniem
    print(type(True) is int)  # False
    print(isinstance(True, int))  # True
    print('  +007  '.strip())  # +007
    print('0' <= '5' <= '9')  # True

Inny sposób / wariant bez własnych funkcji
W ręcznej wersji nie używaj sum/min/max/len — policz wynik pętlą. all() także nie jest konieczne: można odrzucić tekst po znalezieniu błędnego znaku. Samo str.isdigit() dopuszcza również niektóre znaki spoza ASCII, więc nie realizuje dokładnie tego warunku. Własne funkcje są wymagane.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja integer_stats(data) przyjmuje listę dowolnych obiektów. Zachowaj int, lecz odrzuć bool i float. Dla str zaakceptuj po strip() opcjonalny pojedynczy + lub - i co najmniej jedną cyfrę ASCII 0..9; przelicz na int. Inne elementy odrzuć. Zwróć (lista,suma,srednia,min,max), dla braku liczb ([],0,None,None,None). Zrób wersję z sum/min/max/len i wersję ręczną bez tych czterech funkcji. To zadanie funkcyjne, bez czytania reprezentacji listy przez eval.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
[7," -2 ",True,None,"5","2.0",3.0] -> ([7,-2,5],10,10/3,-2,7).

SPRAWDŹ TAKŻE
Pusty napis, sam znak +, "--2", False, zero, pusta lista, łańcuch "007".

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

## zad15.py

```text
DZIEŃ 2 — ZADANIE 15: Usuwanie duplikatów i sortowanie z kluczem
Tematyka: Usuwanie duplikatów i sortowanie z kluczem.
Źródło: Lab06/zad12.py, zad19.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: sort_words(words) w części B; część A może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- set(data) albo pętla z in: usunięcie duplikatów.
- sorted(data,key=...) i lista.sort(key=...): sortowanie według klucza.
- Krotki są porównywane od pierwszego elementu, potem od drugiego; False poprzedza True.
- key=len oznacza długość słowa; key=nazwa_funkcji przekazuje funkcję, nie jej wynik.
- Funkcję klucza można zapisać przez def albo krótkie lambda.

Małe przykłady składni — nie są całym rozwiązaniem
    print(sorted(['xxxx', 'a', 'bb'], key=len))  # ['a', 'bb', 'xxxx']
    print(sorted([('b', 2), ('a', 3)]))  # [('a', 3), ('b', 2)]
    key_example = lambda x: x * x  # krótka funkcja: dla 3 zwraca 9

Inny sposób / wariant bez własnych funkcji
Nie musisz używać lambda — funkcję klucza możesz nazwać i zdefiniować przez def. W części A alternatywą są dwie osobne listy liczb posortowane i połączone; jednak aby przećwiczyć wymagany klucz krotkowy, końcowo zrób też wersję z key. Bez własnej funkcji klucza można użyć lambda, a dla słów bezpośrednio key=len.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Część A: wczytaj listę int, usuń duplikaty i wypisz najpierw nieparzyste rosnąco, potem parzyste rosnąco (PUSTA dla pustej). Użyj klucza będącego krotką (czy_parzysta,n). Część B: osobna funkcja sort_words(words) zwraca słowa według długości rosnąco, a dla równych długości zachowuje kolejność wejściową. Nie zmienia oryginału; porównaj z list.sort.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
7 2 3 2 -1 0: -1 3 7 0 2. ["kot","ala","a","do"] -> ["a","do","kot","ala"].

SPRAWDŹ TAKŻE
Ujemne liczby; stabilność sortowania; sorted zwraca listę, sort zmienia listę i zwraca None.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

