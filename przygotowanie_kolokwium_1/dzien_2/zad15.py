"""
DZIEŃ 2 — ZADANIE 15: Usuwanie duplikatów i sortowanie z kluczem
Tematyka: Usuwanie duplikatów i sortowanie z kluczem.
Źródło: Lab06/zad12.py, zad19.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: sort_words(words) w części B; część A może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- set(data) albo pętla z in: usunięcie duplikatów.
- sorted(data,key=...) i lista.sort(key=...): sortowanie według klucza.
- Krotki są porównywane od pierwszego elementu, potem od drugiego; False poprzedza True.
- key=len oznacza długość słowa; key=nazwa_funkcji przekazuje funkcję, nie jej wynik.
- Funkcję klucza można zapisać przez def albo krótkie lambda.

Małe przykłady składni — nie są całym rozwiązaniem
    print(sorted(['xxxx', 'a', 'bb'], key=len))  # ['a', 'bb', 'xxxx']
    print(sorted([('b', 2), ('a', 3)]))  # [('a', 3), ('b', 2)]
    key_example = lambda x: x * x  # krótka funkcja: dla 3 zwraca 9

Inny sposób / wariant bez własnych funkcji
Nie musisz używać lambda — funkcję klucza możesz nazwać i zdefiniować przez def. W części A alternatywą są dwie osobne listy liczb posortowane i połączone; jednak aby przećwiczyć wymagany klucz krotkowy, końcowo zrób też wersję z key. Bez własnej funkcji klucza można użyć lambda, a dla słów bezpośrednio key=len.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Część A: wczytaj listę int, usuń duplikaty i wypisz najpierw nieparzyste rosnąco, potem parzyste rosnąco (PUSTA dla pustej). Użyj klucza będącego krotką (czy_parzysta,n). Część B: osobna funkcja sort_words(words) zwraca słowa według długości rosnąco, a dla równych długości zachowuje kolejność wejściową. Nie zmienia oryginału; porównaj z list.sort.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
7 2 3 2 -1 0: -1 3 7 0 2. ["kot","ala","a","do"] -> ["a","do","kot","ala"].

SPRAWDŹ TAKŻE
Ujemne liczby; stabilność sortowania; sorted zwraca listę, sort zmienia listę i zwraca None.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
