"""
DZIEŃ 2 — ZADANIE 12: Malejące trójki bez nakładania
Tematyka: Malejące trójki bez nakładania.
Źródło: Lab05/03 Zadania (do przesłania)/zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: triples(data) jako wersję bez nakładania, zgodnie z zadaniem 11. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- while i zmienny indeks początku: wygodne, gdy przesunięcie zależy od trafienia.
- len(data), indeksy, porównanie a>b>c i data[i:i+3]: ocena pełnego okna.
- i += 1 lub i += 3: różne przesunięcia, zgodnie z poleceniem.
- append() zbiera trójki; print(*trojka) wypisuje ich elementy.

Małe przykłady składni — nie są całym rozwiązaniem
    index = 4
    index += 3
    print(index)  # 7; += zmienia aktualną wartość zmiennej

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz modułów ani dodatkowej funkcji do sprawdzania okna. Pętlę możesz przetestować bez def, ale końcowo zastosuj funkcję analogiczną do zadania 11. Samo for i in range(...) nie reaguje na zmianę i wewnątrz pętli — do sterowanego przesunięcia wybierz while.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Jak zadanie 11, ale po znalezieniu trójki zużyj te trzy elementy; dalsze szukanie zaczyna się za nią. Gdy okno nie pasuje, przesuń początek tylko o jeden. Wynik ma zależeć od skanowania od lewej, bez szukania globalnie najlepszego podziału.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
5 4 3 2 1: tylko 5 4 3. Dla 1 9 8 7 6 5 4: 9 8 7 / 6 5 4.

SPRAWDŹ TAKŻE
Różnica między przesunięciem o 1 i o 3; dwa sąsiednie rozłączne okna.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
