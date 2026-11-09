"""
D1.09: Wzór i rozłączne przedziały | Lab04
Wczytaj wzrost w m i masę w kg; BMI=masa/wzrost². Wypisz 2 miejsca i pasmo przed zaokrągleniem.
Wymagane: bmi(height,mass), band(height,mass); A:<18.5, B:[18.5,25), C:[25,30), D:≥30.
Wejście/próba: 2 100
Wynik: 25.00 / C
Przydatne: float(), split(), **2, if/elif, print(f'{x:.2f}'); moduły zbędne.
"""

# Tutaj napisz swoje rozwiązanie.

def bmi(height,mass):
    if height == 0:
        return 0

    return mass / (height * height)

def band(height,mass):
    value = bmi(height,mass)

    if value < 18.5:
        return "A"
    if 18.5 <= value < 25:
        return "B"
    if 25 <= value < 30:
        return "C"

    return "D"

h, m = map(float, input().split())

print(f"{bmi(h,m):.2f}", band(h,m))