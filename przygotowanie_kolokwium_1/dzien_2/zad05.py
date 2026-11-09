"""
DZIEŃ 2 — ZADANIE 05: Kategorie znaków i formatowanie
Tematyka: Kategorie znaków i formatowanie.
Źródło: Lab05/02 Strings/01–10; Lab06/zad20.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: char_stats(text). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input(): zachowuje wiersz i jego spacje. for char in text: przegląd znaków.
- char == ' ': dosłowna spacja; char.isupper(), char.islower(): litery duże/małe.
- if/elif/else i liczniki += 1: rozłączne kategorie.
- return a,b,c,d zwraca krotkę; print(*wynik) wypisuje jej elementy.
- text.upper(): cały napis wielkimi literami.

Małe przykłady składni — nie są całym rozwiązaniem
    print('Ą'.isupper())  # True
    print('7'.islower())  # False
    print('rower'.upper())  # ROWER

Inny sposób / wariant bez własnych funkcji
Możesz policzyć kategorie bez def, ale końcowa wersja wymaga char_stats. Nie zastępuj testu char==' ' metodą isspace(), bo ta uznaje też tabulatory za białe znaki, a zadanie zalicza je do pozostałych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj cały wiersz tekstu (może być pusty). Funkcja char_stats(text) zwraca (spacje,duze,male,pozostale). Spacja to dokładnie znak " "; litery klasyfikuj isupper i islower; pozostałe obejmują cyfry i interpunkcję. Wypisz 4 liczby w jednej linii, a w drugiej text.upper(). Kategorie mają być rozłączne i sumować się do len(text).

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Tekst Ala 2!: 1 1 2 2 / ALA 2!.

SPRAWDŹ TAKŻE
Pusty tekst; polskie litery; cyfry; tabulator należy do pozostałych.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
