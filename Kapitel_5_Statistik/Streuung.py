from typing import List
from Lagemaße import mean, quantile
import numpy
import os
import sys
import math
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# muss immer nach sys.path.. stehen
from Kapitel_4_Lineare_Algebra.Vektoren import sum_of_squares


print("Execution of run starts")


num_friends = numpy.random.binomial(100, 0.06, 206)

""" Mit der Streuung wird die Eigenschaft einer Liste beschrieben, die angibt, 
wie stark die Werte der Liste auseinanderliegen """

""" Ein einfacher Parameter ist die Distanz zwischen größtem und kleinsten Wert """


def data_range(xs: List[float]) -> float:
    return(max(xs) - min(xs))


""" Eine komplexere Beschreibung erfolgt mithilfe der Varianz """


def de_mean(xs: List[float]) -> List[float]:
    """ verschiebe xs durch Abziehen des Mittelwertes (Ergebnis hat Mittelwert 0) """
    x_bar = mean(xs)
    return [x_i - x_bar for x_i in xs]


def variance(xs: List[float]) -> float:
    """ Ungefähr die durchschnittliche quadrierte Abweichung vom Mittelwert """
    assert len(xs) >= 2, "variance requires at least 2 elements"
    n = len(xs)
    deviation = de_mean(xs)
    # Von jedem Element wird der Mittelwert abgezogen, nun kann man die quadrate der Elemente nehmen
    return(sum_of_squares(deviation)/n)


print("Varianz:", variance(num_friends))


def standard_deviation(xs: List[float]) -> float:
    """ Die Standardabweichung ist die Wurzel der Varianz """
    return math.sqrt(variance(xs))

""" Eine Robuste Alternative ist es, die Differenz zwischen dem 75.
und dem 25. Perzentil zu berechnen """


def interquartile_range(xs: List[float]) -> float:
    """ Liefert die Different zwischen dem 75. und 25. Perzentil"""
    return(quantile(0.75) - quantile(0.25))