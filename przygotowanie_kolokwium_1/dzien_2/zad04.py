"""
DZIEŃ 2 — ZADANIE 04: Krotka i bezpieczny odczyt indeksu
Tematyka: Krotka i bezpieczny odczyt indeksu.
Źródło: Lab05/01 Data structures/04 - tuples.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- tuple('abcdefghijklmnopqrstuvwxyz'): krotka kolejnych liter; można też wpisać litery ręcznie.
- int(input()), porównania i if/else: sprawdzenie indeksu przed odczytem.
- len(), krotka[i], krotka[start:stop]: długość, element i wycinek.
- print(*wycinek): litery osobno, oddzielone spacjami.

Małe przykłady składni — nie są całym rozwiązaniem
    letters = tuple('abcd')
    print(letters[-1])  # d
    print(*letters[1:3])  # b c

Inny sposób / wariant bez własnych funkcji
Nie trzeba własnej funkcji ani importu. Zamiast tworzyć krotkę przez tuple() możesz użyć literału ('a','b',...), ale tutaj materiałem ćwiczenia ma być krotka, nie lista.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz tuple liter a..z. Wczytaj indeks i (int). Dla -26<=i<26 wypisz odpowiednią literę, w przeciwnym razie BLAD. Następnie wypisz długość krotki i litery indeksów 10..15 w jednej linii. Nie modyfikuj krotki.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
i=-1: z / 26 / k l m n o p.

SPRAWDŹ TAKŻE
-26 i 25 są poprawne; -27 i 26 nie są poprawne; indeksowanie od zera.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
