# Próbne kolokwia

[A](kolokwium_A/README.md) · [B](kolokwium_B/README.md) · [C](kolokwium_C/README.md) · [D — zapas](kolokwium_D/README.md)

Każdy arkusz ma 5 plików `zad1.py`–`zad5.py`, własny `sprawdz.py` i `testy.json`. Wspólny silnik znajduje się w `../narzedzia/sprawdzarka.py`. Zachowaj strukturę folderów przy pobieraniu zestawu. Nie ma bibliotek do instalowania.

## Uruchamianie

Z katalogu głównego repozytorium:

```console
python przygotowanie_kolokwium_1/kolokwia/kolokwium_A/sprawdz.py
python przygotowanie_kolokwium_1/kolokwia/kolokwium_B/sprawdz.py
python przygotowanie_kolokwium_1/kolokwia/kolokwium_C/sprawdz.py
python przygotowanie_kolokwium_1/kolokwia/kolokwium_D/sprawdz.py
```

Z folderu wybranego arkusza wystarczy `python sprawdz.py`. W PyCharm uruchom `sprawdz.py` zwykłym Run. Skrypt sam odnajdzie testy i domyślnie pliki z zadaniami, niezależnie od bieżącego katalogu terminala.

Sprawdzanie jednego zadania (diagnostyka bez oceny całego arkusza):

```console
python sprawdz.py --task 3
```

Wszystkie błędne przypadki zamiast pierwszego:

```console
python sprawdz.py --details
```

Jeśli rozwiązania piszesz w osobnym projekcie, podaj folder zawierający bezpośrednio `zad1.py`–`zad5.py`:

```console
python sprawdz.py --solutions-dir "C:/Nazwisko Imie 123456"
```

Domyślny limit to 2 sekundy **na pojedynczy test**, a nie na cały arkusz. Na wolniejszym komputerze można użyć `--timeout 5`. To techniczny limit testera, niezwiązany z 75 minutami rozwiązywania.

## Co jest sprawdzane

Tester uruchamia każdy program osobno dla każdego przypadku. Przekazuje dane na stdin i porównuje stdout z oczekiwaniem. Uwzględnia też brak pliku, błędy składni/wyjątki, niezerowy kod zakończenia, przekroczenie czasu i wyjście większe niż 1 MiB. Uruchomienia otrzymują kodowanie UTF-8.

Porównanie zachowuje **liczbę i kolejność wierszy oraz treść tokenów**. Ignoruje liczbę spacji/tabulatorów pomiędzy tokenami w jednym wierszu oraz odstępy na końcu wiersza. Akceptuje brak ostatniego znaku nowej linii i zakończenia Windows/Linux. Dodatkowe puste wiersze, komunikaty `Podaj...`, zmieniona wielkość liter, błędna kolejność lub `2.5` zamiast wymaganego `2.50` powodują niezaliczenie testu. Nie stosuje ukrytej tolerancji numerycznej: zaokrąglaj zgodnie z opisem.

Brak pliku lub choć jeden nieudany przypadek oznacza **0 całych zadań za ten plik**. Wynik końcowy:

| Całe zadania | Ocena | Zaliczenie |
|---:|---:|---|
| 0, 1 lub 2 | 2.0 | nie |
| 3 | 3.0 | tak |
| 4 | 4.0 | tak |
| 5 | 5.0 | tak |

Liczby zaliczonych testów służą tylko do szukania błędu. Tester nie zamienia np. połowy testów w połowę zadania. Kody zakończenia sprawdzarki: `0` — wszystkie wybrane zadania przeszły; `1` — co najmniej jedno nie przeszło (również gdy ocena całego arkusza to 3.0 lub 4.0); `2` — błąd argumentów/konfiguracji.

## Wskazówki do nauki

Wszystkie 20 plików z zadaniami ma sekcję narzędzi: składnia, funkcje/metody, małe przykłady i alternatywy. W arkuszach **nie wymaga się własnych funkcji** — można pisać kod bez `def`. Przy pierwszym podejściu możesz korzystać z tych wskazówek jako części nauki; przy próbie odtwarzającej warunki kolokwium pomiń je i przeczytaj samo polecenie. [Jak czytać wskazówki](../JAK_CZYTAC_WSKAZOWKI.md).

## Tryb uczciwej próby

Przez 75 minut nie czytaj `testy.json`, nie uruchamiaj sprawdzarki i nie poprawiaj programu na podstawie jej wskazówek. Możesz uruchamiać własne programy na przykładach z poleceń i samodzielnie wymyślonych danych. Po upływie czasu przygotuj ZIP w 5 minut; dopiero później uruchom testy. Zapisz wynik przed poprawkami i po poprawkach oddzielnie.

Testy są jawne do nauki i zawierają łącznie **215 przypadków**. Pokrywają przykłady, typowe błędy i granice, lecz nie dowodzą poprawności dla każdego możliwego wejścia. Ocena jest treningowa. Dobór tematów wynika z laboratoriów, nie z informacji o rzeczywistych pytaniach.

## Kontrola samej sprawdzarki

Opcjonalnie, z katalogu głównego repozytorium:

```console
python -m unittest discover -s przygotowanie_kolokwium_1/narzedzia -v
```

Te 16 testów narzędzia sprawdza m.in. wszystkie progi ocen, brak punktów za częściowo poprawne zadanie, błędy programu, kodowanie, limity i format porównania. Nie zawierają rozwiązań arkuszy.
