"""
DZIEŃ 1 — ZADANIE 14: Jednoczesne rzuty wieloma kośćmi
Tematyka: Jednoczesne rzuty wieloma kośćmi.
Źródło: Lab02/zad08.py; Lab04/zad05.py, zad10.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

POLECENIE
★ Funkcja dice_until(n,limit,seed) losuje w jednej rundzie n kości (1..6 każda), używając lokalnego Random(seed). Kończy po pierwszej rundzie samych jedynek lub samych szóstek, albo po limit rundach. Zwraca (liczba_rund, "JEDYNKI"/"SZOSTKI"/"LIMIT"). Parametry: 1<=n<=20, 0<=limit<=10000. Nie sumuj jedynek z różnych rund. Rozszerzenie: osobna funkcja sum_even_draws(target,limit,seed) dodaje tylko parzyste losowania randint(1,100) do chwili suma>=target albo limit; zwraca liczbę wszystkich losowań i sumę, target>0.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
limit=0: (0,"LIMIT"). Dla n=1 i limit=1000 zwykle szybko pojawi się 1 albo 6; porównaj dwa uruchomienia tego samego seed.

SPRAWDŹ TAKŻE
Zawsze istnieje limit; licznik rund różni się od liczby pojedynczych kości; w rozszerzeniu licz też nieparzyste losowania.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
