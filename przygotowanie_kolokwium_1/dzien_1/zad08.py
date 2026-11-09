"""
DZIEŃ 1 — ZADANIE 08: Konwersje i wybór operacji
Tematyka: Konwersje i wybór operacji.
Źródło: Lab02/zadania do realizacji.py; Lab04/zad02.py–zad03.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: km_to_miles(distance), miles_to_km(distance), c_to_f(value), f_to_c(value). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- input().upper(): wybór operacji niezależnie od wielkości liter.
- while, if/elif/else, break: ponawianie wyboru i wybranie przeliczenia.
- in sprawdza przynależność, np. do krotki dozwolonych napisów.
- float(input()), operatory *, /, +, - oraz print(f'{wynik:.2f}').

Małe przykłady składni — nie są całym rozwiązaniem
    choice = input().upper()
    print('mi'.upper())  # MI
    value = 3.5
    print(f'{value:.2f}')  # 3.50

Inny sposób / wariant bez własnych funkcji
Przeliczenia to zwykłe działania i można je wykonać bez bibliotek oraz bez def. W końcowej wersji umieść je jednak w czterech wymaganych funkcjach. Zamiast upper() można porównywać osobno warianty małych i dużych liter.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj km_to_miles, miles_to_km, c_to_f, f_to_c. Przyjmij 1 mila = 1.60934 km; F=C*9/5+32. Wczytuj nazwę operacji KM, MI, C lub F aż będzie poprawna (ignoruj wielkość liter); przy złej wypisz BLAD. KM oznacza km na mile, MI mile na km, C stopnie C na F, F odwrotnie. Następnie wczytaj wartość i wypisz wynik z 2 miejscami.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Kolejne linie: x / c / 20. Wyjście: BLAD, a potem 68.00.

SPRAWDŹ TAKŻE
0 stopni C; -40; 1 mila; kilka błędnych wyborów; odległości są nieujemne.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
