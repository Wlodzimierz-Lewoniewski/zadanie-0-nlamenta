from collections import defaultdict
import re

# zamiana na małe litery i usunięcie niealfanumerycznych znaków
def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', ' ', text).lower()

# liczba dokumentów
n = int(input("Podaj liczbę dokumentów:"))

# dokumenty
documents = [input("->").lower().split() for _ in range(n)]

# liczba zapytań
m = int(input("Liczba zapytań:"))

# zapytania
queries = [input("->").strip().lower() for _ in range(m)]

# przetwarzanie zapytań
for query in queries:
    results = []

    for i, document in enumerate(documents):
        count = document.count(query)
        if count > 0:
            results.append((i, count))

    results.sort(key=lambda x: (-x[1], x[0]))

    # wyświetlanie indeksów dokumentów
    if results:
        print(" ".join(str(i[0]) for i in results))
    else:
        print()

