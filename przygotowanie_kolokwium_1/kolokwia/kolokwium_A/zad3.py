"""
Kol. A.3: Malejące trójki z nakładaniem | Lab05
Wczytaj listę int (może być pusta); wypisz każde sąsiadujące okno a>b>c w kolejności początku.
Własne funkcje opcjonalne; nakładanie i identyczne trójki dozwolone; brak → BRAK.
Wejście/próba: 5 4 3 2 1
Wynik: 5 4 3 / 4 3 2 / 3 2 1
Przydatne: list(map(int,input().split())), len(), range()/while, indeksy, [i:i+3], print(*trojka).
"""

# Tutaj napisz swoje rozwiązanie.
int_list = [int(i) for i in input().split()]

groups = []
for i in range(len(int_list)-2):
    if int_list[i] > int_list[i+1] > int_list[i+2]:
        groups.append(" ".join(map(str,int_list[i:i+3])))

print(" / ".join(groups))