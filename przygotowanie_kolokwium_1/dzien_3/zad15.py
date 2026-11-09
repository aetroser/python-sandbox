"""
DZIEŃ 3 — ZADANIE 15: Zadanie przekrojowe: raport o liście
Tematyka: Zadanie przekrojowe: raport o liście.
Źródło: Lab03/zad05.py; Lab06/zad01.py, zad11.py, zad19.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 30 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: report(data); wykorzystaj także wcześniejsze funkcje pomocnicze. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- import lub from ... import ...: własne wcześniejsze funkcje; ich pliki muszą być dostępne w projekcie.
- is_prime, square_pairs i wcześniejszy klucz sortowania: części obliczeń.
- Słownik {'nazwa':wartosc}, indeksowanie po kluczu, return: zebranie trzech wyników.
- f'{a}:{b}': tekst pary; ' '.join(fragmenty): połączenie gotowych napisów.
- print(*liczby) wypisuje listę liczb; if not wynik obsługuje pustą kategorię.

Małe przykłady składni — nie są całym rozwiązaniem
    a, b = 4, 16
    piece = f'{a}:{b}'
    print(' '.join([piece, '5:25']))  # 4:16 5:25

Inny sposób / wariant bez własnych funkcji
Nie musisz używać list comprehension ani lambda: wystarczą pętle, append i nazwana funkcja klucza. Ten raport można policzyć wprost, ale końcowa wersja ma ćwiczyć report i ponowne użycie funkcji, a nie wklejenie kilku programów konsolowych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja report(data) zwraca słownik z kluczami: primes (wszystkie pierwsze z zachowaniem duplikatów i kolejności), pairs (unikalne sąsiednie pary (a,a**2), kolejność pierwszego wystąpienia), ordered (różne nieparzyste rosnąco, następnie różne parzyste rosnąco). Wczytaj listę int i wypisz 3 linie: primes rozdzielone spacją, pairs jako a:b rozdzielone spacją, ordered rozdzielone spacją. Każdą pustą kategorię oznacz BRAK. Wykorzystaj własne wcześniejsze funkcje zamiast kopiować całe programy z input().

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2 4 3 9 2 4 -> 2 3 2 / 2:4 3:9 / 3 9 2 4.

SPRAWDŹ TAKŻE
Puste dane; 0 0; liczby ujemne; uruchomienie modułów importowanych bez efektów ubocznych.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
