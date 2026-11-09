"""
DZIEŃ 1 — ZADANIE 05: Funkcje i sumy według parzystości
Tematyka: Funkcje i sumy według parzystości.
Źródło: Lab03/zad01.py–zad04.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: is_even(n), sum_even(a,b), sum_odd(a,b), selected_sum(even,a,b). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- def, parametry i return: definiowanie funkcji i przekazywanie wyniku.
- n % 2, porównanie == oraz bool: sprawdzanie parzystości.
- range(a,b+1) albo while: przejście przez przedział z końcem b.
- if/else wybiera odpowiednią funkcję; suma += n gromadzi wynik.

Małe przykłady składni — nie są całym rozwiązaniem
    def double(value):
        return value * 2
    result = double(4)  # przykład wywołania: result ma wartość 8

Inny sposób / wariant bez własnych funkcji
Pętle sumujące można najpierw przećwiczyć bez def, ale ostatecznie muszą znaleźć się we wskazanych funkcjach. sum() jest możliwym skrótem do sumowania gotowej kolekcji; tutaj łatwiej zacząć od zmiennej sumującej. Nie twórz własnej funkcji o nazwie sum.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj is_even(n), sum_even(a,b), sum_odd(a,b) i selected_sum(even,a,b). Granice włącznie; dla a>b zamień je. selected_sum(True,...) wybiera parzyste, False nieparzyste. Nie nazywaj funkcji sum. W programie wczytaj a b i wypisz obie sumy w jednej linii.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
a=-3, b=3: 0 0. selected_sum(True,1,6) zwraca 12.

SPRAWDŹ TAKŻE
Przedział jednoelementowy; zero jest parzyste; is_even zwraca bool, pozostałe funkcje int.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
