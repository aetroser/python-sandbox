"""
D1.06: Liczby pierwsze | Lab03
Wypisz rosnąco liczby pierwsze między a i b (włącznie), przy braku BRAK; n<2 nie jest pierwsze.
Wymagana: is_prime(n) → bool; sprawdzaj dzielniki własną pętlą.
Wejście/próba: -2 11
Wynik: 2 3 5 7 11
Przydatne: %, for/while, return True/False, append(), print(*wyniki); biblioteki zbędne.
"""

# Tutaj napisz swoje rozwiązanie.

def interval(a, b):
    numbers = []
    if a > b:
        a, b = b, a
    while a <= b:
        numbers.append(a)
        a += 1
    return numbers

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x, y = map(int, input().split())

for i in interval(x, y):
    if is_prime(i):
        print(i, end=" ")
