"""
DZIEŃ 3 — ZADANIE 12: Pomiar czasu bez z góry ustalonego zwycięzcy
Tematyka: Pomiar czasu bez z góry ustalonego zwycięzcy.
Źródło: Lab06/zad04.py; Lab04/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(range(...)) i tuple(range(...)): dane do porównania; += w pętli sumującej.
- import time; time.perf_counter(): punkt czasu, odjęcie dwóch odczytów daje sekundy.
- random.randint(a,b): liczby do osobnej próby generowania.
- lista.sort() lub sorted(lista): sortowanie; zapamiętaj, co dokładnie mierzysz.
- statistics.median(czasy): porównanie 5 powtórzeń; f'{czas:.6f}': 6 cyfr po kropce.

Małe przykłady składni — nie są całym rozwiązaniem
    import time
    start = time.perf_counter()
    # W tym miejscu wykonuje się mierzona operacja.
    elapsed = time.perf_counter() - start
    print(f'{elapsed:.6f}')

Inny sposób / wariant bez własnych funkcji
Własne funkcje są opcjonalne, można powtórzyć operacje w pętli for. W tym ćwiczeniu sumuj listę i krotkę ręcznie, a nie przez sum(). Do mediany 5 pomiarów można też posortować czasy i wziąć środkowy element.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Utwórz listę i krotkę liczb 1..100000. Osobno zmierz pętle ręcznego sumowania przez time.perf_counter(); utworzenie danych ma być przed startem pomiaru. Następnie zmierz generowanie 100000 liczb randint(1,100000) i sortowanie tej listy oddzielnie. Wypisz sumy oraz 4 czasy z 6 miejscami. Powtórz 5 razy i porównaj mediany czasów; nie zakładaj, że krotka zawsze będzie szybsza.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Obie sumy muszą wynosić 5000050000. Czasy są zależne od komputera i nie mają jednego oczekiwanego wyniku.

SPRAWDŹ TAKŻE
Start i stop każdej operacji; sortowanie kolejnej próby ma otrzymać nieposortowane dane.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
