from typing import List
from ...DataScienceBuch.Kapitel_4_Lineare_Algebra.Vektoren import sum_of_squares
from .Lagemaße import mean

""" Mit der Streuung wird die Eigenschaft einer Liste beschrieben, die angibt, 
wie stark die Werte der Liste auseinanderliegen """

""" Ein einfacher Parameter ist die Distanz zwischen größtem und kleinsten Wert """


def data_range(xs: List[float]) -> float:
    return(max(xs) - min(xs))


""" Eine komplexere Beschreibung erfolgt mithilfe der Varianz """


def de_mean(xs: List[float]) -> List[float]:
    """verschiebe xs durch Abziehen des Mittelwertes (Ergebnis hat Mittelwert 0)"""
    x_bar = mean(xs)
    return [x_i - x_bar for x_i in xs]


def variance(xs: List[float]) -> float:
    """Ungefähr die durchschnittliche quadrierte Abweichung vom Mittelwert"""
    assert len(xs) >= 2, "variance requires at least 2 elements"
    n = len(xs)
    deviation = de_mean(xs)
    # Von jedem Element wird der Mittelwert abgezogen, nun kann man die quadrate der Elemente nehmen
    return(sum_of_squares(deviation)/n)
