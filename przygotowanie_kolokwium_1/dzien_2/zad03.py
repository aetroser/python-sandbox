"""
DZIEŃ 2 — ZADANIE 03: Operacje na liście i indeksy wystąpień
Tematyka: Operacje na liście i indeksy wystąpień.
Źródło: Lab05/01 Data structures/02–03; Lab06/zad11.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): odczyt listy, int(input()): szukana wartość.
- enumerate(lista): pary (indeks,wartość); append(): zbieranie pasujących indeksów.
- x in lista: bezpieczne sprawdzenie przed lista.remove(x), które usuwa pierwsze wystąpienie.
- sorted(lista): posortowana kopia; print(*lista): liczby bez nawiasów.
- if not lista: przypadek pustego wyniku.

Małe przykłady składni — nie są całym rozwiązaniem
    for index, value in enumerate([10, 20]):
        print(index, value)  # wiersze: 0 10 oraz 1 20
    print(*[6, 8])  # 6 8, bez nawiasów

Inny sposób / wariant bez własnych funkcji
Zamiast enumerate możesz użyć for i in range(len(lista)) albo while z indeksem. Usunięcie można wykonać przez znalezienie indeksu i del lista[i]. Własne funkcje są opcjonalne.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepustą listę int z jednej linii i x z drugiej. Wypisz indeksy wszystkich x albo BRAK. Następnie usuń tylko pierwsze wystąpienie x, jeśli istnieje, i wypisz pozostałe elementy albo PUSTA. W trzeciej linii wypisz posortowaną kopię po usunięciu. Nie zmieniaj kolejności oryginalnych pozostałych elementów w drugiej linii.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Lista 7 2 7 1, x=7: 0 2 / 2 7 1 / 1 2 7.

SPRAWDŹ TAKŻE
Brak x; tylko jeden element równy x; kolejne duplikaty.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
