"""
DZIEŃ 1 — ZADANIE 13: Moduł random i powtarzalny eksperyment
Tematyka: Moduł random i powtarzalny eksperyment.
Źródło: Lab02/zad07.py; Lab05/03 Zadania (do przesłania)/zad01.py (ścieżki względem Labs/ w oryginalnym Labs.zip).
Poziom: ★ rozszerzenie. Orientacyjny czas: 20 min.
Środowisko: Python 3.10+; wyłącznie biblioteka standardowa.
Cel: samodzielne rozwiązanie; poniżej nie ma gotowego algorytmu.

POLECENIE
★ Zdefiniuj experiment(seed,n). Utwórz lokalny generator random.Random(seed). Wylosuj n liczb randint(0,10), następnie jeden adres z listy ["a@gmail.com","b@interia.com","c@gmail.com"] po odfiltrowaniu gmail.com, następnie potasuj kopię tej listy. Zwróć krotkę (liczby,adres,potasowana_lista). Nie zmieniaj pierwotnej listy. Osobno sprawdź randrange(0,10), random(), choices(...,k=3) oraz sample(...,k=3); opisz różnice w komentarzu.

PRZYKŁAD / SPRAWDZENIE RĘCZNE
Dwa wywołania experiment(42,5) w tej samej wersji Pythona mają dać identyczne wyniki; liczby należą do 0..10.

SPRAWDŹ TAKŻE
n=0; randint zawiera oba końce, randrange nie zawiera stop; choices dopuszcza powtórzenia, sample wybiera pozycje bez zwracania.

ZASADY
Liczby rzeczywiste zapisuj z kropką. Nie sprawdzaj błędów danych,
jeśli polecenie nie wymaga tego wprost. W zadaniach z konsolą czytaj
bez komunikatów input(), a wypisuj tylko wskazany wynik.
Gdy polecenie wymaga funkcji, funkcja zwraca wynik; przykładowe
wywołania umieść pod if __name__ == '__main__':.
To ćwiczenie sprawdzasz ręcznie; automatyczne testery dotyczą kolokwiów.
"""

# Tutaj napisz swoje rozwiązanie.
