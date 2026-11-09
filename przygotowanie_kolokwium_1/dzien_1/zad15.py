"""
DZIEŃ 1 — ZADANIE 15: Przybliżenie całki prostokątami
Tematyka: Przybliżenie całki prostokątami.
Źródło: Lab04/zad08.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: rectangle_sum(a,b,n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(), float(), int(): dwie granice oraz liczba części.
- range(n): dokładnie n indeksów od 0 do n-1; for albo while do sumowania.
- **, *, /, +, - oraz suma += pole: obliczanie i dodawanie pól.
- print(f'{wynik:.4f}'): dokładnie 4 miejsca po kropce, także końcowe zera.

Małe przykłady składni — nie są całym rozwiązaniem
    parts = input().split()
    a = float(parts[0])
    b = float(parts[1])
    n = int(parts[2])
    print(f'{2.5:.4f}')  # 2.5000

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz biblioteki do całkowania ani funkcji sum(). Wystarczy pętla ze zmienną sumującą. Osobna funkcja dla wielomianu jest opcjonalna; rectangle_sum pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

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
