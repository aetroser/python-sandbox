"""
KOLOKWIUM D — ZADANIE 2: Trójki bez powtórnego użycia elementów
Tematyka: Trójki bez powtórnego użycia elementów.
Źródło: Lab05/03 Zadania (do przesłania)/zad04.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())), len(), indeksowanie: odczyt i pełne okna.
- while z indeksem: przesunięcie zależne od wyniku.
- a>b>c, if/else, +=1 lub +=3: warunek i przesunięcia.
- print(*data[i:i+3]): wypisanie okna bez nawiasów; flaga trafienia: BRAK.

Małe przykłady składni — nie są całym rozwiązaniem
    i = 2
    i += 3
    print(i)  # 5
    print(*[9, 6, 3])  # 9 6 3

Inny sposób / wariant bez własnych funkcji
Nie potrzebujesz własnych funkcji ani listy wyników, jeśli wypisujesz trójki podczas przeglądania. Bez wycinka wypisz trzy elementy osobno. Do zmiennego przesunięcia użyj while, a nie zmieniania i wewnątrz for z range().

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną linię 0..100 int (-100..100). Skanuj od lewej okna trzech sąsiadów. Jeśli a>b>c, wypisz trójkę i przesuń początek za te trzy elementy. Jeśli warunek nie jest spełniony, przesuń początek o jeden. Każdą znalezioną trójkę wypisz w osobnej linii; przy braku BRAK. Nie wolno ponownie użyć pozycji należącej do już wybranej trójki.

WEJŚCIE PRZYKŁADOWE
1 9 8 7 6 5 4

WYJŚCIE PRZYKŁADOWE
9 8 7
6 5 4

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
