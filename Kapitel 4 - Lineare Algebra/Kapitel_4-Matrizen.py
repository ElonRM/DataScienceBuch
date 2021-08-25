from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[Vector]

A = [[1, 2, 3],  # A besitzt 2 Zeilen und 3 Spalten
     [4, 5, 6]]

B = [[1, 2],  # B besitzt 3 Zeilen und 2 Spalten
     [3, 4],
     [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Liefert (Anzahl an Zeilen, Anzahl an Spalten) von A"""
    num_rows: len(A)
    num_cols: len(A[0]) if A else 0  # Anzahl der Elemente in erster Zeile
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Liefert i-te Zeile als Vector"""
    return(A[i])  # A[i] ist bereits die i-te Zeile


def get_column(A: Matrix, j: int) -> Vector:
    """Liefert i-te Spalte als Vector"""
    return[A_i[j]
           for A_i in A]  # von jeder Zeile A_i wird das j-te element genommen


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Liefert eine num_rows x num_cols Matrix, in der
    der Eintrag (i, j) durch entry_fn(i, j) erzeugtwird
    """
    return[[entry_fn(i, j)
            for j in range(num_cols)]  # Anzahl der Spalten
           for i in range(num_rows)]   # Anzahl der Zeilen


def identity_matrix(n: int) -> Matrix:
    """Liefert n x n Einheitsmatrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
