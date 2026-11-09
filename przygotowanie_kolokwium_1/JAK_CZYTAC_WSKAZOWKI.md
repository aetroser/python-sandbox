# Jak korzystać ze wskazówek do zadań

Każdy z 65 plików z zadaniami ma tylko 6 wierszy opisu: temat/lab, polecenie, wymaganie dotyczące własnych funkcji, wejście, wynik i przydatne narzędzia. Znak `/` w przykładzie oznacza następny wiersz. Poniższe wyjaśnienia są opcjonalną pomocą, poza plikami z zadaniami. Szczegółowe wcześniejsze opisy są w plikach `POMOC.md` przy poszczególnych dniach i arkuszach.

## Co znaczy „bez funkcji”

W tych opisach **„bez własnych funkcji” oznacza bez pisania `def`**. Nadal możesz używać `input()`, `print()`, `int()` i innych operacji dostępnych w języku.

| Rodzaj | Przykład | Do czego służy |
|---|---|---|
| Funkcja wbudowana | `len(tekst)` | Jest dostępna bez importu; tutaj daje długość tekstu. |
| Metoda obiektu | `tekst.lower()` | Wywołujesz ją po kropce na danej wartości; tutaj daje tekst małymi literami. |
| Funkcja z modułu | `math.sqrt(liczba)` | Najpierw wykonujesz `import math`; tutaj obliczasz pierwiastek. |
| Własna funkcja | `def nazwa(argument):` | Samodzielnie definiujesz obliczenia, do których potem wracasz przez wywołanie. |
| Konstrukcja języka | `if`, `for`, `while` | Steruje wykonaniem programu; to nie są funkcje. |

Jeżeli zadanie wymaga własnej funkcji, jest to zaznaczone w trzecim wierszu opisu. Możesz najpierw przećwiczyć rachunek bez niej, ale końcową wersję zrób zgodnie z wymaganiem. Jeżeli funkcja jest opcjonalna, możesz napisać program bezpośrednio pod opisem zadania.

Krótki przykład własnej funkcji, niezwiązany z rozwiązaniem zadań:

```python
def double(value):
    return value * 2

result = double(7)
print(result)
```

`value` jest parametrem. `return` przekazuje wynik do miejsca wywołania, a `print` wypisuje go na ekranie. Wcięcie po `def` oznacza wnętrze funkcji. Zapis `double` to nazwa funkcji, a `double(7)` to jej wywołanie.

## Liczby z określoną liczbą cyfr po kropce

```python
x = 8.5
print(f'{x:.2f}')  # 8.50
print(f'{x:.4f}')  # 8.5000
```

- Litera `f` przed napisem pozwala wstawić do niego wartości w klamrach.
- `x` to wypisywana wartość.
- Dwukropek rozpoczyna opis formatowania.
- `.2f` oznacza zapis stałoprzecinkowy z dokładnie 2 cyframi po kropce.
- `.4f` daje 4 cyfry po kropce.

Alternatywy dla pierwszego zapisu:

```python
print(format(x, '.2f'))
print('{:.2f}'.format(x))
```

Wybierz jedną wersję; nie wypisuj wszystkich trzech w rozwiązaniu. Formatowanie zmienia tekst wyjściowy, nie wartość zmiennej `x`.

`round(x, 2)` zwraca zaokrągloną liczbę. Nie określa liczby wypisanych cyfr — `print(round(8.5, 2))` daje `8.5`, a nie `8.50`. Dlatego w zadaniach z wymaganym formatem stosuj formatowanie.

## Jak przeczytać listę narzędzi

1. Sprawdź, czy własna funkcja i konkretny sposób rozwiązania są wymagane.
2. Przeczytaj objaśnienia operacji potrzebnych w danym zadaniu.
3. Uruchom krótki przykład składni osobno, aby zobaczyć jego działanie.
4. Zastosuj poznane operacje we własnym rozwiązaniu polecenia.
5. Alternatywy traktuj jako inne drogi, a nie dodatkowe rzeczy do obowiązkowego użycia.

Przykłady w opisach są tekstem wewnątrz docstringa, czyli wielowierszowego opisu pomiędzy potrójnymi cudzysłowami. **Nie wykonują się po uruchomieniu zadania.** Kod rozwiązania wpisz pod zamykającymi potrójnymi cudzysłowami. Gdy chcesz wypróbować mały przykład, skopiuj go do osobnego pliku lub konsoli Pythona.

## Wskazówki a próbne kolokwium

W trybie nauki korzystaj ze wskazówek również w arkuszach A–D. Przy kolejnej próbie na czas możesz pominąć wiersz „Przydatne” i oprzeć się tylko na samym poleceniu oraz dozwolonej dokumentacji. Zasady wejścia, wyjścia i oceniania pozostają opisane w arkuszu.

Źródła składni: [oficjalny tutorial — wejście i wyjście](https://docs.python.org/3/tutorial/inputoutput.html), [funkcje i sterowanie](https://docs.python.org/3/tutorial/controlflow.html), [typy wbudowane](https://docs.python.org/3/library/stdtypes.html).
