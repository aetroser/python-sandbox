"""
DZIEŃ 2 — ZADANIE 02: Kopia listy i współdzielenie danych
Tematyka: Kopia listy i współdzielenie danych.
Źródło: Lab05/01 Data structures/08 - basic operations on lists.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 10 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
Nie musisz tworzyć własnej funkcji przez def. Możesz napisać program bezpośrednio w pliku; nadal używasz potrzebnych funkcji wbudowanych, np. input() i print().

Co wykorzystać
- a=[...]: lista; b=a: druga nazwa tego samego obiektu.
- a[:] albo a.copy(): płytka kopia listy; append(x): dopisanie na końcu.
- lista[i]=x: zmiana elementu; print(lista): reprezentacja z nawiasami.
- == porównuje zawartość, is sprawdza tożsamość obiektu; id(obiekt) może pomóc w obserwacji.

Małe przykłady składni — nie są całym rozwiązaniem
    a = [10, 20]
    b = a
    c = a.copy()
    print(a is b)  # True
    print(a is c)  # False

Inny sposób / wariant bez własnych funkcji
Wystarczą przypisania, wycinek i append; nie trzeba pisać def ani importować modułu. copy.deepcopy to inny rodzaj kopiowania i nie zastępuje obserwacji płytkiej kopii wymaganej w tym zadaniu.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Utwórz a=[2,4,6], b=a i c=a[:]. Wykonaj b.append(8), następnie c[0]=99. Przed uruchomieniem zapisz przewidywane wartości a,b,c w komentarzu. Potem wypisz każdą listę w osobnej linii. W dodatkowej próbie z listą [[1],[2]] sprawdź, co robi płytka kopia, gdy modyfikujesz wewnętrzną listę.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Pierwsza próba: [2, 4, 6, 8] / [2, 4, 6, 8] / [99, 4, 6].

SPRAWDŹ TAKŻE
Różnica przypisania i kopiowania; a==c i a is c oznaczają różne pytania.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
