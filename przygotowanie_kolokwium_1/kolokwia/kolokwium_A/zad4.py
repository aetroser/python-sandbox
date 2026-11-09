"""
KOLOKWIUM A — ZADANIE 4: Statystyka słów
Tematyka: Statystyka słów.
Źródło: Lab03/zad06.py; Lab05/02 Strings (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input(), replace(znak,' '), lower(), split(): przygotowanie tekstu.
- Słownik {}, get(word,0) lub if/in: liczenie słów.
- len(lista) i len(slownik): liczby słów i różnych słów.
- max(slownik.values()) oraz min()/sorted() lub pętla porównawcza: zwycięzca z remisem.
- print(slowo,licznik): ostatni wiersz dla niepustych danych.

Małe przykłady składni — nie są całym rozwiązaniem
    print('X,Y'.replace(',', ' ').lower().split())  # ['x', 'y']
    counts = {'bus': 2}
    print(counts.get('car', 0))  # 0

Inny sposób / wariant bez własnych funkcji
Możesz pisać bez def i bez Counter z dodatkowego modułu. Bez get() użyj if. Bez max/min ustal najlepszy wynik pętlą, porównując najpierw liczność, a przy remisie napis.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj linię tekstu długości 0..1000. Zastąp każdy znak z zestawu ,.!?;: spacją, zamień tekst na małe litery, a potem podziel split(). Innych znaków nie usuwaj. Wypisz w osobnych liniach: liczbę wszystkich słów; liczbę różnych słów; najczęstsze słowo i jego liczność rozdzielone spacją. Przy remisie wybierz słowo alfabetycznie najmniejsze według porządku Pythona. Gdy nie ma słów, trzecia linia to BRAK.

WEJŚCIE PRZYKŁADOWE
Kot, pies! KOT pies ala.

WYJŚCIE PRZYKŁADOWE
5
3
kot 2

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
