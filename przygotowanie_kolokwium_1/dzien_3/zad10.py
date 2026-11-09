"""
DZIEŃ 3 — ZADANIE 10: Progi ocen i kolejność warunków
Tematyka: Progi ocen i kolejność warunków.
Źródło: Lab06/zad09.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: podstawa. Orientacyjny czas: 15 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: calculate_grade(points,max_points,thresholds). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- Punkty/maksimum i *100 dają procent; > oznacza przekroczenie, nie osiągnięcie progu.
- Lista krotek; for threshold,grade in thresholds rozpakowuje każdy próg i ocenę.
- if oraz return: zwrócenie pierwszej pasującej oceny; po przejrzeniu progów wartość domyślna.
- int(), input().split(), print(): odczyt i wypisanie int.

Małe przykłady składni — nie są całym rozwiązaniem
    limits = [(90, 'A'), (70, 'B')]
    for boundary, label in limits:
        print(boundary, label)  # przykład rozpakowania pary

Inny sposób / wariant bez własnych funkcji
Wariant bez pętli to if/elif dla kolejnych progów; wariant bez def także policzy ocenę. Końcowa wersja ma jednak wykorzystywać calculate_grade i przekazaną listę thresholds. Nie używaj round() przed porównaniem.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
Zdefiniuj calculate_grade(points,max_points,thresholds). Progi to [(80,5),(60,4),(50,3)] w kolejności malejącej. Ocena odpowiada pierwszemu progowi, który procent ściśle przekracza; gdy brak, 2. max_points>0, 0<=points<=max_points. Wczytaj points max_points i wypisz ocenę. Te progi są wyłącznie ćwiczeniem z Lab06; prawdziwe kolokwium oceniane jest liczbą całych zadań.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
80 100 -> 4; 81 100 -> 5; 50 100 -> 2; 51 100 -> 3.

SPRAWDŹ TAKŻE
Dokładnie 50%,60%,80%; 0 i 100%; nie zaokrąglaj procentu przed decyzją.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
