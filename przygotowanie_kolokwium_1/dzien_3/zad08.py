"""
DZIEŃ 3 — ZADANIE 08: Średnia, mediana i moda
Tematyka: Średnia, mediana i moda.
Źródło: Lab06/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): lista liczb; import statistics.
- statistics.mean(data), statistics.median(data): średnia i mediana.
- statistics.multimode(data): lista wszystkich mod; min(...) wybiera najmniejszą z nich.
- print(f'{x:.2f}'): dokładnie 2 miejsca dla średniej/mediany; modę wypisz jako int.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.multimode([8, 8, 3, 3]))  # [8, 3]
    print(min([8, 3]))  # 3
    print(f'{2.5:.2f}')  # 2.50

Inny sposób / wariant bez własnych funkcji
Własne funkcje nie są obowiązkowe. Bez statistics średnią policz przez sum()/len(), medianę z posortowanej listy i środkowych pozycji, a mody za pomocą słownika liczności. Zamiast sum() też można użyć pętli. Przy remisie samo mode() nie gwarantuje najmniejszej wartości.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepustą listę int z jednej linii. Wypisz w 3 liniach średnią z 2 miejscami, medianę z 2 miejscami i modę jako int. Przy remisie mody wybierz najmniejszą z najczęstszych liczb; możesz użyć statistics.multimode i min. Nie zakładaj, że statistics.mode rozstrzyga remis przez najmniejszą wartość.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
4 1 4 1: 2.50 / 2.50 / 1.

SPRAWDŹ TAKŻE
Jeden element; parzysta liczba elementów; liczby ujemne; wszystkie różne.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
