"""
DZIEŃ 1 — ZADANIE 07: Silnia iteracyjna i rekurencyjna
Tematyka: Silnia iteracyjna i rekurencyjna.
Źródło: Lab04/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: factorial_loop(n) i factorial_recursive(n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- for z range() albo while i *=: wersja iteracyjna.
- if, return oraz wywołanie własnej funkcji: wersja rekurencyjna.
- import math, math.factorial(n): tylko do porównania wyników własnych wersji.
- int(input()), print(): wejście i wypisanie dwóch wyników.

Małe przykłady składni — nie są całym rozwiązaniem
    iloczyn = 1
    iloczyn *= 7  # to samo co iloczyn = iloczyn * 7
    import math
    print(math.factorial(3))  # 6; przykład kontroli, nie zamiennik obu wersji

Inny sposób / wariant bez własnych funkcji
Wersję z pętlą da się zapisać bez własnej funkcji. Rekurencja w tym ćwiczeniu polega na wywoływaniu factorial_recursive, więc wymaga def. Nie zastępuj obu wymaganych implementacji samym math.factorial().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj factorial_loop(n) i factorial_recursive(n) dla n od 0 do 20. Obie zwracają int. Wczytaj n i wypisz oba wyniki, każdy w osobnej linii. Porównaj ręcznie z math.factorial. Nie mierz czasu pojedynczego bardzo krótkiego wywołania.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
n=5: dwie linie po 120. Dla n=0 obie funkcje zwracają 1.

SPRAWDŹ TAKŻE
0, 1, 10, 20; warunek kończący rekurencję. Nie podawaj ujemnego n.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
