"""
KOLOKWIUM D — ZADANIE 3: Aktualizacja książki telefonicznej
Tematyka: Aktualizacja książki telefonicznej.
Źródło: Lab05/01 Data structures/05 - dicts.py–07 - in_keyword.py (względem Labs/ w Labs.zip).
Sugerowany czas: 15 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), input().split(), range(): odczyt wpisów i zapytań.
- book={}, book[name]=number: dodanie albo zastąpienie numeru.
- book.get(name,'BRAK') albo if name in book: wyszukiwanie.
- len(book) liczy różne klucze; print('WPISY',len(book)): końcowy wiersz.
- Numer pozostaje str, aby zachować zera.

Małe przykłady składni — nie są całym rozwiązaniem
    book = {'Ewa': '0007'}
    book['Ewa'] = '0012'
    print(book['Ewa'])  # 0012
    print(len(book))  # 1

Inny sposób / wariant bez własnych funkcji
Możesz napisać całość bez def. Metodę get() można zastąpić warunkiem if/in. Nie trzeba sortować książki, bo wypisujesz odpowiedzi w kolejności zapytań, a nie wszystkie wpisy.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj n (0..100), potem n linii "imie numer". Imię to wyraz ASCII bez spacji; numer to niepusty tekst cyfr (zachowaj zera). Kolejny wpis o tym samym imieniu zastępuje poprzedni numer. Następnie wczytaj q (0..100) i q imion, każde osobno. Dla każdego zapytania wypisz aktualny numer lub BRAK. Na końcu wypisz "WPISY k", gdzie k to liczba różnych imion w książce. Wielkość liter ma znaczenie.

WEJŚCIE PRZYKŁADOWE
3
Ala 001
Ola 222
Ala 003
3
Ala
Ola
Jan

WYJŚCIE PRZYKŁADOWE
003
222
BRAK
WPISY 2

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
