"""
DZIEŃ 1 — ZADANIE 10: Równanie kwadratowe i przypadki szczególne
Tematyka: Równanie kwadratowe i przypadki szczególne.
Źródło: Lab03/zad08.py; Lab04/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: real_roots(a,b,c). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(), int(): współczynniki; **, *, -, /: obliczenia.
- W tym ćwiczeniu użyj import math i math.sqrt(delta), tylko dla delta>=0.
- if/elif/else: trzy przypadki; [], append(), sorted(): lista wyników rosnąco.
- len(wyniki): liczba wyników; print(f'{x:.2f}'): jeden wynik z 2 miejscami.

Małe przykłady składni — nie są całym rozwiązaniem
    import math
    print(math.sqrt(25))  # 5.0
    print(sorted([8, -2]))  # [-2, 8]
    print(f'{1.5:.2f}')  # 1.50

Inny sposób / wariant bez własnych funkcji
Przypadki można rozpisać wprost bez def, ale końcowo użyj real_roots. Zamiast sorted() wystarczy porównać dwa wyniki i w razie potrzeby je zamienić. Nie stosuj sqrt do ujemnej delty.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja real_roots(a,b,c) zwraca listę rzeczywistych rozwiązań rosnąco. Zakładamy a!=0; dla delty=0 zwróć jeden element, dla delty<0 pustą listę. Wczytaj całkowite a b c; wypisz liczbę pierwiastków, a następnie każdy z nich w osobnej linii z 2 miejscami. Zastosuj math.sqrt tylko dla nieujemnej delty.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
1 -3 2: linie 2 / 1.00 / 2.00. 1 0 1: tylko 0.

SPRAWDŹ TAKŻE
Delta dodatnia/zerowa/ujemna; a ujemne; uporządkowanie wyników.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
