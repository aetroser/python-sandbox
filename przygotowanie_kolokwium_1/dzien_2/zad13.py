"""
DZIEŃ 2 — ZADANIE 13: Sąsiadujące kwadraty bez duplikatów
Tematyka: Sąsiadujące kwadraty bez duplikatów.
Źródło: Lab06/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: square_pairs(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- len(data), range(), data[i], data[i+1]: sąsiednie elementy.
- a**2 oblicza kwadrat; (a,b) tworzy krotkę opisującą parę.
- seen=set(), pair in seen i seen.add(pair): wykrywanie duplikatów par.
- Osobna lista z append() zachowuje kolejność pierwszego znalezienia.
- print(*pair): dwa elementy w jednym wierszu.

Małe przykłady składni — nie są całym rozwiązaniem
    pair = (5, 25)
    seen = set()
    seen.add(pair)
    print(pair in seen)  # True

Inny sposób / wariant bez własnych funkcji
Nie musisz używać set(): można sprawdzać pair not in lista_wynikow, a potem append. Zbiór przyspiesza sprawdzanie, lista zachowuje kolejność. Końcowe rozwiązanie ma mieć square_pairs, choć samą pętlę można rozpisać bez def.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Zdefiniuj square_pairs(data): szukaj sąsiadów (a,b), dla których b=a**2. Każdą parę wypisz tylko raz, w kolejności pierwszego znalezienia. Wczytaj listę int z jednej linii. Wypisz pary w osobnych liniach albo BRAK. Para (-2,4) jest inna od (2,4); (0,0) jest poprawna.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2 4 2 4 -2 4: 2 4 / -2 4.

SPRAWDŹ TAKŻE
Pusta lista; para na końcu; duplikaty; (1,1); nie pomijaj nakładających się par.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
