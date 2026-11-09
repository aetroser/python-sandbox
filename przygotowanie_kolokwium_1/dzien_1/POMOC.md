# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad01.py

```text
DZIEŃ 1 — ZADANIE 01: Wejście, typy i formatowanie
Tematyka: Wejście, typy i formatowanie.
Źródło: Lab02/zad01.py–zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 8 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: add(a, b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input(): wczytuje jeden wiersz jako str; float(): zamienia tekst na liczbę rzeczywistą.
- print(): wypisuje wynik. Operatory +, - i * wykonują działania.
- F-string f'{x:.2f}' oznacza zapis z dokładnie 2 cyframi po kropce.
- type(x).__name__ daje samą nazwę typu, np. float; type(x) daje zapis <class 'float'>.

Małe przykłady składni — nie są całym rozwiązaniem
    x = float(input())
    print(f'{x:.2f}')        # gdy x=8.5, wypisze 8.50
    print(type(x).__name__)  # wypisze float

Inny sposób / wariant bez własnych funkcji
Najpierw możesz policzyć działania bez własnej funkcji, potem przenieść dodawanie do add(a,b). Do formatowania możesz zamiast f-stringa użyć print(format(x, '.2f')) lub print('{:.2f}'.format(x)). Samo round(x,2) nie zapewnia dwóch wypisanych cyfr: np. round(8.5,2) nadal jest liczbą 8.5.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwie liczby rzeczywiste, każdą w osobnej linii. Wypisz sumę, różnicę a-b i iloczyn, każdy w osobnej linii z dwoma miejscami po kropce. Na końcu wypisz nazwę typu sumy (float). Następnie zdefiniuj funkcję add(a, b) zwracającą sumę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 2.5 oraz -1.5. Wyjście w 4 liniach: 1.00 / 4.00 / -3.75 / float.

SPRAWDŹ TAKŻE
Zero, dwie liczby ujemne, ułamek. Wyjaśnij sobie, dlaczego samo input() nie dodaje liczb.

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
DZIEŃ 1 — ZADANIE 02: Przedział i pętla while
Tematyka: Przedział i pętla while.
Źródło: Lab02/zad03.py, zad06.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: interval(a, b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(): dzieli wiersz na fragmenty. int(): zamienia fragment na liczbę całkowitą.
- min(a,b), max(a,b): ustalają granice; można je zastąpić if i zamianą zmiennych.
- while: wymagany do zbudowania listy; [] tworzy listę, lista.append(x) dopisuje element.
- sum(lista) sumuje liczby, print(*lista) wypisuje elementy osobno, ze spacjami.

Małe przykłady składni — nie są całym rozwiązaniem
    a, b = map(int, input().split())  # map stosuje int do każdego fragmentu
    liczby = []
    liczby.append(12)
    print(*liczby)  # * rozpakowuje listę; tutaj wypisze 12

Inny sposób / wariant bez własnych funkcji
Bez sum() możesz prowadzić sumę w zmiennej i powiększać ją przez +=. Bez map() zapisz części=input().split(), a=int(części[0]), b=int(części[1]). W końcowej wersji zostaw interval i while — to wymagania tego ćwiczenia.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj całkowite a i b w jednej linii. Funkcja interval(a, b) zwraca listę wszystkich liczb od min(a,b) do max(a,b), łącznie z końcami. Zbuduj ją pętlą while. Wypisz liczby w jednej linii, a w drugiej ich sumę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 3 -1. Wyjście: -1 0 1 2 3, a w drugiej linii 5.

SPRAWDŹ TAKŻE
a=b; przedział zawierający zero; obie granice ujemne.

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
DZIEŃ 1 — ZADANIE 03: break, continue i liczba kończąca
Tematyka: break, continue i liczba kończąca.
Źródło: Lab02/zad06.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()): odczyt jednej liczby w każdym obiegu pętli.
- while True, break, continue: w tym ćwiczeniu wszystkie są wymagane.
- if, ==, <, >: rozpoznawanie końca i wybieranie danych.
- n % 2 to reszta z dzielenia przez 2; licznik += 1 i suma += n aktualizują stan.

Małe przykłady składni — nie są całym rozwiązaniem
    licznik = 0
    licznik += 1
    print(licznik, 20)  # dwie wartości w jednym wierszu, oddzielone spacją

Inny sposób / wariant bez własnych funkcji
Listy, sum() i dodatkowe moduły nie są potrzebne. Wystarczą dwie zmienne do wyniku, warunki i wymagana pętla; nie musisz przechowywać wszystkich danych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytuj po jednej liczbie całkowitej aż do 0. Zero kończy wczytywanie i nie jest daną. Ujemne pomijaj przez continue. Zsumuj tylko dodatnie nieparzyste; policz, ile ich było. Wypisz licznik i sumę w jednej linii. Użyj while True oraz break.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Dla kolejnych linii -5, 2, 3, 7, 0 wynik: 2 10.

SPRAWDŹ TAKŻE
Pierwsze wejście 0; same ujemne; same dodatnie parzyste; liczby po 0 nie są przetwarzane.

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
DZIEŃ 1 — ZADANIE 04: Tabliczka i zagnieżdżone pętle
Tematyka: Tabliczka i zagnieżdżone pętle.
Źródło: Lab02/zad04.py–zad05.py; Lab03/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()): wczytuje n. range(start,stop): kolejne liczby bez stop.
- Wersja pierwsza: dwie zagnieżdżone pętle for. Wersja druga: dwie pętle while.
- print(wartość, end=' '): nie przechodzi do następnego wiersza; print() kończy wiersz.
- Operator * mnoży liczby.

Małe przykłady składni — nie są całym rozwiązaniem
    for k in range(2, 5):  # k przyjmuje 2, 3, 4
        print(k, end=' ')
    print()

Inny sposób / wariant bez własnych funkcji
Nie trzeba definiować funkcji ani budować całej tabeli w liście. Wersje for i while uruchamiaj osobno, żeby nie wypisać dwóch tabliczek w jednym wyniku.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (1..12). Wypisz n wierszy po n iloczynów: w wierszu i znajdują się i*1,...,i*n (i od 1). Oddzielaj liczby spacją. Zrób wersję for, a potem zastąp ją wersją while o identycznym wyjściu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
n=3: wiersze 1 2 3 / 2 4 6 / 3 6 9.

SPRAWDŹ TAKŻE
n=1 i n=12; brak dodatkowego pustego wiersza; rozróżniaj numer wiersza od indeksu.

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
DZIEŃ 1 — ZADANIE 05: Funkcje i sumy według parzystości
Tematyka: Funkcje i sumy według parzystości.
Źródło: Lab03/zad01.py–zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_even(n), sum_even(a,b), sum_odd(a,b), selected_sum(even,a,b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- def, parametry i return: definiowanie funkcji i przekazywanie wyniku.
- n % 2, porównanie == oraz bool: sprawdzanie parzystości.
- range(a,b+1) albo while: przejście przez przedział z końcem b.
- if/else wybiera odpowiednią funkcję; suma += n gromadzi wynik.

Małe przykłady składni — nie są całym rozwiązaniem
    def double(value):
        return value * 2
    result = double(4)  # przykład wywołania: result ma wartość 8

Inny sposób / wariant bez własnych funkcji
Pętle sumujące można najpierw przećwiczyć bez def, ale ostatecznie muszą znaleźć się we wskazanych funkcjach. sum() jest możliwym skrótem do sumowania gotowej kolekcji; tutaj łatwiej zacząć od zmiennej sumującej. Nie twórz własnej funkcji o nazwie sum.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj is_even(n), sum_even(a,b), sum_odd(a,b) i selected_sum(even,a,b). Granice włącznie; dla a>b zamień je. selected_sum(True,...) wybiera parzyste, False nieparzyste. Nie nazywaj funkcji sum. W programie wczytaj a b i wypisz obie sumy w jednej linii.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
a=-3, b=3: 0 0. selected_sum(True,1,6) zwraca 12.

SPRAWDŹ TAKŻE
Przedział jednoelementowy; zero jest parzyste; is_even zwraca bool, pozostałe funkcje int.

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
DZIEŃ 1 — ZADANIE 06: Liczby pierwsze
Tematyka: Liczby pierwsze.
Źródło: Lab03/zad05.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_prime(n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(), input().split(): granice; range() lub while: kolejne liczby i potencjalne dzielniki.
- n % d: reszta z dzielenia przez d; if rozdziela przypadki n<2 i pozostałe.
- return True / return False: wynik logiczny funkcji, bez print w jej środku.
- Lista wyników, append(), print(*wyniki); if not wyniki wykrywa pustą listę.

Małe przykłady składni — nie są całym rozwiązaniem
    print(17 % 5)  # 2 — reszta z dzielenia
    print(15 % 5)  # 0 — 5 jest dzielnikiem 15

Inny sposób / wariant bez własnych funkcji
Nie ma potrzebnej tu wbudowanej funkcji is_prime. Napisz własne sprawdzanie dzielników. Biblioteki nie są konieczne; samą pętlę można sprawdzić bez def, ale końcowa wersja wymaga is_prime.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj is_prime(n) -> bool. Wczytaj całkowite a b. Wypisz rosnąco liczby pierwsze z domkniętego przedziału między nimi, albo BRAK. Nie korzystaj z zewnętrznych bibliotek. Liczby mniejsze od 2 nie są pierwsze.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: -2 11. Wynik: 2 3 5 7 11.

SPRAWDŹ TAKŻE
0, 1, 2, 4, 49, 97; odwrócone granice; przedział bez liczb pierwszych.

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
DZIEŃ 1 — ZADANIE 07: Silnia iteracyjna i rekurencyjna
Tematyka: Silnia iteracyjna i rekurencyjna.
Źródło: Lab04/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: factorial_loop(n) i factorial_recursive(n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- for z range() albo while i *=: wersja iteracyjna.
- if, return oraz wywołanie własnej funkcji: wersja rekurencyjna.
- import math, math.factorial(n): tylko do porównania wyników własnych wersji.
- int(input()), print(): wejście i wypisanie dwóch wyników.

Małe przykłady składni — nie są całym rozwiązaniem
    iloczyn = 1
    iloczyn *= 7  # to samo co iloczyn = iloczyn * 7
    import math
    print(math.factorial(3))  # 6; przykład kontroli, nie zamiennik obu wersji

Inny sposób / wariant bez własnych funkcji
Wersję z pętlą da się zapisać bez własnej funkcji. Rekurencja w tym ćwiczeniu polega na wywoływaniu factorial_recursive, więc wymaga def. Nie zastępuj obu wymaganych implementacji samym math.factorial().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj factorial_loop(n) i factorial_recursive(n) dla n od 0 do 20. Obie zwracają int. Wczytaj n i wypisz oba wyniki, każdy w osobnej linii. Porównaj ręcznie z math.factorial. Nie mierz czasu pojedynczego bardzo krótkiego wywołania.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
n=5: dwie linie po 120. Dla n=0 obie funkcje zwracają 1.

SPRAWDŹ TAKŻE
0, 1, 10, 20; warunek kończący rekurencję. Nie podawaj ujemnego n.

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
DZIEŃ 1 — ZADANIE 08: Konwersje i wybór operacji
Tematyka: Konwersje i wybór operacji.
Źródło: Lab02/zadania do realizacji.py; Lab04/zad02.py–zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: km_to_miles(distance), miles_to_km(distance), c_to_f(value), f_to_c(value). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().upper(): wybór operacji niezależnie od wielkości liter.
- while, if/elif/else, break: ponawianie wyboru i wybranie przeliczenia.
- in sprawdza przynależność, np. do krotki dozwolonych napisów.
- float(input()), operatory *, /, +, - oraz print(f'{wynik:.2f}').

Małe przykłady składni — nie są całym rozwiązaniem
    choice = input().upper()
    print('mi'.upper())  # MI
    value = 3.5
    print(f'{value:.2f}')  # 3.50

Inny sposób / wariant bez własnych funkcji
Przeliczenia to zwykłe działania i można je wykonać bez bibliotek oraz bez def. W końcowej wersji umieść je jednak w czterech wymaganych funkcjach. Zamiast upper() można porównywać osobno warianty małych i dużych liter.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj km_to_miles, miles_to_km, c_to_f, f_to_c. Przyjmij 1 mila = 1.60934 km; F=C*9/5+32. Wczytuj nazwę operacji KM, MI, C lub F aż będzie poprawna (ignoruj wielkość liter); przy złej wypisz BLAD. KM oznacza km na mile, MI mile na km, C stopnie C na F, F odwrotnie. Następnie wczytaj wartość i wypisz wynik z 2 miejscami.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kolejne linie: x / c / 20. Wyjście: BLAD, a potem 68.00.

SPRAWDŹ TAKŻE
0 stopni C; -40; 1 mila; kilka błędnych wyborów; odległości są nieujemne.

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
DZIEŃ 1 — ZADANIE 09: Wzór i rozłączne przedziały
Tematyka: Wzór i rozłączne przedziały.
Źródło: Lab04/zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: bmi(height,mass) oraz band(height,mass). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- float(), input().split(): dwie liczby z jednego wiersza.
- ** to potęgowanie, / to dzielenie; if/elif/else sprawdza rozłączne przedziały.
- Wywołanie bmi(...) wewnątrz band(...): użycie wyniku innej funkcji.
- print(f'{wartosc:.2f}'): dwa miejsca; print(symbol): kolejny wiersz.

Małe przykłady składni — nie są całym rozwiązaniem
    print(4 ** 2)  # 16; w Pythonie potęga to **, a nie ^
    x = 24.999
    print(f'{x:.2f}')  # 25.00, choć x nadal jest mniejsze od 25

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz modułu math. Wariant bez def jest możliwy jako pierwsza próba, ale końcowa wersja ma zawierać obie funkcje. Nie używaj zaokrąglonego tekstu do wyboru przedziału.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Ćwiczenie obliczeniowe na wzorze BMI, bez interpretacji zdrowotnej. Funkcja bmi(height,mass) zwraca mass/height**2; wzrost w metrach, masa w kg. Funkcja band(height,mass) używa bmi i zwraca A dla wyniku <18.5, B dla [18.5,25), C dla [25,30), D dla >=30. Dane dodatnie. Wczytaj height mass; wypisz wartość z 2 miejscami i symbol w drugiej linii. Klasyfikuj przed zaokrągleniem.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście 2 100: 25.00 / C.

SPRAWDŹ TAKŻE
Wzrost 2 i masy 74, 100, 120 sprawdzają dokładne progi. Wynik 24.999 należy jeszcze do B.

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
DZIEŃ 1 — ZADANIE 10: Równanie kwadratowe i przypadki szczególne
Tematyka: Równanie kwadratowe i przypadki szczególne.
Źródło: Lab03/zad08.py; Lab04/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: real_roots(a,b,c). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(), int(): współczynniki; **, *, -, /: obliczenia.
- W tym ćwiczeniu użyj import math i math.sqrt(delta), tylko dla delta>=0.
- if/elif/else: trzy przypadki; [], append(), sorted(): lista wyników rosnąco.
- len(wyniki): liczba wyników; print(f'{x:.2f}'): jeden wynik z 2 miejscami.

Małe przykłady składni — nie są całym rozwiązaniem
    import math
    print(math.sqrt(25))  # 5.0
    print(sorted([8, -2]))  # [-2, 8]
    print(f'{1.5:.2f}')  # 1.50

Inny sposób / wariant bez własnych funkcji
Przypadki można rozpisać wprost bez def, ale końcowo użyj real_roots. Zamiast sorted() wystarczy porównać dwa wyniki i w razie potrzeby je zamienić. Nie stosuj sqrt do ujemnej delty.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja real_roots(a,b,c) zwraca listę rzeczywistych rozwiązań rosnąco. Zakładamy a!=0; dla delty=0 zwróć jeden element, dla delty<0 pustą listę. Wczytaj całkowite a b c; wypisz liczbę pierwiastków, a następnie każdy z nich w osobnej linii z 2 miejscami. Zastosuj math.sqrt tylko dla nieujemnej delty.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
1 -3 2: linie 2 / 1.00 / 2.00. 1 0 1: tylko 0.

SPRAWDŹ TAKŻE
Delta dodatnia/zerowa/ujemna; a ujemne; uporządkowanie wyników.

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
DZIEŃ 1 — ZADANIE 11: Importy i samodzielne uruchamianie modułu
Tematyka: Importy i samodzielne uruchamianie modułu.
Źródło: Lab03/zad01.py–zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_even i sum_even w osobnym module narzedzia11.py. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import nazwa_modulu: potem wywołujesz nazwa_modulu.nazwa_funkcji(...).
- from nazwa_modulu import nazwa_funkcji: pozwala wywołać samą nazwę funkcji.
- if __name__ == '__main__': umieść pod nim wejście/wyjście wykonywane tylko przy uruchomieniu pliku.
- Nie dodawaj końcówki .py w instrukcji import; oba pliki mają być obok siebie.

Małe przykłady składni — nie są całym rozwiązaniem
    # Dwa niezależne przykłady składni importu:
    import math
    print(math.sqrt(16))
    from math import sqrt
    print(sqrt(16))

Inny sposób / wariant bez własnych funkcji
Ten sam rachunek da się wykonać w jednym pliku bez modułu, ale nie spełniłoby to celu tego zadania. Tu ćwiczysz właśnie własne funkcje, import i brak wypisywania danych przy imporcie.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz obok tego pliku narzedzia11.py z is_even i sum_even z zadania 5; na górze nowego pliku wpisz temat i źródło Lab03/zad01.py–zad02.py. Ten plik zad11.py ma importować narzedzia11, wczytać a b i wypisać sumę parzystych. Import narzedzia11 nie może nic wypisywać ani pytać o dane. Pokaż ręcznie różnicę między import narzedzia11 i from narzedzia11 import is_even.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście 1 6: 12. Polecenie python -c "import narzedzia11" uruchomione w tym folderze: brak wyjścia.

SPRAWDŹ TAKŻE
if __name__ == "__main__"; unikaj import *; funkcja nie powinna przesłaniać wbudowanego sum.

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
DZIEŃ 1 — ZADANIE 12: Wartość funkcji i pierwiastki zespolone
Tematyka: Wartość funkcji i pierwiastki zespolone.
Źródło: Lab04/zad01.py, zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: value(x) i complex_roots(a,b,c). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- **, *, +, -, /: zwykłe działania; float(input()): argument części A.
- Część B: import cmath i cmath.sqrt(...), który dopuszcza ujemny argument.
- Zwróć dwa elementy np. jako listę; liczba zespolona może zawierać jednostkę 1j.
- W części A użyj print(f'{wynik:.2f}'); części B nie dopisuj do tego samego wyjścia.

Małe przykłady składni — nie są całym rozwiązaniem
    import cmath
    print(cmath.sqrt(-9))  # 3j
    print(1j * 1j)  # (-1+0j)

Inny sposób / wariant bez własnych funkcji
Część A to działania możliwe bez bibliotek. Sam rachunek obu części można zapisać bez def, lecz ćwiczenie wymaga wskazanych funkcji i cmath.sqrt w części B. eval() nie jest potrzebne.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Część A: value(x) oblicza 3*x**2+7*x-19; wczytaj x i wypisz wynik z 2 miejscami. Część B: complex_roots(a,b,c), a!=0, zwraca dwa pierwiastki, także gdy są równe; użyj cmath.sqrt. Przykłady części B uruchamiaj ręcznie osobno. Nie potrzebujesz eval.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
value(2)=7. complex_roots(1,0,1) daje pierwiastki 1j i -1j (kolejność dowolna).

SPRAWDŹ TAKŻE
Pierwiastek zespolony podniesiony do kwadratu ma dać -1; delta=0; ujemne x.

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
DZIEŃ 1 — ZADANIE 13: Moduł random i powtarzalny eksperyment
Tematyka: Moduł random i powtarzalny eksperyment.
Źródło: Lab02/zad07.py; Lab05/03 Zadania (do przesłania)/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: experiment(seed,n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import random; rng=random.Random(seed): lokalny generator z własnym ziarnem.
- rng.randint(a,b), rng.randrange(a,b), rng.random(): różne sposoby losowania.
- rng.choice(lista), rng.choices(lista,k=3), rng.sample(lista,k=3): wybór elementów.
- lista.copy() lub lista[:]: kopia; rng.shuffle(kopia): tasowanie w miejscu, nie zwraca listy.
- split('@') lub endswith('@gmail.com'): wybór domeny; append(): budowanie list.

Małe przykłady składni — nie są całym rozwiązaniem
    import random
    rng = random.Random(17)
    sample = ['red', 'green', 'blue']
    chosen = rng.choice(sample)
    copy = sample.copy()
    rng.shuffle(copy)  # nie pisz copy = rng.shuffle(copy)

Inny sposób / wariant bez własnych funkcji
Do filtrowania adresów wystarczy for i if — list comprehension nie jest obowiązkowe. Losowania można wykonać bez własnej funkcji, ale tu pozostaw experiment, żeby porównać dwa wywołania. Zwykłe funkcje modułu random nie zastępują wymaganego lokalnego generatora.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Zdefiniuj experiment(seed,n). Utwórz lokalny generator random.Random(seed). Wylosuj n liczb randint(0,10), następnie jeden adres z listy ["a@gmail.com","b@interia.com","c@gmail.com"] po odfiltrowaniu gmail.com, następnie potasuj kopię tej listy. Zwróć krotkę (liczby,adres,potasowana_lista). Nie zmieniaj pierwotnej listy. Osobno sprawdź randrange(0,10), random(), choices(...,k=3) oraz sample(...,k=3); opisz różnice w komentarzu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Dwa wywołania experiment(42,5) w tej samej wersji Pythona mają dać identyczne wyniki; liczby należą do 0..10.

SPRAWDŹ TAKŻE
n=0; randint zawiera oba końce, randrange nie zawiera stop; choices dopuszcza powtórzenia, sample wybiera pozycje bez zwracania.

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
DZIEŃ 1 — ZADANIE 14: Jednoczesne rzuty wieloma kośćmi
Tematyka: Jednoczesne rzuty wieloma kośćmi.
Źródło: Lab02/zad08.py; Lab04/zad05.py, zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: dice_until(n,limit,seed); w rozszerzeniu sum_even_draws(target,limit,seed). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import random, random.Random(seed), rng.randint(1,6): wyniki kości.
- for z range(limit) albo while z licznikiem: ograniczona liczba rund.
- Lista jednej rundy; all(warunek for element in lista) sprawdza, czy wszystkie elementy pasują.
- Alternatywnie lista.count(1) lub count(6) podaje liczność wartości; return może zwrócić krotkę.
- W rozszerzeniu % 2, += i porównanie >= służą do parzystości, sumy i końca.

Małe przykłady składni — nie są całym rozwiązaniem
    values = [4, 4, 4]
    print(all(x == 4 for x in values))  # True
    print(values.count(4))  # 3
    print((2, 'LIMIT'))  # krotka dwóch elementów

Inny sposób / wariant bez własnych funkcji
Bez all() i count() policz pasujące wyniki zwykłą pętlą. Nie musisz używać list comprehension. Całą symulację da się rozpisać wprost, ale końcowe ćwiczenie wymaga własnych funkcji i lokalnego Random(seed).

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja dice_until(n,limit,seed) losuje w jednej rundzie n kości (1..6 każda), używając lokalnego Random(seed). Kończy po pierwszej rundzie samych jedynek lub samych szóstek, albo po limit rundach. Zwraca (liczba_rund, "JEDYNKI"/"SZOSTKI"/"LIMIT"). Parametry: 1<=n<=20, 0<=limit<=10000. Nie sumuj jedynek z różnych rund. Rozszerzenie: osobna funkcja sum_even_draws(target,limit,seed) dodaje tylko parzyste losowania randint(1,100) do chwili suma>=target albo limit; zwraca liczbę wszystkich losowań i sumę, target>0.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
limit=0: (0,"LIMIT"). Dla n=1 i limit=1000 zwykle szybko pojawi się 1 albo 6; porównaj dwa uruchomienia tego samego seed.

SPRAWDŹ TAKŻE
Zawsze istnieje limit; licznik rund różni się od liczby pojedynczych kości; w rozszerzeniu licz też nieparzyste losowania.

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
DZIEŃ 1 — ZADANIE 15: Przybliżenie całki prostokątami
Tematyka: Przybliżenie całki prostokątami.
Źródło: Lab04/zad08.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: rectangle_sum(a,b,n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(), float(), int(): dwie granice oraz liczba części.
- range(n): dokładnie n indeksów od 0 do n-1; for albo while do sumowania.
- **, *, /, +, - oraz suma += pole: obliczanie i dodawanie pól.
- print(f'{wynik:.4f}'): dokładnie 4 miejsca po kropce, także końcowe zera.

Małe przykłady składni — nie są całym rozwiązaniem
    parts = input().split()
    a = float(parts[0])
    b = float(parts[1])
    n = int(parts[2])
    print(f'{2.5:.4f}')  # 2.5000

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz biblioteki do całkowania ani funkcji sum(). Wystarczy pętla ze zmienną sumującą. Osobna funkcja dla wielomianu jest opcjonalna; rectangle_sum pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja rectangle_sum(a,b,n) dla a<b i n>=1 oblicza przybliżenie dla f(x)=2*x**2+x-6. Podziel [a,b] na n równych części o szerokości h=(b-a)/n. Dodaj n pól h*f(a+i*h), i=0..n-1. To suma wartości ze znakiem: ujemne pola pozostają ujemne. Nie potrzeba znajomości całek. Wczytaj a b n, wypisz wynik z 4 miejscami. Indeksuj części liczbą całkowitą, żeby uniknąć dryfowania pętli po float.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
0 2 2: pola -6 oraz -3, wynik -9.0000.

SPRAWDŹ TAKŻE
n=1; przedział przecinający miejsce zerowe; porównaj n=10 i n=1000.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

