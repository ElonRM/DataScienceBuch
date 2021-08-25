from typing import Callable, Dict, Iterable, List, Optional, Tuple


# Der Code wird dadurch nur lesbarer, ändern tut sich nichts,
def total(xs: List[float]) -> float:
    # Man sagt dem Leser, dass xs eine Liste aus floats ist und die Rückgabe auch eine float ist
    return sum(xs)


x: int = 5  # ein x ist eigentlich offensichtlich ein int, aber wie erwähnt hat es keine Funktion
y: int = 4.6  # das funktioniert genauso
print(x, y)


values: List[int] = []
best_so_far: Optional[float] = None

# keys sind strings, Werte sind ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# Listen und Generatoren sind beide Iterables
lazy = True
if lazy:
    events: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    events = [0, 2, 4, 6, 8]

# Tupel geben einen Typ für jedes Element an
triple: Tuple[int, float, int] = (10, 2.3, 5)

# Der Type Hint besagt, dass repeater eine Funktion ist, die zwei Argumente
# erwartet: einen String und einen Int. Zurück gibt sie einen String.


def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)


print(comma_repeater("five", 5))  # five, five, five, five, five
assert twice(comma_repeater, "type hints") == "type hints, type hints"


# Da es sich bei Type Annotations einfahc um PYhton Objekte handeln,
# kann man sie Variablen zuweisen, um sihc leichter darauf beziehen zu können
Number = int
Numbers = List[Number]


def total(xs: Numbers) -> Number:
    return(sum(xs))
