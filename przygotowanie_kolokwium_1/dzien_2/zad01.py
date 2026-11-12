"""
D2.01: Indeksy i slicing | Lab05
Wczytaj tekst (min. 4 znaki); wypisz pierwszy, ostatni, pierwszą połowę, co drugi znak i tekst od tyłu.
Własne funkcje zbędne.
Wejście/próba: Python
Wynik: P / n / Pyt / Pto / nohtyP
Przydatne: input(), len(), //2, s[0], s[-1], s[:k], s[::2], s[::-1].
"""

# Tutaj napisz swoje rozwiązanie.
input_text = str(input())

if (len(input_text) < 4):
    exit("Zbyt krótki tekst")

print(input_text[0])
print(input_text[-1:])
print(input_text[:int(len(input_text)/2)])
print(input_text[::-1])
print(input_text[::2])