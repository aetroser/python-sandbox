"""
DZIEŃ 1 — ZADANIE 01: Wejście, typy i formatowanie
Tematyka: Wejście, typy i formatowanie.
Źródło: Lab02/zad01.py–zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 8 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: add(a, b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input(): wczytuje jeden wiersz jako str; float(): zamienia tekst na liczbę rzeczywistą.
- print(): wypisuje wynik. Operatory +, - i * wykonują działania.
- F-string f'{x:.2f}' oznacza zapis z dokładnie 2 cyframi po kropce.
- type(x).__name__ daje samą nazwę typu, np. float; type(x) daje zapis <class 'float'>.

Małe przykłady składni — nie są całym rozwiązaniem
    x = float(input())
    print(f'{x:.2f}')        # gdy x=8.5, wypisze 8.50
    print(type(x).__name__)  # wypisze float

Inny sposób / wariant bez własnych funkcji
Najpierw możesz policzyć działania bez własnej funkcji, potem przenieść dodawanie do add(a,b). Do formatowania możesz zamiast f-stringa użyć print(format(x, '.2f')) lub print('{:.2f}'.format(x)). Samo round(x,2) nie zapewnia dwóch wypisanych cyfr: np. round(8.5,2) nadal jest liczbą 8.5.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj dwie liczby rzeczywiste, każdą w osobnej linii. Wypisz sumę, różnicę a-b i iloczyn, każdy w osobnej linii z dwoma miejscami po kropce. Na końcu wypisz nazwę typu sumy (float). Następnie zdefiniuj funkcję add(a, b) zwracającą sumę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 2.5 oraz -1.5. Wyjście w 4 liniach: 1.00 / 4.00 / -3.75 / float.

SPRAWDŹ TAKŻE
Zero, dwie liczby ujemne, ułamek. Wyjaśnij sobie, dlaczego samo input() nie dodaje liczb.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
