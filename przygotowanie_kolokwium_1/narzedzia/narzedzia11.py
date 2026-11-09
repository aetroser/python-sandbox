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