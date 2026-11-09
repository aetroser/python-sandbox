"""
DZIEŃ 1 — ZADANIE 15: Przybliżenie całki prostokątami
Tematyka: Przybliżenie całki prostokątami.
Źródło: Lab04/zad08.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

POLECENIE
★ Funkcja rectangle_sum(a,b,n) dla a<b i n>=1 oblicza przybliżenie dla f(x)=2*x**2+x-6. Podziel [a,b] na n równych części o szerokości h=(b-a)/n. Dodaj n pól h*f(a+i*h), i=0..n-1. To suma wartości ze znakiem: ujemne pola pozostają ujemne. Nie potrzeba znajomości całek. Wczytaj a b n, wypisz wynik z 4 miejscami. Indeksuj części liczbą całkowitą, żeby uniknąć dryfowania pętli po float.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
0 2 2: pola -6 oraz -3, wynik -9.0000.

SPRAWDŹ TAKŻE
n=1; przedział przecinający miejsce zerowe; porównaj n=10 i n=1000.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
