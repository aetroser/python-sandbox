"""
D1.10: Równanie kwadratowe i przypadki szczególne | Lab03, Lab04
Dla a b c (a≠0) wypisz liczbę różnych pierwiastków rzeczywistych, potem każdy rosnąco z 2 miejscami.
Wymagana: real_roots(a,b,c) → lista (pusta, gdy brak pierwiastków).
Wejście/próba: 1 -3 2
Wynik: 2 / 1.00 / 2.00
Przydatne: import math, math.sqrt(delta), if/elif, sorted(), len(), print(f'{x:.2f}').
"""

# Tutaj napisz swoje rozwiązanie.

def real_roots(a,b,c):
    delta = b*b - 4 * a * c
    if delta < 0:
        return [0, [0, 0]]
    if delta == 0:
        return [1, [-b/(2*a), 0]]
    else:
        return [2, [
            (-b - (delta**0.5))/(2*a),
            (-b + (delta ** 0.5)) / (2 * a)
        ]]

x, y, z = map(float, input().split())
result = real_roots(x,y,z)

print(result[0], result[1][0], result[1][1])