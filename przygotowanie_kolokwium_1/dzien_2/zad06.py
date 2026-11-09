"""
DZIEŃ 2 — ZADANIE 06: Odwracanie bez wycinka
Tematyka: Odwracanie bez wycinka.
Źródło: Lab06/zad18.py; Lab05/02 Strings/05 - slicing.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 12 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: reverse_str(text) i palindrome(text). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- Pętla po znakach albo po indeksach; + skleja napisy.
- text.lower() ujednolica litery; text.replace(' ','') usuwa zwykłe spacje.
- == porównuje napisy; funkcja palindrome zwraca bool.
- if/else wybiera wypisanie TAK albo NIE. W reverse_str zakazane są [::-1] i reversed().

Małe przykłady składni — nie są całym rozwiązaniem
    print('A B'.lower())       # a b
    print('A B'.replace(' ', ''))  # AB
    piece = 'x'
    print(piece + 'yz')  # xyz

Inny sposób / wariant bez własnych funkcji
Bez reversed() i bez wycinka użyj własnej pętli i sklejania znaków. Zapis bez def jest możliwy do przećwiczenia, ale końcowo zostaw obie wymagane funkcje. Nie usuwaj innych znaków niż spacje.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj reverse_str(text) bez [::-1] i bez reversed(). Zwróć napis odwrócony. Funkcja palindrome(text) ignoruje spacje i wielkość liter, pozostałych znaków nie usuwa; zwraca bool. Wczytaj linię i wypisz odwrócony tekst, a potem TAK lub NIE zależnie od palindrome.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kajak: kajaK / TAK. Tekst a b a też jest palindromem.

SPRAWDŹ TAKŻE
Pusty tekst uznaj za palindrom; jeden znak; różna wielkość liter.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
