"""
DZIEŃ 3 — ZADANIE 07: calendar i struktura miesiąca
Tematyka: calendar i struktura miesiąca.
Źródło: Lab05/03 Zadania (do przesłania)/zad05.py; Lab06/zad17.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- import calendar; calendar.setfirstweekday(calendar.MONDAY): poniedziałek jako pierwsza kolumna.
- calendar.monthcalendar(year,month): lista tygodni, każdy z 7 liczb dni (0 oznacza poza miesiącem).
- Dwie pętle albo indeks kolumny 0: liczenie dni i poniedziałków.
- calendar.month(year,month) i calendar.calendar(year): tekstowe kalendarze do osobnej obserwacji.

Małe przykłady składni — nie są całym rozwiązaniem
    import calendar
    calendar.setfirstweekday(calendar.MONDAY)
    weeks = calendar.monthcalendar(2020, 8)
    print(weeks[0])  # [0, 0, 0, 0, 0, 1, 2]

Inny sposób / wariant bez własnych funkcji
Nie musisz pisać własnych funkcji. Dni można też otrzymać przez calendar.monthrange(year,month)[1], ale to dodatek: w tym zadaniu przećwicz wymaganą macierz monthcalendar. Kalendarze tekstowe oglądaj oddzielnie, żeby nie zmienić wymaganego wyjścia liczbowego.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj rok miesiąc. Użyj calendar.monthcalendar: zera są dniami spoza miesiąca. Wypisz liczbę dni miesiąca i liczbę poniedziałków w nim (w jednej linii). Następnie ręcznie obejrzyj calendar.month i calendar.calendar dla tego roku. Ustaw pierwszy dzień tygodnia na poniedziałek.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024 2 -> 29 4.

SPRAWDŹ TAKŻE
Luty przestępny; miesiąc mający 5 poniedziałków; nie licz zer jako dni.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
