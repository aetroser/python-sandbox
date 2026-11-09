"""
DZIEŃ 1 — ZADANIE 11: Importy i samodzielne uruchamianie modułu
Tematyka: Importy i samodzielne uruchamianie modułu.
Źródło: Lab03/zad01.py–zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_even i sum_even w osobnym module narzedzia11.py. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import nazwa_modulu: potem wywołujesz nazwa_modulu.nazwa_funkcji(...).
- from nazwa_modulu import nazwa_funkcji: pozwala wywołać samą nazwę funkcji.
- if __name__ == '__main__': umieść pod nim wejście/wyjście wykonywane tylko przy uruchomieniu pliku.
- Nie dodawaj końcówki .py w instrukcji import; oba pliki mają być obok siebie.

Małe przykłady składni — nie są całym rozwiązaniem
    # Dwa niezależne przykłady składni importu:
    import math
    print(math.sqrt(16))
    from math import sqrt
    print(sqrt(16))

Inny sposób / wariant bez własnych funkcji
Ten sam rachunek da się wykonać w jednym pliku bez modułu, ale nie spełniłoby to celu tego zadania. Tu ćwiczysz właśnie własne funkcje, import i brak wypisywania danych przy imporcie.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz obok tego pliku narzedzia11.py z is_even i sum_even z zadania 5; na górze nowego pliku wpisz temat i źródło Lab03/zad01.py–zad02.py. Ten plik zad11.py ma importować narzedzia11, wczytać a b i wypisać sumę parzystych. Import narzedzia11 nie może nic wypisywać ani pytać o dane. Pokaż ręcznie różnicę między import narzedzia11 i from narzedzia11 import is_even.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście 1 6: 12. Polecenie python -c "import narzedzia11" uruchomione w tym folderze: brak wyjścia.

SPRAWDŹ TAKŻE
if __name__ == "__main__"; unikaj import *; funkcja nie powinna przesłaniać wbudowanego sum.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
