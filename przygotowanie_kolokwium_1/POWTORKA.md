# Co powtórzyć przed próbą

To lista pojęć i pułapek, bez gotowych rozwiązań zadań.

## Lab02 — wejście, pętle, losowanie

- `input()` daje `str`; do obliczeń potrzebujesz `int` lub `float`. Liczby zapisuj z kropką.
- W `range(start, stop)` końcowa granica jest wyłączona. W zadaniach przedział może być domknięty.
- `break` kończy pętlę; `continue` przechodzi do następnego obiegu. W `while` pamiętaj o zmianie licznika także na ścieżce z `continue`.
- `randint(a,b)` zawiera oba końce; `randrange(a,b)` pomija b. `random()` daje float z [0,1).
- `choice` wybiera jeden element, `choices` dopuszcza ponowny wybór pozycji, `sample` wybiera bez zwracania. `shuffle` modyfikuje listę.
- Jedna runda z czterema kośćmi oznacza cztery wyniki naraz. Cztery jedynki z różnych rund nie są rundą samych jedynek.

## Lab03–Lab04 — funkcje i liczby

- `return` przekazuje wynik; `print` tylko wypisuje. Funkcja bez `return` zwraca `None`.
- Oddziel część obliczeniową od `input`/`print`. Import modułu nie powinien rozpoczynać pytania o dane.
- `if __name__ == '__main__':` oddziela uruchomienie pliku od jego importowania.
- 0 i liczby ujemne nie są pierwsze; 1 też nie. 2 jest pierwsza. `0! = 1`.
- Rekurencja potrzebuje warunku kończącego. Nie nazywaj własnych zmiennych `sum`, `list`, `str` czy `type`.
- Dla równania kwadratowego rozpatrz trzy znaki delty. Uporządkuj dwa pierwiastki, zwłaszcza gdy a<0.
- `math.sqrt` jest do nieujemnych liczb rzeczywistych; `cmath.sqrt` obsługuje liczby zespolone.
- Przy sumach prostokątów rozróżnij liczbę części n, szerokość h i punkt lewego końca.

## Lab05 — napisy i kolekcje

- Indeksy zaczynają się od 0, ostatni ma indeks -1. W wycinku `[i:j]` pozycja j jest wyłączona.
- `split()` bez argumentu pomija wielokrotne białe znaki. `split(' ')` może tworzyć puste elementy.
- `strip(',.')` usuwa znaki wyłącznie z końców; nie zastępuje interpunkcji wewnątrz słowa spacją.
- Napisy i krotki są niemutowalne. Lista jest mutowalna; `b=a` nie tworzy kopii listy.
- `remove` usuwa pierwszą pasującą wartość; `pop` usuwa po indeksie i zwraca usunięty element.
- `sorted` zwraca nową listę. `sort` zmienia listę i zwraca `None`. Sortowanie jest stabilne.
- W słowniku klucz jest unikalny: przypisanie istniejącego klucza aktualizuje wartość. `in` sprawdza klucze, a nie wartości.
- Zbiór usuwa duplikaty, lecz nie zapewnia kolejności potrzebnej do wyjścia. Posortuj wynik lub zachowaj osobną listę kolejności.
- Przy nakładających się oknach po trafieniu idź o 1. Bez nakładania po trafieniu idź o długość zużytego okna.

## Lab06 — daty, statystyka, warunki

- `bool` jest podtypem `int`. Jeżeli polecenie wyklucza boole, samo `isinstance(x,int)` nie wystarczy.
- `date` to data, `datetime` także czas. Różnica dwóch dat to `timedelta`; liczbę dni pobierz z `.days`.
- `weekday()` daje 0 dla poniedziałku; `isoweekday()` daje 1. Nie mieszaj konwencji.
- Wiek to pełne lata, a nie liczba dni podzielona przez 365. Doprecyzuj regułę dla 29 lutego.
- Rok podzielny przez 100 musi być także podzielny przez 400, aby był przestępny.
- Mediana parzystej listy to średnia dwóch środkowych elementów po sortowaniu. Przy remisie mody stosuj regułę z polecenia.
- `variance` i `stdev` dotyczą próby i wymagają co najmniej 2 danych; wersje z prefiksem `p` dotyczą populacji.
- Nie zaokrąglaj przed decyzją o progu. Rozróżniaj `>` oraz `>=`, a warunki sprawdzaj od najbardziej szczegółowych.

## Przed oddaniem każdego pliku

- Czy poprawne są nazwa pliku i wszystkie wcięcia?
- Czy liczba i kolejność wypisywanych wierszy odpowiadają poleceniu?
- Czy nie ma zachęt `Podaj...`, debugujących `print` i dodatkowych pustych wierszy?
- Czy sprawdziłeś puste/minimalne dane, duplikaty, remisy, zero i dokładne granice, o ile są dozwolone?
- Czy po ostatniej zmianie program nadal przechodzi przykład?

[Oficjalne źródła i mapa materiału](ZAKRES_I_ZRODLA.md).
