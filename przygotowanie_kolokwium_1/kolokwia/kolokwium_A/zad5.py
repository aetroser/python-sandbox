"""
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
"""

# Tutaj napisz swoje rozwiązanie.
