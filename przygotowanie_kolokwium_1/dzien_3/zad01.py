"""
DZIEŃ 3 — ZADANIE 01: Formatowanie daty i czasu
Tematyka: Formatowanie daty i czasu.
Źródło: Lab05/03 Zadania (do przesłania)/zad06.py; Lab06/zad05.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: now_text(); przetwarzanie podanej daty może być bez def. Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- from datetime import datetime: import klasy, nie całego modułu.
- map(int,input().split()) i rozpakowanie do 6 zmiennych: odczyt pól.
- datetime(rok,miesiac,dzien,godzina,minuta,sekunda): tworzy obiekt.
- f'{dt:%Y-%m-%d %H:%M:%S}': format daty i czasu z zerami.
- datetime.now(): aktualna data i czas tylko w dodatkowej funkcji now_text.

Małe przykłady składni — nie są całym rozwiązaniem
    from datetime import datetime
    dt = datetime(2020, 8, 9, 6, 7, 8)
    print(f'{dt:%Y-%m-%d %H:%M:%S}')  # 2020-08-09 06:07:08

Inny sposób / wariant bez własnych funkcji
Zamiast f-stringa można użyć dt.strftime('%Y-%m-%d %H:%M:%S'). Kody %Y/%m/%d to rok/miesiąc/dzień, %H/%M/%S to godzina/minuta/sekunda — %m i %M znaczą co innego. Nie musisz tworzyć dodatkowej funkcji do wczytanej daty; now_text pozostaje wymagana.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj 6 int w jednej linii: rok miesiąc dzień godzina minuta sekunda. Data i czas są poprawne. Utwórz datetime i wypisz RRRR-MM-DD GG:MM:SS z zerami wiodącymi. W osobnej funkcji now_text() zwróć aktualny lokalny czas w tym samym formacie; tej funkcji nie używaj do powtarzalnego przykładu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
2024 2 3 4 5 6 -> 2024-02-03 04:05:06.

SPRAWDŹ TAKŻE
Północ; koniec roku; różnica między date i datetime.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
