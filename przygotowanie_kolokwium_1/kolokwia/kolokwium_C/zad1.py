"""
KOLOKWIUM C — ZADANIE 1: Konwersja temperatury
Tematyka: Konwersja temperatury.
Źródło: Lab04/zad03.py (względem Labs/ w Labs.zip).
Sugerowany czas: 10 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input().upper(): C/F niezależnie od wielkości liter; int(input()): temperatura.
- if/else i operatory *, /, +, -: wybranie kierunku i przeliczenie.
- print(f'{wynik:.2f}'): dokładnie dwie cyfry po kropce.
- round(wynik,2)==0 i przypisanie 0.0: normalizacja ujemnego zera.

Małe przykłady składni — nie są całym rozwiązaniem
    print('f'.upper())  # F
    value = 12.5
    print(f'{value:.2f}')  # 12.50

Inny sposób / wariant bez własnych funkcji
Nie potrzeba modułów ani własnych funkcji. c_to_f/f_to_c są opcjonalnym podziałem programu. Zamiast f-stringa możesz użyć format(wynik,'.2f'); samo round nie dopisuje zer na wyjściu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj w pierwszej linii literę C lub F (może być mała), w drugiej liczbę całkowitą -100..100. C oznacza, że wejście jest w Celsjuszach i należy przeliczyć je na Fahrenheity; F oznacza odwrotnie. F=C*9/5+32. Wypisz sam wynik z 2 miejscami po kropce. Zaokrąglone zero zapisuj 0.00.

WEJŚCIE PRZYKŁADOWE
c
20

WYJŚCIE PRZYKŁADOWE
68.00

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
