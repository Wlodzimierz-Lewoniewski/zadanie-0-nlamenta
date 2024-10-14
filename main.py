import string

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
    dokumenty.append(przeksztalc_tekst(tresc_dokumentow))  # przetwarzamy dokumenty

# liczba zapytań
m = int(input("Podaj liczbę zapytań: "))

# zapytania
zapytania = []
for _ in range(m):
    query = input().strip().lower()
    zapytania.append(query)

# przetwarzanie zapytań
for zapytanie in zapytania:
    results = []

    # przetwarzanie każdego dokumentu
    for i, document in enumerate(dokumenty):
        liczba = document.count(zapytanie)  # zliczamy wystąpienia pojedynczego zapytania
        if liczba > 0:
            results.append((i, liczba))

    # sortowanie: według liczby wystąpień (malejąco), a potem według indeksu dokumentu (rosnąco)
    results.sort(key=lambda x: (-x[1], x[0]))

    # wyświetlanie indeksów dokumentów
    if results:
        print(" ".join(str(i[0]) for i in results))
    else:
        print()
