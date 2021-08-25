list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]

pairs = [pair for pair in zip(list_1, list_2)]
print(pairs)

letters, numbers = zip(*pairs)


def add(a, b):
    return a+b


print(add(1, 2))

try:
    print(add([1, 2]))
except TypeError:
    print("add expects two inputs")

print(add(*[1, 2]))
