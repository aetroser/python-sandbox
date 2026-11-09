"""
DZIEŃ 3 — ZADANIE 09: Wariancja i odchylenie standardowe
Tematyka: Wariancja i odchylenie standardowe.
Źródło: Lab06/zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(float,input().split())): odczyt liczb rzeczywistych.
- import statistics; statistics.variance(data), statistics.stdev(data): wartości dla próby.
- print(f'{x:.4f}'): cztery miejsca po kropce.
- abs(a-b) ocenia małą różnicę numeryczną; **2 podnosi odchylenie do kwadratu.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.variance([2, 4]))  # 2
    print(f'{0.5:.4f}')  # 0.5000

Inny sposób / wariant bez własnych funkcji
Nie musisz definiować własnych funkcji. Dodatkowo możesz policzyć wariancję ręcznie: suma kwadratów odchyleń od średniej podzielona przez n-1, a odchylenie jako jej pierwiastek. W głównym ćwiczeniu użyj jednak wymaganych variance i stdev, nie wersji populacyjnych.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj co najmniej 2 liczby rzeczywiste. Wypisz statistics.variance i statistics.stdev (dla próby), każde z 4 miejscami po kropce. Nie używaj pvariance ani pstdev. Sprawdź ręcznie, czy stdev**2 jest bliskie variance.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
1 2 3: 1.0000 / 1.0000.

SPRAWDŹ TAKŻE
Wszystkie równe; tylko 2 liczby; różnica między dzieleniem przez n i n-1.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
