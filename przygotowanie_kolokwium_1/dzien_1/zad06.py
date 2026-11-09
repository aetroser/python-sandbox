"""
DZIEŃ 1 — ZADANIE 06: Liczby pierwsze
Tematyka: Liczby pierwsze.
Źródło: Lab03/zad05.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_prime(n). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(), input().split(): granice; range() lub while: kolejne liczby i potencjalne dzielniki.
- n % d: reszta z dzielenia przez d; if rozdziela przypadki n<2 i pozostałe.
- return True / return False: wynik logiczny funkcji, bez print w jej środku.
- Lista wyników, append(), print(*wyniki); if not wyniki wykrywa pustą listę.

Małe przykłady składni — nie są całym rozwiązaniem
    print(17 % 5)  # 2 — reszta z dzielenia
    print(15 % 5)  # 0 — 5 jest dzielnikiem 15

Inny sposób / wariant bez własnych funkcji
Nie ma potrzebnej tu wbudowanej funkcji is_prime. Napisz własne sprawdzanie dzielników. Biblioteki nie są konieczne; samą pętlę można sprawdzić bez def, ale końcowa wersja wymaga is_prime.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj is_prime(n) -> bool. Wczytaj całkowite a b. Wypisz rosnąco liczby pierwsze z domkniętego przedziału między nimi, albo BRAK. Nie korzystaj z zewnętrznych bibliotek. Liczby mniejsze od 2 nie są pierwsze.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: -2 11. Wynik: 2 3 5 7 11.

SPRAWDŹ TAKŻE
0, 1, 2, 4, 49, 97; odwrócone granice; przedział bez liczb pierwszych.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
