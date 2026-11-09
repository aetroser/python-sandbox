"""
DZIEŃ 2 — ZADANIE 07: Normalizacja słów i częstotliwości
Tematyka: Normalizacja słów i częstotliwości.
Źródło: Lab03/zad06.py; Lab05/02 Strings/09 - string_methods.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- replace(znak,' '), lower(), split(): kolejno zastępowanie, małe litery, podział na słowa.
- {} tworzy słownik; counts.get(word,0) daje dotychczasową liczbę lub 0.
- len(words) liczy wszystkie słowa, len(counts) liczy różne klucze.
- max(counts.values()) wyznacza największą liczność; sorted() albo min() pomaga rozstrzygnąć remis.
- Przed max()/min() sprawdź, czy słownik nie jest pusty.

Małe przykłady składni — nie są całym rozwiązaniem
    print('X,Y!'.replace(',', ' '))  # X Y!
    counts = {}
    counts['rower'] = counts.get('rower', 0) + 1
    print(counts['rower'])  # 1

Inny sposób / wariant bez własnych funkcji
Słownik liczności możesz zbudować pętlą; collections.Counter nie jest konieczny. Zamiast get() użyj if word in counts. Nie musisz definiować funkcji. Jeśli nie znasz klucza sortowania, wybierz zwycięzcę przez prostą pętlę z porównaniem liczności i nazwy.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj wiersz. Zastąp każdy ze znaków ,.!?;: spacją, zamień litery na małe i zastosuj split(). Policz słowa, różne słowa i najczęstsze słowo. Przy remisie wybierz alfabetycznie najmniejsze. Wypisz 3 linie: liczba słów, liczba różnych, "słowo licznik"; dla pustego tekstu ostatnia linia BRAK.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kot, pies! KOT pies ala.: 5 / 3 / kot 2.

SPRAWDŹ TAKŻE
Sama interpunkcja; kilka spacji; remis; znak łącznika pozostaje częścią słowa.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
