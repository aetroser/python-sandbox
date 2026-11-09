"""
DZIEŃ 2 — ZADANIE 08: Słownik jako książka telefoniczna
Tematyka: Słownik jako książka telefoniczna.
Źródło: Lab05/01 Data structures/05 - dicts.py–07 - in_keyword.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()) oraz input().split(): liczba wpisów i para tekstów.
- book={} oraz book[name]=number: dodanie albo aktualizacja klucza.
- book.get(name,'BRAK') lub if name in book: bezpieczne wyszukanie.
- sorted(book): klucze w porządku alfabetycznym; print(name,book[name]): wiersz wyniku.

Małe przykłady składni — nie są całym rozwiązaniem
    name, number = 'Ewa 007'.split()
    book = {}
    book[name] = number
    print(book.get('Jan', 'BRAK'))  # BRAK

Inny sposób / wariant bez własnych funkcji
Własne funkcje nie są obowiązkowe. Bez get() użyj if/in i indeksowania słownika. Numer pozostaw jako str — int('007') dałoby 7 i zgubiłoby zera.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n, potem n linii "imię numer"; numer jest tekstem, żeby zachować zera. Powtórzenie imienia aktualizuje numer. Wczytaj szukane imię; wypisz jego numer albo BRAK. Następnie wypisz wszystkie wpisy po jednym wierszu "imię numer", alfabetycznie po imieniu. Imiona to pojedyncze wyrazy, rozróżniaj wielkość liter.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / Ala 001 / Ola 222 / Ala 003 / Ala: wynik 003, potem Ala 003 i Ola 222.

SPRAWDŹ TAKŻE
n=0; aktualizacja istniejącego klucza nie zwiększa liczby wpisów; in sprawdza klucze.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
