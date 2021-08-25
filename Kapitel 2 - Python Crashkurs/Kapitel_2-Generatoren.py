def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in generate_range(10):
    print(f"i: {i}")


def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


for i in natural_numbers():
    print(i)

lazy_evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# solche Generatoren tuen nichts, bis man über sie iteriert. Ansonsten wird noch nichts berechnet

# Keine dieser Berechnungen tut etwas, bevor man nicht darüber iteriert.
data = natural_numbers()
evens = (x for x in data if i % 2 == 0)
even_squares = (x**2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)


names = ["Alice", "Bob", "Charlie", "Debbie"]

# Man schreibt nicht
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# Sondern benutzt Enumerate
# Man schreibt es so
for i, name in enumerate(names):
    print(f"name{i} is {name}")
