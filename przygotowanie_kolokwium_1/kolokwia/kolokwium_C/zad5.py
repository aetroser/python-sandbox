"""
KOLOKWIUM C — ZADANIE 5: Najbliższe urodziny
Tematyka: Najbliższe urodziny.
Źródło: Lab05/03 Zadania (do przesłania)/zad08.py–zad09.py; Lab06/zad08.py, zad16.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): data odniesienia.
- map(int,input().split()): miesiąc i dzień; date(rok,miesiac,dzien): data urodzin w wybranym roku.
- Porównania dat < i >= oraz if: decyzja o bieżącym albo kolejnym roku.
- d.isoformat(): RRRR-MM-DD; (d-today).days: odległość w dniach.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    candidate = date(2020, 8, 9)
    print(candidate.isoformat())  # 2020-08-09
    print(candidate.year)  # 2020

Inny sposób / wariant bez własnych funkcji
Nie musisz tworzyć własnej funkcji do urodzin. Można też przesuwać datę timedelta(days=1) aż do szukanego miesiąca/dnia, ale konstrukcja daty w wybranym roku jest krótsza. Nie korzystaj z date.today().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj datę odniesienia RRRR-MM-DD (rok 1900..2099), następnie miesiąc i dzień urodzin jako dwa int w jednej linii. Taka data istnieje w każdym roku (wykluczamy 29 lutego). Znajdź najbliższe urodziny przypadające dziś albo później. Wypisz ich datę ISO i liczbę dni od daty odniesienia w jednej linii. Dziś oznacza różnicę 0. Nie korzystaj z daty systemowej.

WEJŚCIE PRZYKŁADOWE
2026-11-12
11 13

WYJŚCIE PRZYKŁADOWE
2026-11-13 1

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
