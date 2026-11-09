"""
DZIEŃ 3 — ZADANIE 13: Podsumowanie transakcji w słowniku
Tematyka: Podsumowanie transakcji w słowniku.
Źródło: Lab05/01 Data structures/05 - dicts.py; Lab06/zad02.py, zad12.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: aggregate(rows). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(input()), input().split(): liczba rekordów i trzy pola wiersza.
- int(ilosc), int(cena), *: wartość w groszach; nazwa produktu pozostaje str.
- totals={}, totals.get(name,0): słownik sum według produktu.
- sorted(totals): produkty alfabetycznie; totals.values(): kwoty.
- sum(totals.values()) albo zmienna sumująca: łączna wartość; print(name,value): wiersz.

Małe przykłady składni — nie są całym rozwiązaniem
    totals = {'rower': 100}
    print(totals.get('kask', 0))  # 0
    print(*sorted(totals))  # rower

Inny sposób / wariant bez własnych funkcji
Bez get() stosuj if name in totals. Bez sum() policz sumę pętlą. Bez własnej funkcji też można uzyskać raport, ale końcowo aggregate ma zwrócić słownik; wypisywanie wykonaj poza nią.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Wczytaj n, potem n wierszy "produkt liczba_sztuk cena_grosze". Nazwy są pojedynczymi wyrazami; ilości i ceny to nieujemne int. Sumuj wartość każdego produktu w groszach, nawet gdy powtarza się z inną ceną. Wypisz produkty alfabetycznie w formacie "nazwa wartosc_grosze", a na końcu "SUMA wszystkie_grosze". Funkcja aggregate(rows) zwraca słownik.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / sok 2 350 / chleb 1 400 / sok 1 300 -> chleb 400 / sok 1000 / SUMA 1400.

SPRAWDŹ TAKŻE
n=0 -> SUMA 0; zero sztuk; powtarzający się produkt; unikaj pieniędzy zapisanych jako float.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
