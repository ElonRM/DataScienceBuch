import math
from typing import List

Vector = List[float]

height_weight_age = [
    70,   # Pfund
    170,  # Pfund
    50    # Jahre
]

grades = [
    95,
    85,
    75,
    62
]

# WIr müssen zuerst unsere Eigene Funktion zum Addieren und Subtrahieren von Vektoren schreiben


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def substract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i-w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    # Prüfe, dass vectors nicht leer ist
    assert vectors, "no vectors provided!"

    # Prüfe, dass alle die gleiche Länge haben
    vector_length = len(vectors[0])
    assert all(len(v) == vector_length for v in vectors), "different sizes!"

    # Jede Komponente aller Vektoren aufaddieren
    return([sum(vector[i] for vector in vectors) for i in range(vector_length)])


# Eine Funktion, um ein Vektor mit einem Skalar(eine Zahl) zu multiplizieren
def scalar_multiply(c: float, v: Vector) -> Vector:
    return[c*v_i for v_i in v]

# Zusammen ermöglicht das, einen Vektor aus den Mittelwerten der Komponenten aller Vektoren zu bestimmen


def vector_mean(vectors: List(Vector)) -> Vector:
    return(scalar_multiply(1/len(vectors), vector_sum(vectors)))


# Skalarprodukt
def dot_product(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "Vectors must be same length"
    return(sum(v_i * w_i for v_i, w_i in zip(v, w)))


# Damit lässt sich die Summe der Quadrate eines Vektors leicht berechnen
def sum_of_squares(v: Vector) -> float:
    return dot_product(v, v)


# Nun kann man auch einfach den Betrag eines Vektors bestimmen
def magnitude(v: Vector) -> float:
    math.sqrt(sum_of_squares(v))


# Jetzt kann man den "Abstand" zweier Vektoren berechnen
def distance(v: Vector, w: Vector) -> float:
    return(magnitude(substract(v, w)))
