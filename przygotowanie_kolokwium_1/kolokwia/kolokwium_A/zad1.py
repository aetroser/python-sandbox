"""
Kol. A.1: Sumy i liczności w przedziale | Lab02, Lab03
Dla a b wypisz: liczność i sumę parzystych, potem nieparzystych z domkniętego przedziału między nimi.
Własne funkcje opcjonalne; zero jest parzyste, granice mogą być odwrócone.
Wejście/próba: -2 3
Wynik: 3 0 / 3 3
Przydatne: map(int,input().split()), min()/max() lub if, range(), %2, +=.
"""

# Tutaj napisz swoje rozwiązanie.

start, end = map(int, input().split())

even_count = end // 2 - (start - 1) // 2
odd_count = (end - start + 1) - even_count

even_sum = 0
odd_sum = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(even_count, even_sum, "/", odd_count, odd_sum)