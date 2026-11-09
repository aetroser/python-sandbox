# Rozwinięcia i pomoc — opcjonalnie

W plikach zadań są krótkie polecenia. Tutaj zachowano wcześniejsze pełne warunki, wskazówki i przykłady. Nie musisz czytać całości przed ćwiczeniami.

## zad01.py

```text
DZIEŃ 3 — ZADANIE 01: Formatowanie daty i czasu
Tematyka: Formatowanie daty i czasu.
Źródło: Lab05/03 Zadania (do przesłania)/zad06.py; Lab06/zad05.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: now_text(); przetwarzanie podanej daty może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import datetime: import klasy, nie całego modułu.
- map(int,input().split()) i rozpakowanie do 6 zmiennych: odczyt pól.
- datetime(rok,miesiac,dzien,godzina,minuta,sekunda): tworzy obiekt.
- f'{dt:%Y-%m-%d %H:%M:%S}': format daty i czasu z zerami.
- datetime.now(): aktualna data i czas tylko w dodatkowej funkcji now_text.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import datetime
    dt = datetime(2020, 8, 9, 6, 7, 8)
    print(f'{dt:%Y-%m-%d %H:%M:%S}')  # 2020-08-09 06:07:08

Inny sposób / wariant bez własnych funkcji
Zamiast f-stringa można użyć dt.strftime('%Y-%m-%d %H:%M:%S'). Kody %Y/%m/%d to rok/miesiąc/dzień, %H/%M/%S to godzina/minuta/sekunda — %m i %M znaczą co innego. Nie musisz tworzyć dodatkowej funkcji do wczytanej daty; now_text pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj 6 int w jednej linii: rok miesiąc dzień godzina minuta sekunda. Data i czas są poprawne. Utwórz datetime i wypisz RRRR-MM-DD GG:MM:SS z zerami wiodącymi. W osobnej funkcji now_text() zwróć aktualny lokalny czas w tym samym formacie; tej funkcji nie używaj do powtarzalnego przykładu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024 2 3 4 5 6 -> 2024-02-03 04:05:06.

SPRAWDŹ TAKŻE
Północ; koniec roku; różnica między date i datetime.

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
DZIEŃ 3 — ZADANIE 02: Dzień tygodnia po polsku
Tematyka: Dzień tygodnia po polsku.
Źródło: Lab06/zad06.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: day_of_week(d). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date; date.fromisoformat(text): zamiana tekstu RRRR-MM-DD na datę.
- d.weekday(): numer dnia 0..6 (0=poniedziałek).
- Lista lub krotka polskich nazw i indeksowanie [numer]: wybór nazwy.
- input(), return, print(): odczyt, zwrot nazwy, wypisanie.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    d = date.fromisoformat('2020-01-06')
    print(d.weekday())  # 0, czyli poniedziałek

Inny sposób / wariant bez własnych funkcji
Bez listy nazw można użyć if/elif dla numerów albo słownika. Nie trzeba definiować własnej funkcji konwertującej tekst na datę, bo jest fromisoformat. Wymagana własna funkcja day_of_week ma zwracać polski napis.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja day_of_week(d) przyjmuje datetime.date i zwraca małymi literami polską nazwę dnia: poniedziałek,...,niedziela. Wczytaj poprawną datę RRRR-MM-DD i wypisz nazwę. Skorzystaj z weekday; nie polegaj na języku systemu operacyjnego.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024-01-01 -> poniedziałek; 2024-01-07 -> niedziela.

SPRAWDŹ TAKŻE
weekday numeruje od 0; isoweekday od 1; luty roku przestępnego.

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
DZIEŃ 3 — ZADANIE 03: Wiek w pełnych latach
Tematyka: Wiek w pełnych latach.
Źródło: Lab05/03 Zadania (do przesłania)/zad08.py; Lab06/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: how_old(birth,today). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date i date.fromisoformat(input()): odczyt obu dat.
- d.year, d.month, d.day: pola daty; - i if: obliczenia i korekta pełnych lat.
- Porównanie krotek (miesiąc,dzień): najpierw miesiąc, przy równości dzień.
- return zwraca int; print(wiek) wypisuje go bez formatowania dziesiętnego.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    d = date(2020, 8, 9)
    print(d.year, d.month, d.day)  # 2020 8 9
    print((2, 28) < (3, 1))  # True

Inny sposób / wariant bez własnych funkcji
Dwie pary pól możesz porównać zwykłymi warunkami zamiast krotek. Nie ma potrzeby date.today() ani dzielenia liczby dni przez 365. Rachunek można przetestować bez def, ale końcowo how_old jest wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja how_old(birth,today) przyjmuje dwie daty, birth<=today. Wczytaj je w dwóch liniach RRRR-MM-DD. Zwróć i wypisz liczbę pełnych lat. Rok zwiększa się w dniu urodzin. Dla 29 lutego w roku nieprzestępnym przyjmij zwiększenie wieku 1 marca. Nie używaj date.today() w tej wersji.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2000-11-13 oraz 2026-11-12 -> 25; dla 2026-11-13 -> 26.

SPRAWDŹ TAKŻE
Dzień przed urodzinami; dzień urodzin; narodziny dziś; 29 lutego.

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
DZIEŃ 3 — ZADANIE 04: Różnica dni i pełne tygodnie
Tematyka: Różnica dni i pełne tygodnie.
Źródło: Lab06/zad08.py, zad13.py; Lab05/03 Zadania (do przesłania)/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: date_distance(start,end). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): daty wejściowe.
- end-start daje timedelta; (end-start).days daje podpisaną liczbę dni.
- abs(liczba) to wartość bezwzględna, // oznacza dzielenie całkowite.
- return dni,tygodnie zwraca krotkę; print(*wynik) wypisuje dwie liczby.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    span = date(2020, 1, 10) - date(2020, 1, 1)
    print(span.days)  # 9
    print(abs(-9) // 7)  # 1

Inny sposób / wariant bez własnych funkcji
Zamiast abs() można zmienić znak ujemnej liczby warunkiem if. Odejmowania dat nie trzeba implementować ręcznie. Wariant bez własnej funkcji jest możliwy, lecz końcowa wersja wymaga date_distance.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja date_distance(start,end) zwraca krotkę: podpisana różnica dni end-start oraz liczba pełnych tygodni w bezwzględnej różnicy dni. Wczytaj dwie daty, wypisz dwie liczby. Nie doliczaj dnia początkowego.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024-01-01 i 2024-01-16 -> 15 2. Zamiana dat -> -15 2.

SPRAWDŹ TAKŻE
Ta sama data; 6 i 7 dni; przejście przez 29 lutego.

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
DZIEŃ 3 — ZADANIE 05: Luty i lata przestępne
Tematyka: Luty i lata przestępne.
Źródło: Lab06/zad14.py, zad17.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: days_in_february(year). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import calendar; calendar.isleap(year): True dla roku przestępnego.
- range(a,b+1): lata z końcową granicą włącznie.
- % (reszta), ==, and/or: własny warunek podzielności roku.
- Lista, append() i print(*lista): wypisanie lat; if not lista: BRAK.

Małe przykłady składni — nie są całym rozwiązaniem
    import calendar
    print(calendar.isleap(2020))  # True
    print(2020 % 4)  # 0, czyli rok jest podzielny przez 4

Inny sposób / wariant bez własnych funkcji
Zgodnie z poleceniem wykonaj najpierw wersję z isleap(), potem wersję bez tej funkcji — zwykłymi warunkami podzielności. Własna days_in_february jest wymagana w końcowej wersji.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwa lata a<=b (1900..2100). Wypisz lata przestępne od a do b albo BRAK; w drugiej linii liczbę dni lutego roku b. Zdefiniuj days_in_february(year). Najpierw wersja z calendar.isleap, potem własny warunek porównany z modułem.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
1999 2001 -> 2000 / 28.

SPRAWDŹ TAKŻE
1900 nie jest przestępny; 2000 jest; 2100 nie jest; 2024 jest.

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
DZIEŃ 3 — ZADANIE 06: Dodawanie dni i poniedziałki
Tematyka: Dodawanie dni i poniedziałki.
Źródło: Lab06/zad15.py–zad16.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: mondays(year) i plus_three_weeks(d). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import date,timedelta: daty i odstępy czasu.
- date(year,1,1), d.year, d.weekday(): początek i sprawdzanie dnia.
- timedelta(days=1) / timedelta(days=7): przesuwanie o dzień/tydzień.
- timedelta(weeks=3) i timedelta(days=21): dwie formy tego samego odstępu.
- append() zbiera daty, d.isoformat() zwraca tekst RRRR-MM-DD.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date, timedelta
    d = date(2020, 8, 9)
    print((d + timedelta(days=2)).isoformat())  # 2020-08-11

Inny sposób / wariant bez własnych funkcji
Możesz przechodzić po każdym dniu i wybierać poniedziałki albo znaleźć pierwszy poniedziałek i iść co 7 dni. Nie trzeba pisać własnej obsługi długości miesięcy. Bez def można wykonać próbę, lecz końcowo pozostaw obie funkcje.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj rok (1900..2100). Funkcja mondays(year) zwraca listę dat wszystkich poniedziałków tego roku. Wypisz je po jednej w formacie ISO. Osobno zdefiniuj plus_three_weeks(d) i sprawdź zgodność dodania timedelta(weeks=3) i timedelta(days=21).

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024: pierwsza data 2024-01-01, ostatnia 2024-12-30; jest ich 53.

SPRAWDŹ TAKŻE
Rok zaczynający się innym dniem; nie wypisuj dat kolejnego roku; zmiana miesiąca.

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
DZIEŃ 3 — ZADANIE 07: calendar i struktura miesiąca
Tematyka: calendar i struktura miesiąca.
Źródło: Lab05/03 Zadania (do przesłania)/zad05.py; Lab06/zad17.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- import calendar; calendar.setfirstweekday(calendar.MONDAY): poniedziałek jako pierwsza kolumna.
- calendar.monthcalendar(year,month): lista tygodni, każdy z 7 liczb dni (0 oznacza poza miesiącem).
- Dwie pętle albo indeks kolumny 0: liczenie dni i poniedziałków.
- calendar.month(year,month) i calendar.calendar(year): tekstowe kalendarze do osobnej obserwacji.

Małe przykłady składni — nie są całym rozwiązaniem
    import calendar
    calendar.setfirstweekday(calendar.MONDAY)
    weeks = calendar.monthcalendar(2020, 8)
    print(weeks[0])  # [0, 0, 0, 0, 0, 1, 2]

Inny sposób / wariant bez własnych funkcji
Nie musisz pisać własnych funkcji. Dni można też otrzymać przez calendar.monthrange(year,month)[1], ale to dodatek: w tym zadaniu przećwicz wymaganą macierz monthcalendar. Kalendarze tekstowe oglądaj oddzielnie, żeby nie zmienić wymaganego wyjścia liczbowego.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj rok miesiąc. Użyj calendar.monthcalendar: zera są dniami spoza miesiąca. Wypisz liczbę dni miesiąca i liczbę poniedziałków w nim (w jednej linii). Następnie ręcznie obejrzyj calendar.month i calendar.calendar dla tego roku. Ustaw pierwszy dzień tygodnia na poniedziałek.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024 2 -> 29 4.

SPRAWDŹ TAKŻE
Luty przestępny; miesiąc mający 5 poniedziałków; nie licz zer jako dni.

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
DZIEŃ 3 — ZADANIE 08: Średnia, mediana i moda
Tematyka: Średnia, mediana i moda.
Źródło: Lab06/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): lista liczb; import statistics.
- statistics.mean(data), statistics.median(data): średnia i mediana.
- statistics.multimode(data): lista wszystkich mod; min(...) wybiera najmniejszą z nich.
- print(f'{x:.2f}'): dokładnie 2 miejsca dla średniej/mediany; modę wypisz jako int.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.multimode([8, 8, 3, 3]))  # [8, 3]
    print(min([8, 3]))  # 3
    print(f'{2.5:.2f}')  # 2.50

Inny sposób / wariant bez własnych funkcji
Własne funkcje nie są obowiązkowe. Bez statistics średnią policz przez sum()/len(), medianę z posortowanej listy i środkowych pozycji, a mody za pomocą słownika liczności. Zamiast sum() też można użyć pętli. Przy remisie samo mode() nie gwarantuje najmniejszej wartości.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepustą listę int z jednej linii. Wypisz w 3 liniach średnią z 2 miejscami, medianę z 2 miejscami i modę jako int. Przy remisie mody wybierz najmniejszą z najczęstszych liczb; możesz użyć statistics.multimode i min. Nie zakładaj, że statistics.mode rozstrzyga remis przez najmniejszą wartość.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
4 1 4 1: 2.50 / 2.50 / 1.

SPRAWDŹ TAKŻE
Jeden element; parzysta liczba elementów; liczby ujemne; wszystkie różne.

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
DZIEŃ 3 — ZADANIE 09: Wariancja i odchylenie standardowe
Tematyka: Wariancja i odchylenie standardowe.
Źródło: Lab06/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(float,input().split())): odczyt liczb rzeczywistych.
- import statistics; statistics.variance(data), statistics.stdev(data): wartości dla próby.
- print(f'{x:.4f}'): cztery miejsca po kropce.
- abs(a-b) ocenia małą różnicę numeryczną; **2 podnosi odchylenie do kwadratu.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.variance([2, 4]))  # 2
    print(f'{0.5:.4f}')  # 0.5000

Inny sposób / wariant bez własnych funkcji
Nie musisz definiować własnych funkcji. Dodatkowo możesz policzyć wariancję ręcznie: suma kwadratów odchyleń od średniej podzielona przez n-1, a odchylenie jako jej pierwiastek. W głównym ćwiczeniu użyj jednak wymaganych variance i stdev, nie wersji populacyjnych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj co najmniej 2 liczby rzeczywiste. Wypisz statistics.variance i statistics.stdev (dla próby), każde z 4 miejscami po kropce. Nie używaj pvariance ani pstdev. Sprawdź ręcznie, czy stdev**2 jest bliskie variance.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
1 2 3: 1.0000 / 1.0000.

SPRAWDŹ TAKŻE
Wszystkie równe; tylko 2 liczby; różnica między dzieleniem przez n i n-1.

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
DZIEŃ 3 — ZADANIE 10: Progi ocen i kolejność warunków
Tematyka: Progi ocen i kolejność warunków.
Źródło: Lab06/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: calculate_grade(points,max_points,thresholds). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- Punkty/maksimum i *100 dają procent; > oznacza przekroczenie, nie osiągnięcie progu.
- Lista krotek; for threshold,grade in thresholds rozpakowuje każdy próg i ocenę.
- if oraz return: zwrócenie pierwszej pasującej oceny; po przejrzeniu progów wartość domyślna.
- int(), input().split(), print(): odczyt i wypisanie int.

Małe przykłady składni — nie są całym rozwiązaniem
    limits = [(90, 'A'), (70, 'B')]
    for boundary, label in limits:
        print(boundary, label)  # przykład rozpakowania pary

Inny sposób / wariant bez własnych funkcji
Wariant bez pętli to if/elif dla kolejnych progów; wariant bez def także policzy ocenę. Końcowa wersja ma jednak wykorzystywać calculate_grade i przekazaną listę thresholds. Nie używaj round() przed porównaniem.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj calculate_grade(points,max_points,thresholds). Progi to [(80,5),(60,4),(50,3)] w kolejności malejącej. Ocena odpowiada pierwszemu progowi, który procent ściśle przekracza; gdy brak, 2. max_points>0, 0<=points<=max_points. Wczytaj points max_points i wypisz ocenę. Te progi są wyłącznie ćwiczeniem z Lab06; prawdziwe kolokwium oceniane jest liczbą całych zadań.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
80 100 -> 4; 81 100 -> 5; 50 100 -> 2; 51 100 -> 3.

SPRAWDŹ TAKŻE
Dokładnie 50%,60%,80%; 0 i 100%; nie zaokrąglaj procentu przed decyzją.

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
DZIEŃ 3 — ZADANIE 11: Reguły i zbiory objawów jako dane
Tematyka: Reguły i zbiory objawów jako dane.
Źródło: Lab06/zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: classify(tokens). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(): lista tokenów, set(tokens): zbiór bez powtórzeń.
- 'token' in symptoms: obecność; == porównuje całe zbiory.
- if/elif/else oraz and/not: wyrażanie reguł, od bardziej szczegółowych.
- return 'NAPIS' zwraca etykietę, print(...) wypisuje wynik funkcji.

Małe przykłady składni — nie są całym rozwiązaniem
    tokens = set('a b a'.split())
    print('a' in tokens)  # True
    print(tokens == {'a', 'b'})  # True

Inny sposób / wariant bez własnych funkcji
Zamiast set() możesz użyć trzech zmiennych bool oznaczających obecność tokenów. Moduły nie są potrzebne. Reguły można przetestować bez def, ale końcowo classify pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
To wyłącznie ćwiczenie reguł tekstowych. Wczytaj jedną linię tokenów: goraczka, miesnie, oslabienie; pusta linia dozwolona. Powtórzenia ignoruj. Funkcja classify(tokens) zwraca GRYPA dla wszystkich trzech; PRZEZIEBIENIE dla goraczka i oslabienie bez miesnie; PRZETRENOWANIE dla samego miesnie; OK dla pustego zbioru lub samego oslabienie; INNE dla pozostałych kombinacji. Wypisz wynik. Nie jest to narzędzie medyczne.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
goraczka oslabienie miesnie -> GRYPA; miesnie -> PRZETRENOWANIE.

SPRAWDŹ TAKŻE
Sprawdź wszystkie 8 możliwych podzbiorów trzech tokenów; reguła szczegółowa przed ogólną.

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
DZIEŃ 3 — ZADANIE 12: Pomiar czasu bez z góry ustalonego zwycięzcy
Tematyka: Pomiar czasu bez z góry ustalonego zwycięzcy.
Źródło: Lab06/zad04.py; Lab04/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(range(...)) i tuple(range(...)): dane do porównania; += w pętli sumującej.
- import time; time.perf_counter(): punkt czasu, odjęcie dwóch odczytów daje sekundy.
- random.randint(a,b): liczby do osobnej próby generowania.
- lista.sort() lub sorted(lista): sortowanie; zapamiętaj, co dokładnie mierzysz.
- statistics.median(czasy): porównanie 5 powtórzeń; f'{czas:.6f}': 6 cyfr po kropce.

Małe przykłady składni — nie są całym rozwiązaniem
    import time
    start = time.perf_counter()
    # W tym miejscu wykonuje się mierzona operacja.
    elapsed = time.perf_counter() - start
    print(f'{elapsed:.6f}')

Inny sposób / wariant bez własnych funkcji
Własne funkcje są opcjonalne, można powtórzyć operacje w pętli for. W tym ćwiczeniu sumuj listę i krotkę ręcznie, a nie przez sum(). Do mediany 5 pomiarów można też posortować czasy i wziąć środkowy element.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Utwórz listę i krotkę liczb 1..100000. Osobno zmierz pętle ręcznego sumowania przez time.perf_counter(); utworzenie danych ma być przed startem pomiaru. Następnie zmierz generowanie 100000 liczb randint(1,100000) i sortowanie tej listy oddzielnie. Wypisz sumy oraz 4 czasy z 6 miejscami. Powtórz 5 razy i porównaj mediany czasów; nie zakładaj, że krotka zawsze będzie szybsza.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Obie sumy muszą wynosić 5000050000. Czasy są zależne od komputera i nie mają jednego oczekiwanego wyniku.

SPRAWDŹ TAKŻE
Start i stop każdej operacji; sortowanie kolejnej próby ma otrzymać nieposortowane dane.

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
DZIEŃ 3 — ZADANIE 13: Podsumowanie transakcji w słowniku
Tematyka: Podsumowanie transakcji w słowniku.
Źródło: Lab05/01 Data structures/05 - dicts.py; Lab06/zad02.py, zad12.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: aggregate(rows). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(input()), input().split(): liczba rekordów i trzy pola wiersza.
- int(ilosc), int(cena), *: wartość w groszach; nazwa produktu pozostaje str.
- totals={}, totals.get(name,0): słownik sum według produktu.
- sorted(totals): produkty alfabetycznie; totals.values(): kwoty.
- sum(totals.values()) albo zmienna sumująca: łączna wartość; print(name,value): wiersz.

Małe przykłady składni — nie są całym rozwiązaniem
    totals = {'rower': 100}
    print(totals.get('kask', 0))  # 0
    print(*sorted(totals))  # rower

Inny sposób / wariant bez własnych funkcji
Bez get() stosuj if name in totals. Bez sum() policz sumę pętlą. Bez własnej funkcji też można uzyskać raport, ale końcowo aggregate ma zwrócić słownik; wypisywanie wykonaj poza nią.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Wczytaj n, potem n wierszy "produkt liczba_sztuk cena_grosze". Nazwy są pojedynczymi wyrazami; ilości i ceny to nieujemne int. Sumuj wartość każdego produktu w groszach, nawet gdy powtarza się z inną ceną. Wypisz produkty alfabetycznie w formacie "nazwa wartosc_grosze", a na końcu "SUMA wszystkie_grosze". Funkcja aggregate(rows) zwraca słownik.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / sok 2 350 / chleb 1 400 / sok 1 300 -> chleb 400 / sok 1000 / SUMA 1400.

SPRAWDŹ TAKŻE
n=0 -> SUMA 0; zero sztuk; powtarzający się produkt; unikaj pieniędzy zapisanych jako float.

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
DZIEŃ 3 — ZADANIE 14: Analiza gry z podanych rzutów
Tematyka: Analiza gry z podanych rzutów.
Źródło: Lab03/zad09.py; Lab04/zad06.py, zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), map(int,input().split()): liczba partii i wyniki graczy.
- if/elif/else, and, >, ==: reguły rozstrzygania; sprawdź wspólne przekroczenie przed wyborem zwycięzcy.
- Liczniki += 1 albo słownik liczników: podsumowanie czterech etykiet.
- Osobna gra: import random, random.randint(1,100), while, break, licznik prób.

Małe przykłady składni — nie są całym rozwiązaniem
    counts = {'A': 0, 'B': 0}
    counts['A'] += 1
    print(counts['A'], counts['B'])  # 1 0

Inny sposób / wariant bez własnych funkcji
Możesz użyć czterech zwykłych liczników bez słownika, a obie części napisać bez def. Funkcja do oceny partii jest opcjonalna. Grę w zgadywanie uruchamiaj osobno od analizy zapisanych partii.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Dane są już rozegrane: wczytaj n, potem n linii "wynik_A wynik_B" (0..36). Wynik >21 przegrywa; jeśli obaj przekroczyli 21, wynik partii OBAJ; gdy tylko jeden przekroczył, wygrywa drugi; inaczej większy wygrywa, równe to REMIS. Wypisz wynik każdej partii (A/B/OBAJ/REMIS), a na końcu cztery liczniki w tej kolejności. Następnie osobno napisz grę w zgadywanie z losowaniem 1..100 i licznikiem prób; nie łącz wyjść obu programów.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / 22 20 / 21 21 / 25 30 -> B / REMIS / OBAJ / 0 1 1 1.

SPRAWDŹ TAKŻE
n=0; dwa przekroczenia nie oznaczają remisu; dokładnie 21 jest poprawne.

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
DZIEŃ 3 — ZADANIE 15: Zadanie przekrojowe: raport o liście
Tematyka: Zadanie przekrojowe: raport o liście.
Źródło: Lab03/zad05.py; Lab06/zad01.py, zad11.py, zad19.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 30 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: report(data); wykorzystaj także wcześniejsze funkcje pomocnicze. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import lub from ... import ...: własne wcześniejsze funkcje; ich pliki muszą być dostępne w projekcie.
- is_prime, square_pairs i wcześniejszy klucz sortowania: części obliczeń.
- Słownik {'nazwa':wartosc}, indeksowanie po kluczu, return: zebranie trzech wyników.
- f'{a}:{b}': tekst pary; ' '.join(fragmenty): połączenie gotowych napisów.
- print(*liczby) wypisuje listę liczb; if not wynik obsługuje pustą kategorię.

Małe przykłady składni — nie są całym rozwiązaniem
    a, b = 4, 16
    piece = f'{a}:{b}'
    print(' '.join([piece, '5:25']))  # 4:16 5:25

Inny sposób / wariant bez własnych funkcji
Nie musisz używać list comprehension ani lambda: wystarczą pętle, append i nazwana funkcja klucza. Ten raport można policzyć wprost, ale końcowa wersja ma ćwiczyć report i ponowne użycie funkcji, a nie wklejenie kilku programów konsolowych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja report(data) zwraca słownik z kluczami: primes (wszystkie pierwsze z zachowaniem duplikatów i kolejności), pairs (unikalne sąsiednie pary (a,a**2), kolejność pierwszego wystąpienia), ordered (różne nieparzyste rosnąco, następnie różne parzyste rosnąco). Wczytaj listę int i wypisz 3 linie: primes rozdzielone spacją, pairs jako a:b rozdzielone spacją, ordered rozdzielone spacją. Każdą pustą kategorię oznacz BRAK. Wykorzystaj własne wcześniejsze funkcje zamiast kopiować całe programy z input().

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2 4 3 9 2 4 -> 2 3 2 / 2:4 3:9 / 3 9 2 4.

SPRAWDŹ TAKŻE
Puste dane; 0 0; liczby ujemne; uruchomienie modułów importowanych bez efektów ubocznych.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
```

