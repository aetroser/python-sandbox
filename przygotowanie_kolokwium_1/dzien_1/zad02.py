"""
DZIEŃ 1 — ZADANIE 02: Przedział i pętla while
Tematyka: Przedział i pętla while.
Źródło: Lab02/zad03.py, zad06.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: interval(a, b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().split(): dzieli wiersz na fragmenty. int(): zamienia fragment na liczbę całkowitą.
- min(a,b), max(a,b): ustalają granice; można je zastąpić if i zamianą zmiennych.
- while: wymagany do zbudowania listy; [] tworzy listę, lista.append(x) dopisuje element.
- sum(lista) sumuje liczby, print(*lista) wypisuje elementy osobno, ze spacjami.

Małe przykłady składni — nie są całym rozwiązaniem
    a, b = map(int, input().split())  # map stosuje int do każdego fragmentu
    liczby = []
    liczby.append(12)
    print(*liczby)  # * rozpakowuje listę; tutaj wypisze 12

Inny sposób / wariant bez własnych funkcji
Bez sum() możesz prowadzić sumę w zmiennej i powiększać ją przez +=. Bez map() zapisz części=input().split(), a=int(części[0]), b=int(części[1]). W końcowej wersji zostaw interval i while — to wymagania tego ćwiczenia.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj całkowite a i b w jednej linii. Funkcja interval(a, b) zwraca listę wszystkich liczb od min(a,b) do max(a,b), łącznie z końcami. Zbuduj ją pętlą while. Wypisz liczby w jednej linii, a w drugiej ich sumę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 3 -1. Wyjście: -1 0 1 2 3, a w drugiej linii 5.

SPRAWDŹ TAKŻE
a=b; przedział zawierający zero; obie granice ujemne.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
