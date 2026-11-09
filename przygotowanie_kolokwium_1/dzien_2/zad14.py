"""
DZIEŃ 2 — ZADANIE 14: Filtrowanie typów i statystyki ręczne
Tematyka: Filtrowanie typów i statystyki ręczne.
Źródło: Lab06/zad02.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 25 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

NARZĘDZIA I SKŁADNIA DO TEGO ZADANIA

Własne funkcje (def)
W tym ćwiczeniu zdefiniuj: integer_stats(data); możesz nazwać drugą wersję integer_stats_manual(data). Obliczenia da się również zapisać bez def, ale końcowa wersja ma ćwiczyć wskazane funkcje i zwracać wyniki przez return.

Co wykorzystać
- type(x) is int odróżnia int od bool; isinstance(x,str) rozpoznaje tekst.
- strip() usuwa białe znaki z końców tekstu, indeksowanie/wycinek pozwalają sprawdzić pojedynczy znak + lub -.
- Porównanie '0'<=char<='9' sprawdza cyfrę ASCII; all(...) albo pętla sprawdza cały fragment.
- int(text) konwertuje dopiero po weryfikacji; append() buduje listę liczb.
- W pierwszej wersji: sum(), len(), min(), max(). W ręcznej: licznik, suma, porównania i None.

Małe przykłady składni — nie są całym rozwiązaniem
    print(type(True) is int)  # False
    print(isinstance(True, int))  # True
    print('  +007  '.strip())  # +007
    print('0' <= '5' <= '9')  # True

Inny sposób / wariant bez własnych funkcji
W ręcznej wersji nie używaj sum/min/max/len — policz wynik pętlą. all() także nie jest konieczne: można odrzucić tekst po znalezieniu błędnego znaku. Samo str.isdigit() dopuszcza również niektóre znaki spoza ASCII, więc nie realizuje dokładnie tego warunku. Własne funkcje są wymagane.

Poniższe polecenie określa wymagania. Narzędzia opisane jako opcjonalne
lub alternatywne są do wyboru; nie musisz używać wszystkich naraz.

POLECENIE
★ Funkcja integer_stats(data) przyjmuje listę dowolnych obiektów. Zachowaj int, lecz odrzuć bool i float. Dla str zaakceptuj po strip() opcjonalny pojedynczy + lub - i co najmniej jedną cyfrę ASCII 0..9; przelicz na int. Inne elementy odrzuć. Zwróć (lista,suma,srednia,min,max), dla braku liczb ([],0,None,None,None). Zrób wersję z sum/min/max/len i wersję ręczną bez tych czterech funkcji. To zadanie funkcyjne, bez czytania reprezentacji listy przez eval.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
[7," -2 ",True,None,"5","2.0",3.0] -> ([7,-2,5],10,10/3,-2,7).

SPRAWDŹ TAKŻE
Pusty napis, sam znak +, "--2", False, zero, pusta lista, łańcuch "007".

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
