"""
KOLOKWIUM B — ZADANIE 2: Posortowane unikalne adresy
Tematyka: Posortowane unikalne adresy.
Źródło: Lab05/03 Zadania (do przesłania)/zad01.py–zad02.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), range(n), input(): odczyt n adresów.
- address.split('@')[1] i ==: dokładna domena.
- set(), add(), sorted(): różne adresy we wskazanej kolejności.
- len(wyniki) i pętla print(address): liczba oraz kolejne wiersze.

Małe przykłady składni — nie są całym rozwiązaniem
    address = 'name@example.net'
    print(address.split('@')[1])  # example.net
    items = set()
    items.add('x')
    items.add('x')
    print(len(items))  # 1

Inny sposób / wariant bez własnych funkcji
Bez własnych funkcji można wykonać całość wprost. Bez set() sprawdzaj, czy adres jest już na liście, i dopisuj tylko nowe. Sam test 'gmail.com' in address nie sprawdza dokładnej domeny.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n poprawnych adresów e-mail, każdy w osobnej linii. Adresy składają się z małych liter ASCII, cyfr i znaków . _ @; każdy ma dokładnie jedno @. Wybierz tylko domenę dokładnie gmail.com, usuń identyczne adresy i posortuj rosnąco całe adresy. W pierwszej linii wypisz ich liczbę, następnie każdy adres osobno. Dla pustego wyniku wypisz tylko 0.

WEJŚCIE PRZYKŁADOWE
4
b@gmail.com
a@gmail.com
b@gmail.com
x@notgmail.com

WYJŚCIE PRZYKŁADOWE
2
a@gmail.com
b@gmail.com

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
