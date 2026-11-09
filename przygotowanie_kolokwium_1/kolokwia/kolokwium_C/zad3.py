"""
KOLOKWIUM C — ZADANIE 3: Zestawienie sprzedaży
Tematyka: Zestawienie sprzedaży.
Źródło: Lab05/01 Data structures/05 - dicts.py; Lab06/zad02.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), input().split(): liczba rekordów i trzy pola.
- int(ilosc), int(cena), *: wartość jednego rekordu w groszach.
- Slownik {}, get(nazwa,0), przypisanie: sumy dla produktów.
- sorted(slownik): klucze alfabetycznie; sum(slownik.values()): łączna kwota.
- print(nazwa,kwota), print('SUMA',kwota): wymagane wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    name, quantity, price = 'kask 2 1250'.split()
    value = int(quantity) * int(price)
    print(name, value)  # kask 2500

Inny sposób / wariant bez własnych funkcji
Nie musisz definiować aggregate. Bez get() użyj if/in, a bez sum() gromadź kwotę w zmiennej. Wystarczą int — float nie jest tu potrzebny.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n linii "produkt ilosc cena". Produkt jest niepustym wyrazem z małych liter ASCII; ilosc i cena są int 0..10000. Cena to grosze za sztukę. Zsumuj ilosc*cena dla każdego produktu. Wypisz produkty alfabetycznie, po jednym wierszu "produkt wartosc_grosze". Zachowaj też produkty o sumie 0. Na końcu zawsze wypisz "SUMA wartosc_wszystkich_groszy". Nie przeliczaj na złote.

WEJŚCIE PRZYKŁADOWE
3
sok 2 350
chleb 1 400
sok 1 300

WYJŚCIE PRZYKŁADOWE
chleb 400
sok 1000
SUMA 1400

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
