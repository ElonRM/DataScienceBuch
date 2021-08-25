from typing import Counter, List
import numpy

num_friends = numpy.random.binomial(100, 0.06, 206)


def mean(xs: List[float]) -> float:
    return sum(xs)/len(xs)


print(mean(num_friends))

# Die Unterstriche zeigen, dass dies "private" Funktionen sind, da sie nur
# von unserer median Funktion, nicht aber von anderen Nutzern unserer Statistik
# Bibliotek verwendet werden sollen


def _meadian_even(xs: List[float]) -> float:
    """Liefert den Mittelwert die zwei mittleren Einträge"""
    return (sorted(xs)[len(xs)//2-1] + sorted(xs)[len(xs)//2])/2


def _median_odd(xs: List[float]) -> float:
    """Liefert den Median"""
    return sorted(xs)[len(xs)//2]


def median(v: List[float]) -> float:
    """Lifert den Median abhängig von gerade/ungeraden Anzahlen"""
    return _median_odd(v) if len(v) % 2 == 1 else _meadian_even(v)


print(median(num_friends))


def quatile(xs: List[float], p: float) -> float:
    """Liefert den Wert des p-ten Perzentils"""
    return sorted(xs)[int(len(xs)*p)]


def mode(xs: List[float]) -> List[float]:
    """Liefert eine Liste, denn es kann mehr als einen Modus geben"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i
            for x_i, count in counts.items()
            if count == max_count]


print(mode(num_friends))
