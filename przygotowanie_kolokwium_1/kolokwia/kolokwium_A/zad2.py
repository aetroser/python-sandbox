"""
Kol. A.2: Rozwiązania równania kwadratowego | Lab03
Dla int a b c (a≠0) wypisz liczbę różnych rzeczywistych pierwiastków, potem każdy rosnąco z 2 miejscami.
Własne funkcje opcjonalne; brak → tylko 0, zaokrąglone ujemne zero zapisuj 0.00.
Wejście/próba: 1 -3 2
Wynik: 2 / 1.00 / 2.00
Przydatne: math.sqrt() lub delta**0.5, if/elif, sorted() lub zamiana, print(f'{x:.2f}'), round(x,2).
"""

def roots(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        return [0, []]

    if delta == 0:
        return [1, [-b/2*a]]

    return [2, [(-b-delta**0.5)/2*a, (-b+delta**0.5)/2*a]]

# Tutaj napisz swoje rozwiązanie.
x, y, z = map(int, input().split())

if x == 0:
    exit("a nie moze byc rowne 0")

rts = roots(x, y, z)


print(rts[0], end=" ")

for i in range(rts[0]):
    print("/", rts[1][i], end=" ")
