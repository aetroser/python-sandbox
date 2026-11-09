"""
D1.08: Konwersje i wybór operacji | Lab02, Lab04
Ponawiaj wybór KM/MI/C/F (bez rozróżniania liter; zły → BLAD); przelicz wartość, wypisz 2 miejsca.
Wymagane: km_to_miles, miles_to_km, c_to_f, f_to_c; 1 mi=1.60934 km, F=C*9/5+32.
Wejście/próba: x / c / 20
Wynik: BLAD / 68.00
Przydatne: upper(), while, if/elif, float(input()), print(f'{x:.2f}').
"""

# Tutaj napisz swoje rozwiązanie.

def km_to_miles(km):
    return km * 0.621371192

def miles_to_km(miles):
    return miles * 1.60934

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def f_to_c(f):
    return (f - 32) * 5.0 / 9.0

while True:
    x = str(input())

    if x in ["KM", "MI", "C", "F", "km", "mi", "c", "f"]:
        break

try:
    y = float(input())
except ValueError:
    print("BLAD")
else:
    print("BLAD")

if x == "KM" or x == "km":
    print(km_to_miles(y))
elif x == "MI" or x == "mi":
    print(miles_to_km(y))
elif x == "C" or x == "c":
    print(c_to_f(y))
else:
    print(f_to_c(y))