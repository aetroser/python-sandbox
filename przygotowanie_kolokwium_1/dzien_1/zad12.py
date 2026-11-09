"""
DZIEŃ 1 — ZADANIE 12: Wartość funkcji i pierwiastki zespolone
Tematyka: Wartość funkcji i pierwiastki zespolone.
Źródło: Lab04/zad01.py, zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: value(x) i complex_roots(a,b,c). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- **, *, +, -, /: zwykłe działania; float(input()): argument części A.
- Część B: import cmath i cmath.sqrt(...), który dopuszcza ujemny argument.
- Zwróć dwa elementy np. jako listę; liczba zespolona może zawierać jednostkę 1j.
- W części A użyj print(f'{wynik:.2f}'); części B nie dopisuj do tego samego wyjścia.

Małe przykłady składni — nie są całym rozwiązaniem
    import cmath
    print(cmath.sqrt(-9))  # 3j
    print(1j * 1j)  # (-1+0j)

Inny sposób / wariant bez własnych funkcji
Część A to działania możliwe bez bibliotek. Sam rachunek obu części można zapisać bez def, lecz ćwiczenie wymaga wskazanych funkcji i cmath.sqrt w części B. eval() nie jest potrzebne.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Część A: value(x) oblicza 3*x**2+7*x-19; wczytaj x i wypisz wynik z 2 miejscami. Część B: complex_roots(a,b,c), a!=0, zwraca dwa pierwiastki, także gdy są równe; użyj cmath.sqrt. Przykłady części B uruchamiaj ręcznie osobno. Nie potrzebujesz eval.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
value(2)=7. complex_roots(1,0,1) daje pierwiastki 1j i -1j (kolejność dowolna).

SPRAWDŹ TAKŻE
Pierwiastek zespolony podniesiony do kwadratu ma dać -1; delta=0; ujemne x.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
