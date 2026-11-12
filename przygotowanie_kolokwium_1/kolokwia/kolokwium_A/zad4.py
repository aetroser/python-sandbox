"""
Kol. A.4: Statystyka słów | Lab03, Lab05
Zamień ,.!?;: na spacje i litery na małe; wypisz liczbę słów, różnych słów, zwycięskie słowo i licznik.
Własne funkcje opcjonalne; remis → najmniejsze alfabetycznie; brak słów → 0 / 0 / BRAK.
Wejście/próba: Kot, pies! KOT pies ala.
Wynik: 5 / 3 / kot 2
Przydatne: replace(), lower(), split(), słownik, get() lub if/in, len(), min()/max() lub pętla.
"""

# Tutaj napisz swoje rozwiązanie.
some_text = str(input()).lower()

for znak in ",.!?;:":
    some_text = some_text.replace(znak, " ")

slowa = some_text.split()

if len(slowa) == 0:
    print("0 / 0 / BRAK")
else:
    liczniki = {}
    for slowo in slowa:
        liczniki[slowo] = liczniki.get(slowo, 0) + 1

    zwyciezca = None
    for slowo in sorted(liczniki):
        if zwyciezca is None or liczniki[slowo] > liczniki[zwyciezca]:
            zwyciezca = slowo

    print(len(slowa), "/", len(liczniki), "/", zwyciezca, liczniki[zwyciezca])