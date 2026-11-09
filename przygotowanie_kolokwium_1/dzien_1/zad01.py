"""
D1.01: Wejście, typy i formatowanie | Lab02
Wczytaj dwie liczby rzeczywiste; wypisz sumę, różnicę i iloczyn z 2 miejscami oraz typ sumy.
Wymagana: add(a,b); same działania możesz najpierw zrobić bez def.
Wejście/próba: 2.5 / -1.5
Wynik: 1.00 / 4.00 / -3.75 / float
Przydatne: float(input()), type(x).__name__, print(f'{x:.2f}').
"""

# Tutaj napisz swoje rozwiązanie.
x = float(input("Podaj pierwszą liczbę rzeczywistą: "))
y = float(input("Podaj drugą liczbę rzeczywistą: "))

print(f"{x+y:.2f}")
print(f"{x-y:.2f}")
print(f"{x*y:.2f}")
print(type(x+y).__name__)