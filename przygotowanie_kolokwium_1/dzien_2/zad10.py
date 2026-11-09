"""
DZIEŃ 2 — ZADANIE 10: Adresy, duplikaty i sortowanie
Tematyka: Adresy, duplikaty i sortowanie.
Źródło: Lab05/03 Zadania (do przesłania)/zad01.py–zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: gmail_addresses(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- int(input()), input(), for z range(n): odczyt adresów.
- address.split('@')[1] pobiera domenę; porównuj przez ==, a nie wyszukiwanie podnapisu.
- set() i add() usuwają identyczne powtórzenia; sorted() daje listę w kolejności.
- if not wynik: brak adresów; for address in wynik: wypisanie po jednym.

Małe przykłady składni — nie są całym rozwiązaniem
    address = 'ewa@example.org'
    print(address.split('@')[1])  # example.org
    print(sorted({'b', 'a', 'b'}))  # ['a', 'b']

Inny sposób / wariant bez własnych funkcji
Bez set() zbieraj adresy do listy tylko wtedy, gdy jeszcze ich w niej nie ma. Możesz też sprawdzić końcówkę endswith('@gmail.com'). Obliczenia da się rozpisać wprost, lecz końcowa wersja wymaga gmail_addresses.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n, potem n poprawnych adresów e-mail małymi literami. Zachowaj wyłącznie te z domeną dokładnie gmail.com (tekst po @). Usuń duplikaty, posortuj rosnąco cały adres i wypisz każdy w osobnej linii; przy braku BRAK. Funkcja gmail_addresses(data) zwraca listę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Wejście: 4 / b@gmail.com / a@gmail.com / b@gmail.com / x@notgmail.com. Wynik: a@gmail.com / b@gmail.com.

SPRAWDŹ TAKŻE
n=0; gmail.com.pl nie jest gmail.com; identyczny adres kilka razy.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
