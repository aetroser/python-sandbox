"""
KOLOKWIUM B — ZADANIE 5: Dzień tygodnia i luty
Tematyka: Dzień tygodnia i luty.
Źródło: Lab06/zad06.py, zad14.py, zad17.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- from datetime import date; date.fromisoformat(input()): data z tekstu.
- d.weekday() daje 0..6; lista/krotka polskich nazw i [indeks] wybierają napis.
- import calendar; calendar.isleap(d.year): informacja o roku przestępnym.
- if/else: wybór liczby dni lutego; print(): dwa osobne wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import date
    import calendar
    print(date(2020, 1, 6).weekday())  # 0
    print(calendar.isleap(2020))  # True

Inny sposób / wariant bez własnych funkcji
Nie musisz pisać day_of_week ani days_in_february. Bez isleap() użyj podzielności przez 4, 100 i 400. Bez listy nazw możesz użyć if/elif; nie polegaj na strftime('%A'), bo język nazwy zależy od ustawień systemu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj poprawną datę RRRR-MM-DD (rok 1900..2100). W pierwszej linii wypisz polską nazwę dnia tygodnia małymi literami z polskimi znakami (poniedziałek, wtorek, środa, czwartek, piątek, sobota, niedziela). W drugiej wypisz liczbę dni lutego w roku wczytanej daty. Nie korzystaj z języka systemu ani bieżącej daty.

WEJŚCIE PRZYKŁADOWE
2024-02-29

WYJŚCIE PRZYKŁADOWE
czwartek
29

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
