"""
D2.14: Filtrowanie typów i statystyki ręczne | Lab06 ★
Zachowaj int bez bool i teksty: po strip() opcjonalny +/− oraz cyfry ASCII; odrzuć float i resztę.
Wymagana: integer_stats(data) → (lista,suma,średnia,min,max); dwie wersje, druga bez sum/min/max/len.
Wejście/próba: [7," -2 ",True,None,"5","2.0",3.0]
Wynik: ([7,-2,5],10,3.3333333333333335,-2,7); brak liczb: ([],0,None,None,None)
Przydatne: type(x) is int, isinstance(x,str), strip(), '0'<=c<='9', int(), pętle; bez eval().
"""

# Tutaj napisz swoje rozwiązanie.
