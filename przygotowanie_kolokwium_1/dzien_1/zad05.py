"""
D1.05: Funkcje i sumy według parzystości | Lab03
Dla a b sumuj osobno parzyste i nieparzyste; końce włącznie, kolejność granic dowolna.
Wymagane: is_even(n), sum_even(a,b), sum_odd(a,b), selected_sum(even,a,b).
Wejście/próba: 1 6
Wynik: 12 9
Przydatne: %, return, range(), if; selected_sum(True,...) wybiera parzyste, False nieparzyste.
"""

# Tutaj napisz swoje rozwiązanie.

def interval(a: int, b: int):
    numbers = []
    if a > b:
        a, b = b, a
    while a <= b:
        numbers.append(a)
        a += 1
    return numbers

def is_even(n):
    return n % 2 == 0

def sum_even(a, b):
    if a == b and is_even(a):
        return a
    elif a == b:
        return 0

    suma = 0
    for i in interval(a, b):
        if is_even(i):
            suma += i
    return suma

def sum_odd(a, b):
    if a == b and not is_even(a):
        return a
    elif a == b:
        return 0

    suma = 0
    for i in interval(a, b):
        if not is_even(i):
            suma += i
    return suma

def selected_sum(which_sum, a, b):
    if which_sum == 1:
        return sum_even(a, b)
    elif which_sum == 0:
        return sum_odd(a, b)
    else:
        exit("a number must be either even or odd")

x, y = map(int, input().split())
even = 1
odd = 0
even_sum = selected_sum(even, x, y)
odd_sum = selected_sum(odd, x, y)
print(even_sum, odd_sum, f"\ndiff: {even_sum - odd_sum}")
