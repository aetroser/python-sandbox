"""
DZIEŃ 2 — ZADANIE 11: Malejące trójki z nakładaniem
Tematyka: Malejące trójki z nakładaniem.
Źródło: Lab05/03 Zadania (do przesłania)/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: triples(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- list(map(int,input().split())): dane, również pusta lista.
- len(data), indeksy i range(): przejście tylko po początkach pełnych okien długości 3.
- Porównanie łańcuchowe a>b>c jest skrótem dla a>b and b>c.
- data[i:i+3]: wycinek okna; wynik.append(okno): zbieranie znalezionych trójek.
- print(*trojka): trzy liczby w jednym wierszu.

Małe przykłady składni — nie są całym rozwiązaniem
    data = [10, 20, 30, 40]
    print(data[1:4])  # [20, 30, 40]
    print(9 > 6 > 2)  # True

Inny sposób / wariant bez własnych funkcji
Zamiast range użyj while z indeksem. Zamiast wycinka możesz zbudować listę z trzech odczytanych elementów. Okna można wypisywać wprost bez def, ale w końcowej wersji triples ma zwrócić zebrane wyniki.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Funkcja triples(data) znajduje każde okno trzech sąsiadujących elementów spełniających a>b>c. Okna mogą się nakładać. Wczytaj listę int z jednej linii, również pustą. Wypisz każdą trójkę w osobnej linii w kolejności początku, albo BRAK. Nie eliminuj identycznych trójek w różnych miejscach.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
5 4 3 2 1: 5 4 3 / 4 3 2 / 3 2 1.

SPRAWDŹ TAKŻE
Lista krótsza od 3; równe wartości przerywają ścisłe malenie; koniec listy.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
