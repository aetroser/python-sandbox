"""
D1.12: Wartość funkcji i pierwiastki zespolone | Lab04 ★
A: oblicz 3*x**2+7*x-19 (2 miejsca). B: zwróć dwa pierwiastki zespolone równania, a≠0.
Wymagane: value(x), complex_roots(a,b,c); część B testuj osobno.
Wejście/próba: A: 2; B: complex_roots(1,0,1)
Wynik: A: 7.00; B: [1j,-1j] (kolejność dowolna)
Przydatne: **2, import cmath, cmath.sqrt(), print(f'{x:.2f}'); eval zbędne.
"""

# Tutaj napisz swoje rozwiązanie.

def value(x):
    return 3*x**2+7*x-19

def complex_roots(a,b,c):
    delta = b * b - 4 * a * c
    if delta < 0:
        real = -b / (2 * a)
        imag = (abs(delta)**0.5)/(2*a)
        return [2, [
            str(real) + " - " + str(imag) + "i",
            str(real) + " + " + str(imag) + "i"
        ]]
    if delta == 0:
        return [1, [str(-b / (2 * a)), str(0)]]
    else:
        return [2, [
               str((-b - (delta ** 0.5)) / (2 * a)),
               str((-b + (delta ** 0.5)) / (2 * a))
           ]]

m, n, o, p = map(int, input().split())

print(value(m))
print(complex_roots(n,o,p))