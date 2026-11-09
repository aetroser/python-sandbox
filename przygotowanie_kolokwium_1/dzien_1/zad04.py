"""
D1.04: Tabliczka i zagnieżdżone pętle | Lab02, Lab03
Wczytaj n (1–12); wypisz tabliczkę n×n. Zrób osobno wersję for i while.
Własne funkcje zbędne.
Wejście/próba: 3
Wynik: 1 2 3 / 2 4 6 / 3 6 9
Przydatne: range(1,n+1), zagnieżdżone pętle, print(x,end=' '), print().
"""

# Tutaj napisz swoje rozwiązanie.

n = int(input())

if n < 1 or n > 12:
    exit("liczba n nie jest z przedziału [1, 12]\n")

print("Wersja for:")
for i in range(0, n*n):
    print("0", end=" ")
    if ((i + 1) % n) == 0:
        print()

print("Wersja while:")
i = 0
while i < n*n:
    print("0", end=" ")
    if ((i + 1) % n) == 0:
        print()
    i += 1