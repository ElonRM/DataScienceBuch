from typing import List
from matplotlib import pyplot as plt
import numpy
import os
import sys
import math
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# muss immer nach sys.path.. stehen
from Kapitel_5_Statistik.Streuung import de_mean, standard_deviation
from Kapitel_4_Lineare_Algebra.Vektoren import dot_product


num_friends = numpy.random.binomial(100, 0.1, 206)
daily_minutes = [num_friends[x_i] * numpy.random.normal(2.5,0.5) for x_i in range(len(num_friends))]


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must be same length"

    return dot_product(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

print("Covariance: ", covariance(num_friends, daily_minutes))


def correlation(xs: List[float], xy: List[float]) -> float:
    """Misst, wie stark xs und xy bzw. ihrer Mittelwerte variieren"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(xy)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, xy) / stdev_x / stdev_y
    else:
        return 0 # wenn es keine Streuung gibt, ist die Korrelation gleich 0

print("Correlation: ", correlation(num_friends, daily_minutes))

# Untersuchung der Daten via matplotlib

plt.scatter(num_friends, daily_minutes)
plt.xticks([20 * x_i for x_i in range(3)])
plt.yticks([20 * y_i for y_i in range(6)])
plt.axes([0,50,0,100])
plt.xlabel("# of friends")
plt.ylabel("# of minutes")
plt.title("Correlation with an Outlier")
plt.show()