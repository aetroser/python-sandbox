"""
DZIEŃ 2 — ZADANIE 01: Indeksy i slicing
Tematyka: Indeksy i slicing.
Źródło: Lab05/01 Data structures/01 - lists.py; Lab05/02 Strings/03–07 (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- input(): odczyt całego tekstu wraz ze spacjami; len(text): długość.
- text[index]: pojedynczy znak; text[start:stop:step]: wycinek, bez pozycji stop.
- Indeks -1 oznacza ostatni znak. // to dzielenie całkowite.
- Krok -1 odwraca kierunek; brak start i stop obejmuje cały napis.

Małe przykłady składni — nie są całym rozwiązaniem
    s = 'abcdefgh'
    print(s[1])     # b
    print(s[2:5])   # cde
    print(s[::3])   # adg
    print(s[::-1])  # hgfedcba

Inny sposób / wariant bez własnych funkcji
Nie są potrzebne moduły ani własne funkcje. Te same wybory znaków da się zbudować pętlą, ale tu przećwicz indeksowanie i wycinki. Nie stosuj strip(), jeśli chcesz zachować spacje wejściowe.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj niepusty napis długości co najmniej 4. Wypisz w osobnych liniach: pierwszy znak, ostatni, pierwszą połowę (len//2 znaków), co drugi znak od indeksu 0, napis odwrócony. Spacje są zwykłymi znakami.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Python: P / n / Pyt / Pto / nohtyP.

SPRAWDŹ TAKŻE
Długość parzysta i nieparzysta; ujemne indeksy; koniec wycinka nie należy do wyniku.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
