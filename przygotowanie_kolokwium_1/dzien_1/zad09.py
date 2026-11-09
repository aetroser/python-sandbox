"""
DZIEŃ 1 — ZADANIE 09: Wzór i rozłączne przedziały
Tematyka: Wzór i rozłączne przedziały.
Źródło: Lab04/zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: bmi(height,mass) oraz band(height,mass). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- float(), input().split(): dwie liczby z jednego wiersza.
- ** to potęgowanie, / to dzielenie; if/elif/else sprawdza rozłączne przedziały.
- Wywołanie bmi(...) wewnątrz band(...): użycie wyniku innej funkcji.
- print(f'{wartosc:.2f}'): dwa miejsca; print(symbol): kolejny wiersz.

Małe przykłady składni — nie są całym rozwiązaniem
    print(4 ** 2)  # 16; w Pythonie potęga to **, a nie ^
    x = 24.999
    print(f'{x:.2f}')  # 25.00, choć x nadal jest mniejsze od 25

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz modułu math. Wariant bez def jest możliwy jako pierwsza próba, ale końcowa wersja ma zawierać obie funkcje. Nie używaj zaokrąglonego tekstu do wyboru przedziału.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Ćwiczenie obliczeniowe na wzorze BMI, bez interpretacji zdrowotnej. Funkcja bmi(height,mass) zwraca mass/height**2; wzrost w metrach, masa w kg. Funkcja band(height,mass) używa bmi i zwraca A dla wyniku <18.5, B dla [18.5,25), C dla [25,30), D dla >=30. Dane dodatnie. Wczytaj height mass; wypisz wartość z 2 miejscami i symbol w drugiej linii. Klasyfikuj przed zaokrągleniem.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście 2 100: 25.00 / C.

SPRAWDŹ TAKŻE
Wzrost 2 i masy 74, 100, 120 sprawdzają dokładne progi. Wynik 24.999 należy jeszcze do B.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
