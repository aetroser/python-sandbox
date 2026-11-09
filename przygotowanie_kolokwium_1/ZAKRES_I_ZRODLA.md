# Zakres, pochodzenie i źródła

Materiał wejściowy: załączony `Labs.zip`, przejrzany plik po pliku (łącznie **80 plików Python**). Zakres: **Lab02, Lab03, Lab04, Lab05 i Lab06**; w archiwum nie ma Lab01. Nie korzystano z innego podręcznika ani repozytorium jako źródła zadań. Nowe warianty i przykłady zostały opracowane dla tego zestawu.

| Oryginalny materiał | Najważniejsze zagadnienia | Ćwiczenia | Arkusze |
|---|---|---|---|
| Lab02/zad01–zad06 | input, typy, while/for, pętle zagnieżdżone, break/continue | dzień 1: 01–05 | A1, B1 |
| Lab02/zad07–zad08 i zadania do realizacji | random, kości, konwersje, BMI | dzień 1: 08–09, ★13–★14 | C1, C4 |
| Lab03/zad01–zad05 | funkcje, import, parzystość, sumy, pierwsze | dzień 1: 05–06, 11 | A1, D1 |
| Lab03/zad06–zad08 | tekst, tabliczka, równanie rzeczywiste | dzień 1: 04,10; dzień 2: 07 | A2, A4 |
| Lab03/zad09 (dodatkowe) | gra w oczko i zestawienie wyników | dzień 3: ★14 | C4 — pokrewny motyw analizy rund |
| Lab04/zad01–zad04 | zespolone, konwersje, BMI, warunki | dzień 1: 08–10, ★12 | A2, C1 |
| Lab04/zad05–zad10 | losowanie, zgadywanie, funkcje, suma pól, silnia, czas | dzień 1: 07, ★12–★15; dzień 3: ★12, ★14 | C4, D5 |
| Lab05/01 Data structures | list, tuple, dict, set, kopie, join/split | dzień 2: 01–04,08–10,★14–★15 | B2, C2–C3, D3 |
| Lab05/02 Strings | konkatenacja, indeksy, slicing, metody, formatowanie | dzień 2: 01,05–07 | A4 |
| Lab05/03 Zadania (do przesłania)/zad01–zad04 | adresy, duplikaty, trójki z/bez nakładania | dzień 2: 10–11, ★12 | A3, B2, D2 |
| Lab05/03 Zadania (do przesłania)/zad05–zad09 | calendar, datetime, znaki, wiek, dni do daty | dzień 2: 09; dzień 3: 01,03–04,07 | A5, C5 |
| Lab06/zad01–zad04 | pary, typy, statistics, pomiar czasu | dzień 2: ★13–★14; dzień 3: 08–09,★12 | B3–B4 |
| Lab06/zad05–zad10 | data/czas, weekday, wiek, dni, oceny, reguły | dzień 3: 01–04,10–11 | A5, B5, D4 |
| Lab06/zad11–zad20 | operacje list, sortowanie, tygodnie, kalendarz, napisy | dzień 2: 03,05–06,★15; dzień 3: 04–07,★15 | B5, C2, C5 |

## Doprecyzowania względem oryginału

- Rozdzielono **treść poleceń** od kodu znajdującego się w części plików. Przykładowy istniejący kod nie zawsze realizuje opis, np. odliczanie zamiast liczb od 1 lub zliczanie jedynek z różnych rzutów zamiast jednoczesnego wyniku.
- Poprawiono nazwę `randinit` na `randint`. `random()` daje float, więc do losowania całkowitych wskazano właściwe funkcje.
- W oknach listy zapisano wprost, czy elementy mogą być wykorzystane ponownie. Naprawiono niepoprawny zapis przykładowej listy z podwójnym przecinkiem.
- Ustalono normalizację słów, rozstrzyganie remisów, kolejność wyników i znaczenie „unikalnych znaków”.
- Ustalono zachowanie przy `bool` wśród `int`, pustych danych i datach 29 lutego. W testach daty są podawane na wejściu; nie zmieniają się z zegarem komputera.
- Dla losowań przyjęto limit zakończenia. Arkusz C analizuje dostarczone rzuty zamiast zależeć od konkretnej sekwencji pseudolosowej.
- W Lab04 opis losowania parzystych z limitem sumy jest niejednoznaczny; nowy wariant ★14 jasno mówi „aż suma >= target lub limit prób”. To doprecyzowany wariant, nie dosłowna kopia niejasnego warunku.
- W Lab06/zad20.py dwa razy zapisano duże litery; w ćwiczeniu rozdzielono duże, małe, spacje i pozostałe znaki.
- Progi ocen w ćwiczeniu z Lab06 zdefiniowano jako **ściśle większe** niż 50/60/80%. To inna zasada niż ocena prawdziwego kolokwium liczbą całych zadań.
- Dodatkowe `eval`, szubienica i kółko i krzyżyk z Lab04/zad11–zad13 nie są priorytetem na trzy dni; ich motywy rozwijają opcjonalne zadania z funkcji i gier. Nie wymagamy implementacji tych pełnych gier.

## Dokumentacja do nauki i weryfikacji

Pierwszeństwo ma oficjalna dokumentacja Pythona. Użyte operacje są dostępne w Pythonie 3.10+; zestaw nie wymaga nowych mechanizmów z najnowszej wersji dokumentacji.

- [Tutorial: sterowanie, funkcje](https://docs.python.org/3/tutorial/controlflow.html)
- [Tutorial: moduły i import](https://docs.python.org/3/tutorial/modules.html)
- [Tutorial: struktury danych](https://docs.python.org/3/tutorial/datastructures.html)
- [Typy wbudowane, napisy, sortowanie](https://docs.python.org/3/library/stdtypes.html)
- [Funkcje wbudowane](https://docs.python.org/3/library/functions.html)
- [random](https://docs.python.org/3/library/random.html)
- [math](https://docs.python.org/3/library/math.html) i [cmath](https://docs.python.org/3/library/cmath.html)
- [datetime: date, datetime, timedelta](https://docs.python.org/3/library/datetime.html)
- [calendar](https://docs.python.org/3/library/calendar.html)
- [statistics](https://docs.python.org/3/library/statistics.html)
- [time.perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter)
- [W3Schools Python — drugie dozwolone źródło na kolokwium](https://www.w3schools.com/python/)

Nie ma podstaw do przewidzenia konkretnych pytań. Arkusze mieszają najczęstsze konstrukcje z dostarczonych laboratoriów, a zadania ★ obejmują dłuższe tematy i zapas.

## Inwentarz przejrzanego archiwum

Suma SHA-256 pliku wejściowego: `8d6b9c3192302d2f208947549b3b481d6c5aa5703153000b810ece5dbdbb5afe`.

### Lab02

- `Lab02/zad01.py`
- `Lab02/zad02.py`
- `Lab02/zad03.py`
- `Lab02/zad04.py`
- `Lab02/zad05.py`
- `Lab02/zad06.py`
- `Lab02/zad07.py`
- `Lab02/zad08.py`
- `Lab02/zadania do realizacji.py`

### Lab03

- `Lab03/zad01.py`
- `Lab03/zad02.py`
- `Lab03/zad03.py`
- `Lab03/zad04.py`
- `Lab03/zad05.py`
- `Lab03/zad06.py`
- `Lab03/zad07.py`
- `Lab03/zad08.py`
- `Lab03/zad09.py`

### Lab04

- `Lab04/zad01.py`
- `Lab04/zad02.py`
- `Lab04/zad03.py`
- `Lab04/zad04.py`
- `Lab04/zad05.py`
- `Lab04/zad06.py`
- `Lab04/zad07.py`
- `Lab04/zad08.py`
- `Lab04/zad09.py`
- `Lab04/zad10.py`
- `Lab04/zad11.py`
- `Lab04/zad12.py`
- `Lab04/zad13.py`

### Lab05

- `Lab05/01 Data structures/01 - lists.py`
- `Lab05/01 Data structures/02 - list_operations.py`
- `Lab05/01 Data structures/03 - list_items.py`
- `Lab05/01 Data structures/04 - tuples.py`
- `Lab05/01 Data structures/05 - dicts.py`
- `Lab05/01 Data structures/06 - dict_key_value.py`
- `Lab05/01 Data structures/07 - in_keyword.py`
- `Lab05/01 Data structures/08 - basic operations on lists.py`
- `Lab05/01 Data structures/09 - join split.py`
- `Lab05/01 Data structures/10 - set.py`
- `Lab05/02 Strings/01 - concatenation.py`
- `Lab05/02 Strings/02 - string_multiplication.py`
- `Lab05/02 Strings/03 - string_indexing.py`
- `Lab05/02 Strings/04 - negative_indexing.py`
- `Lab05/02 Strings/05 - slicing.py`
- `Lab05/02 Strings/06 - in_operator.py`
- `Lab05/02 Strings/07 - len_function.py`
- `Lab05/02 Strings/08 - character_escaping.py`
- `Lab05/02 Strings/09 - string_methods.py`
- `Lab05/02 Strings/10 - string_formatting.py`
- `Lab05/03 Zadania (do przesłania)/zad01.py`
- `Lab05/03 Zadania (do przesłania)/zad02.py`
- `Lab05/03 Zadania (do przesłania)/zad03.py`
- `Lab05/03 Zadania (do przesłania)/zad04.py`
- `Lab05/03 Zadania (do przesłania)/zad05.py`
- `Lab05/03 Zadania (do przesłania)/zad06.py`
- `Lab05/03 Zadania (do przesłania)/zad07.py`
- `Lab05/03 Zadania (do przesłania)/zad08.py`
- `Lab05/03 Zadania (do przesłania)/zad09.py`

### Lab06

- `Lab06/zad01.py`
- `Lab06/zad02.py`
- `Lab06/zad03.py`
- `Lab06/zad04.py`
- `Lab06/zad05.py`
- `Lab06/zad06.py`
- `Lab06/zad07.py`
- `Lab06/zad08.py`
- `Lab06/zad09.py`
- `Lab06/zad10.py`
- `Lab06/zad11.py`
- `Lab06/zad12.py`
- `Lab06/zad13.py`
- `Lab06/zad14.py`
- `Lab06/zad15.py`
- `Lab06/zad16.py`
- `Lab06/zad17.py`
- `Lab06/zad18.py`
- `Lab06/zad19.py`
- `Lab06/zad20.py`

