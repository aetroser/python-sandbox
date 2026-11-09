"""
D1.13: Moduł random i powtarzalny eksperyment | Lab02, Lab05 ★
Wylosuj kolejno n int 0..10, adres Gmail z [a@gmail.com,b@interia.com,c@gmail.com], potasuj kopię listy.
Wymagana: experiment(seed,n) → (liczby,adres,kopia); porównaj także randrange/random/choices/sample.
Wejście/próba: experiment(7,3)
Wynik: ([5,2,6], "a@gmail.com", ["b@interia.com","c@gmail.com","a@gmail.com"])
Przydatne: random.Random(seed), randint(), choice(), copy(), shuffle(); filtrowanie może być pętlą.
"""

# Tutaj napisz swoje rozwiązanie.

import random

ADDRESSES = ["a@gmail.com", "b@interia.com", "c@gmail.com"]

def experiment(seed, n):
    rng = random.Random(seed)
    numbers = [rng.randint(0, 10) for _ in range(n)]
    gmail = []
    for addr in ADDRESSES:
        if addr.endswith("@gmail.com"):
            gmail.append(addr)
    address = rng.choice(gmail)
    copy = ADDRESSES.copy()
    rng.shuffle(copy)

    return (numbers, address, copy)

x, y = map(int, input().split())
print(experiment(x, y))