"""
KOLOKWIUM B — ZADANIE 4: Średnia, mediana i moda z remisem
Tematyka: Średnia, mediana i moda z remisem.
Źródło: Lab06/zad03.py (względem Labs/ w Labs.zip).
Sugerowany czas: 20 min. Limit całego arkusza: 75 min + 5 min na ZIP i wgranie.
Środowisko: Python 3.10+, wyłącznie biblioteka standardowa.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- list(map(int,input().split())): liczby, import statistics: moduł.
- statistics.mean(), statistics.median(), statistics.multimode(): obliczenia.
- min(lista_mod): najmniejsza moda przy remisie.
- print(f'{x:.2f}'): średnia i mediana z 2 cyframi; modę wypisz bez .2f.
- round(x,2)==0 i x=0.0: zamiana zaokrąglonego ujemnego zera.

Małe przykłady składni — nie są całym rozwiązaniem
    import statistics
    print(statistics.multimode([6, 2, 6, 2]))  # [6, 2]
    print(min([6, 2]))  # 2
    print(f'{3.5:.2f}')  # 3.50

Inny sposób / wariant bez własnych funkcji
Możesz pisać bez def. Bez statistics policz średnią sum()/len(), medianę ze środkowych pozycji sorted(), a modę za pomocą słownika liczności. Nie musisz tworzyć własnych funkcji dla każdego z trzech obliczeń.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Wczytaj jedną niepustą linię 1..100 int (-1000..1000). Wypisz w 3 liniach średnią z 2 miejscami po kropce, medianę z 2 miejscami i modę jako int. Przy kilku modach wybierz najmniejszą wartość. Wolno używać modułu statistics. Jeśli zaokrąglony wynik jest zerem, wypisz 0.00.

WEJŚCIE PRZYKŁADOWE
4 1 4 1

WYJŚCIE PRZYKŁADOWE
2.50
2.50
1

WAŻNE
Dane spełniają opisane ograniczenia; nie dodawaj innej walidacji.
Czytaj bez tekstu zachęty (input(), nie input("Podaj...")).
Wypisuj tylko wymagane wyniki; liczby rzeczywiste z kropką.
Każdy plik jest niezależny. Funkcje możesz definiować według własnego uznania.
Zadanie jest zaliczone w testerze dopiero po przejściu wszystkich jego testów.
Nie ma częściowych zadań w ocenie końcowej.
"""

# Tutaj napisz swoje rozwiązanie.
