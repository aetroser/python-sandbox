"""
D1.02: Przedział i pętla while | Lab02
Wczytaj a b; wypisz liczby od mniejszej do większej (końce włącznie), potem ich sumę.
Wymagana: interval(a,b), zwracająca listę zbudowaną przez while.
Wejście/próba: 3 -1
Wynik: -1 0 1 2 3 / 5
Przydatne: int(), split(), while, append(), print(*lista), sum() lub suma += x.
"""

# Tutaj napisz swoje rozwiązanie.

def interval(a,b):
    nrs = []
    if a > b:
        a, b = b, a
    while a <= b:
        nrs.append(a)
        a += 1
    return nrs

x, y = map(int, input().split())
nrs = interval(x, y)

print(*nrs, end=" ")
print(f"/ {sum(nrs)}")