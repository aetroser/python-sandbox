"""
D1.03: break, continue i liczba kończąca | Lab02
Czytaj liczby do 0; ujemne pomijaj. Wypisz liczność i sumę dodatnich nieparzystych.
Własne funkcje zbędne; wymagane while True, break i continue.
Wejście/próba: -5 / 2 / 3 / 7 / 0
Wynik: 2 10
Przydatne: int(input()), if, n % 2, licznik += 1, suma += n.
"""

# Tutaj napisz swoje rozwiązanie.

liczba_nieparzystych = 0
suma_nieparzystych = 0

while True:
    liczba = int(input())

    if liczba == 0:
        break

    if liczba < 0:
        continue

    if liczba % 2:
        liczba_nieparzystych += 1
        suma_nieparzystych += liczba

print(liczba_nieparzystych, suma_nieparzystych)