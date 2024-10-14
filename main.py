import string
from collections import defaultdict

# zamiana na małe litery i usunięcie niealfanumerycznych znaków
def przeksztalc_tekst(wpis):
    konwerter = str.maketrans('', '', string.punctuation)
    return wpis.translate(konwerter).lower().split()

# liczba dokumentów
n = int(input("Podaj liczbę dokumentów: "))

# dokumenty
dokumenty = []

for _ in range(n):
    tresc_dokumentow = input("->").strip()
    dokumenty.append(tresc_dokumentow)  # przetwarzamy dokumenty

# liczba zapytań
m = int(input("Podaj liczbę zapytań: "))

# zapytania
zapytania = []
for _ in range(m):
    zapytanie = input("->").strip().lower()
    zapytania.append(zapytanie)


mapa_wynikow = defaultdict(lambda: defaultdict(int))

# przetwarzanie dokumentów
for i, dokument in enumerate(dokumenty):
    zmodyfikowany_plik = przeksztalc_tekst(dokument)

    # Zliczanie wystąpień zapytań w każdym dokumencie
    for pytanie in zapytania:
        liczba_wystapien = zmodyfikowany_plik.count(pytanie)
        mapa_wynikow[i][pytanie] = liczba_wystapien

for pytanie in zapytania:
    wynik = [(indeks_pliku, mapa_wynikow[indeks_pliku][pytanie]) for indeks_pliku in range(n) if
                       mapa_wynikow[indeks_pliku][pytanie] > 0]
    # sortowanie: według liczby wystąpień (malejąco), a potem według indeksu dokumentu (rosnąco)
    wynik.sort(key=lambda x: (-x[1], x[0]))

    # wyświetlanie indeksów dokumentów
    wynik_koncowy = [indeks_pliku for indeks_pliku, _ in wynik]
    print(wynik_koncowy)
