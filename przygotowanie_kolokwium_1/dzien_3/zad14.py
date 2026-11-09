"""
DZIEŃ 3 — ZADANIE 14: Analiza gry z podanych rzutów
Tematyka: Analiza gry z podanych rzutów.
Źródło: Lab03/zad09.py; Lab04/zad06.py, zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), map(int,input().split()): liczba partii i wyniki graczy.
- if/elif/else, and, >, ==: reguły rozstrzygania; sprawdź wspólne przekroczenie przed wyborem zwycięzcy.
- Liczniki += 1 albo słownik liczników: podsumowanie czterech etykiet.
- Osobna gra: import random, random.randint(1,100), while, break, licznik prób.

Małe przykłady składni — nie są całym rozwiązaniem
    counts = {'A': 0, 'B': 0}
    counts['A'] += 1
    print(counts['A'], counts['B'])  # 1 0

Inny sposób / wariant bez własnych funkcji
Możesz użyć czterech zwykłych liczników bez słownika, a obie części napisać bez def. Funkcja do oceny partii jest opcjonalna. Grę w zgadywanie uruchamiaj osobno od analizy zapisanych partii.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Dane są już rozegrane: wczytaj n, potem n linii "wynik_A wynik_B" (0..36). Wynik >21 przegrywa; jeśli obaj przekroczyli 21, wynik partii OBAJ; gdy tylko jeden przekroczył, wygrywa drugi; inaczej większy wygrywa, równe to REMIS. Wypisz wynik każdej partii (A/B/OBAJ/REMIS), a na końcu cztery liczniki w tej kolejności. Następnie osobno napisz grę w zgadywanie z losowaniem 1..100 i licznikiem prób; nie łącz wyjść obu programów.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
3 / 22 20 / 21 21 / 25 30 -> B / REMIS / OBAJ / 0 1 1 1.

SPRAWDŹ TAKŻE
n=0; dwa przekroczenia nie oznaczają remisu; dokładnie 21 jest poprawne.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
