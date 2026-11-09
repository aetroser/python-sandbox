"""
KOLOKWIUM D — ZADANIE 4: Progi punktowe z Lab06
Tematyka: Progi punktowe z Lab06.
Źródło: Lab06/zad09.py (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- int(input()), map(int,input().split()), range(n): dane i rekordy.
- >, <= i if/elif/else: progi od najwyższego do najniższego.
- Procent: 100*punkty/maksimum; alternatywnie porównuj 100*punkty > prog*maksimum.
- Licznik +=1 dla wyniku co najmniej 3; print('ZALICZONE',licznik): podsumowanie.

Małe przykłady składni — nie są całym rozwiązaniem
    points, maximum, threshold = 7, 10, 60
    print(100 * points > threshold * maximum)  # True, bo 70% > 60%

Inny sposób / wariant bez własnych funkcji
Własna calculate_grade jest opcjonalna. Lista progów też nie jest wymagana — wystarczy if/elif. Porównanie iloczynów pozwala obejść obliczanie float i round(), bez zmiany ścisłości progów.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Ćwiczenie progów z laboratorium, odrębne od zasad oceny kolokwium. Wczytaj n (0..100), następnie n linii "punkty maksimum" z int 0<=punkty<=maksimum, 1<=maksimum<=1000. Dla każdego rekordu wypisz: 5 gdy wynik >80%, 4 gdy >60% i <=80%, 3 gdy >50% i <=60%, inaczej 2. Nie zaokrąglaj procentów przed porównaniem. Na końcu wypisz "ZALICZONE k", gdzie k jest liczbą rekordów z oceną co najmniej 3.

WEJŚCIE PRZYKŁADOWE
4
50 100
60 100
80 100
81 100

WYJŚCIE PRZYKŁADOWE
2
3
4
5
ZALICZONE 3

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
