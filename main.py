# zamiana na małe litery i usunięcie niealfanumerycznych znaków
replacements = (',', '-', '!', '?', '.')

# liczba dokumentów
n = int(input())

# dokumenty
documents = []
for _ in range(n):
    my_str = input().lower()  # Zamiana na małe litery
    for r in replacements:
        my_str = my_str.replace(r, ' ')  # Zamiana znaków na spacje
    words = my_str.split()  # Podział na słowa
    documents.append(words)

# liczba zapytań
m = int(input())

# zapytania
queries = []
for _ in range(m):
    query = input().strip().lower()
    queries.append(query)

# przetwarzanie zapytań
for query in queries:
    results = []

    # przetwarzanie każdego dokumentu
    for i, document in enumerate(documents):
        count = document.count(query)
        if count > 0:
            results.append((i, count))  

    # sortowanie: według liczby wystąpień (malejąco), a potem według indeksu dokumentu (rosnąco)
    results.sort(key=lambda x: (-x[1], x[0]))

    # wyświetlanie indeksów dokumentów
    if results:
        print(" ".join(str(i[0]) for i in results))
    else:
        print()
