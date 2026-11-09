"""
D1.07: Silnia iteracyjna i rekurencyjna | Lab04
Dla n=0..20 oblicz silnię iteracyjnie i rekurencyjnie; wypisz oba wyniki. Pamiętaj 0!=1.
Wymagane: factorial_loop(n), factorial_recursive(n).
Wejście/próba: 5
Wynik: 120 / 120
Przydatne: for/while, *=, if, return; math.factorial(n) tylko do kontroli.
"""

# Tutaj napisz swoje rozwiązanie.

def factorial_loop(n):
    if n == 0:
        return 1

    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac

def factorial_recursive(n):
    if n == 0:
        return 1

    return n * factorial_recursive(n-1)

num = int(input())

if num < 0 or num > 20:
    exit("liczba n poza zakresem [0, 20]")

print(factorial_loop(num), factorial_recursive(num))

