"""
DZIEŃ 1 — ZADANIE 04: Tabliczka i zagnieżdżone pętle
Tematyka: Tabliczka i zagnieżdżone pętle.
Źródło: Lab02/zad04.py–zad05.py; Lab03/zad07.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()): wczytuje n. range(start,stop): kolejne liczby bez stop.
- Wersja pierwsza: dwie zagnieżdżone pętle for. Wersja druga: dwie pętle while.
- print(wartość, end=' '): nie przechodzi do następnego wiersza; print() kończy wiersz.
- Operator * mnoży liczby.

Małe przykłady składni — nie są całym rozwiązaniem
    for k in range(2, 5):  # k przyjmuje 2, 3, 4
        print(k, end=' ')
    print()

Inny sposób / wariant bez własnych funkcji
Nie trzeba definiować funkcji ani budować całej tabeli w liście. Wersje for i while uruchamiaj osobno, żeby nie wypisać dwóch tabliczek w jednym wyniku.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (1..12). Wypisz n wierszy po n iloczynów: w wierszu i znajdują się i*1,...,i*n (i od 1). Oddzielaj liczby spacją. Zrób wersję for, a potem zastąp ją wersją while o identycznym wyjściu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
n=3: wiersze 1 2 3 / 2 4 6 / 3 6 9.

SPRAWDŹ TAKŻE
n=1 i n=12; brak dodatkowego pustego wiersza; rozróżniaj numer wiersza od indeksu.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
