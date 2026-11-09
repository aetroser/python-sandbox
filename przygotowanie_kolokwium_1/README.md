# Przygotowanie do I kolokwium — Programowanie skryptowe

Zestaw na podstawie **całego przesłanego `Labs.zip` (Lab02–Lab06)** i podanych zasad kolokwium. Zadania są nowymi wariantami, z doprecyzowanym wejściem, wyjściem i przypadkami brzegowymi. Pliki zawierają polecenia i miejsce na własny kod. **Nie zawierają rozwiązań.**

- [Jak czytać wskazówki: funkcje, metody, formatowanie](JAK_CZYTAC_WSKAZOWKI.md)
- [Plan na wtorek–czwartek, 10–12 listopada 2026](PLAN_3_DNI.md)
- [Mapa materiału i źródła](ZAKRES_I_ZRODLA.md)
- [Krótka lista rzeczy do powtórzenia](POWTORKA.md)
- [Dziennik błędów i wyników](POSTEPY.md)
- [Próbne kolokwia i uruchamianie testerów](kolokwia/README.md)

## Co jest w środku

| Część | Tematy | Liczba |
|---|---|---:|
| [Dzień 1](dzien_1/README.md) | wejście, pętle, funkcje, liczby, moduły, losowanie | 15 |
| [Dzień 2](dzien_2/README.md) | napisy, listy, krotki, słowniki, zbiory, okna listy | 15 |
| [Dzień 3](dzien_3/README.md) | daty, statystyka, progi, reguły, zadania łączone | 15 |
| [Kolokwium A](kolokwia/kolokwium_A/README.md) | przedział, równanie, trójki, słowa, wiek | 5 |
| [Kolokwium B](kolokwia/kolokwium_B/README.md) | pętla do zera, adresy, pary, statystyki, kalendarz | 5 |
| [Kolokwium C](kolokwia/kolokwium_C/README.md) | temperatura, sortowanie, słownik, rzuty, urodziny | 5 |
| [Kolokwium D — zapas](kolokwia/kolokwium_D/README.md) | pierwsze, trójki bez nakładania, książka, progi, suma pól | 5 |

W każdym dniu zadania **01–11 to podstawa**, **12–15 to rozszerzenia ★ i zapas**. Jest łącznie 33 ćwiczeń podstawowych, 12 rozszerzeń i 20 zadań w arkuszach. Nie musisz kończyć wszystkich rozszerzeń przed piątkiem. Priorytet: samodzielnie rozwiązać i sprawdzić co najmniej trzy pełne zadania w 75 minut.

## Wskazówki w każdym zadaniu

Na górze każdego pliku znajdziesz: informację, czy trzeba pisać własne funkcje `def`; listę przydatnych funkcji, metod i konstrukcji z objaśnieniami; krótkie przykłady składni; warianty alternatywne, w tym rozwiązanie bez własnej funkcji, gdy jest dozwolone. Przykłady pokazują pojedyncze operacje, a cały program nadal piszesz samodzielnie. [Wyjaśnienie od podstaw](JAK_CZYTAC_WSKAZOWKI.md).

## Jak zacząć

Potrzebny jest Python **3.10 lub nowszy** i zwykły edytor/PyCharm. Brak dodatkowych pakietów. Pobierz lub sklonuj repozytorium. W Windows poniższe `python` możesz zastąpić `py -3`, jeśli tak uruchamiasz interpreter. W razie problemów z polskimi znakami użyj `python -X utf8`.

Z katalogu głównego repozytorium uruchom ćwiczenie:

```console
python przygotowanie_kolokwium_1/dzien_1/zad01.py
```

Otwórz plik i czytaj opis na samej górze. Kod wpisuj pod opisem. Gdy zadanie wymaga wyłącznie funkcji, dopisz przykłady pod `if __name__ == '__main__':`.

Po samodzielnym rozwiązaniu arkusza uruchom:

```console
python przygotowanie_kolokwium_1/kolokwia/kolokwium_A/sprawdz.py
```

Puste szablony **celowo nie przechodzą testów**. Testery są do próbnych kolokwiów; codzienne ćwiczenia mają przykłady i listę sprawdzeń ręcznych.

## Reguły próbnych kolokwiów

- 5 niezależnych plików: `zad1.py`–`zad5.py`.
- 75 minut rozwiązywania i dodatkowe 5 minut na pakowanie/wgranie.
- 0–2 zadania w całości: **2.0**; 3: **3.0**; 4: **4.0**; 5: **5.0**.
- Jeden nieudany test oznacza, że zadanie nie jest jeszcze zaliczone. Liczba udanych testów jest informacją do poprawy, nie ułamkiem zaliczonego zadania.
- W czasie próby korzystaj tylko z [python.org](https://www.python.org/) / [oficjalnej dokumentacji](https://docs.python.org/3/) i [W3Schools Python](https://www.w3schools.com/python/), zgodnie z opisem prowadzącego. Nie zaglądaj do testów, innych rozwiązań ani wyników sprawdzarki przed końcem 75 minut.

Dobór zadań w arkuszach jest **oszacowaniem na podstawie laboratoriów**, a nie znajomością pytań prowadzącego. Rzeczywiste zadania mogą mieć inne wejście, komunikaty i wymagania. Wtedy pierwszeństwo ma treść zadania na kolokwium.
