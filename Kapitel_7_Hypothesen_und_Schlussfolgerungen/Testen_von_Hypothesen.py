from typing import Tuple
import math
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Kapitel_6_Wahrscheinlichkeit.Zentrale_Grenzwertsatz import normal_cdf
from Kapitel_6_Wahrscheinlichkeit.Wahrscheinlichkeitsverteilungen import inverse_normal_cdf

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Liefert das der Binomialverteilung(n,p) entsprechende mu und sigma"""
    mu = n*p
    sigma = math.sqrt(mu * (1-p))
    return mu, sigma

#die normalverteile kVf _ist_ die Wahrscheinlichkeit,
# dass die Variable unter einer Schwelle liegt
normal_probability_below = normal_cdf

def normal_probability_above(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """Wahrscheinlichkeit, dass ein N(mu, sigma) größer als lo ist"""
    return 1-normal_cdf(lo, mu, sigma)

# Liegt si unter hi und über low, so liegt sie dazwischen
def normal_probability_between(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """Wahrscheinlichkeit, dass N(mu, sigma) innerhalb des Intervalls liegt"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# Sie liegt außerhalb, wenn sie nicht dazwischen liegt
def normal_probability_outside(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """Wahrscheinlichkeit, dass N(mu, sigma) nicht innerhalb des Intervalls liegt"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
    """Berechnet das z, bei dem P(Z <= z) = probability ist"""
    return(inverse_normal_cdf(probability, mu, sigma))


def normal_lower_bound(probability: float, mu: float, sigma: float = 1) -> float:
    """Berechnet das z, bei dem P(Z >= z) = probability ist"""
    return(inverse_normal_cdf(1-probability, mu, sigma))


def normal_two_sided_bounds(probability: float, mu: float, sigma: float) -> Tuple[float, float]:
    """Berechnet die symmetrischen Grenzen (um den Mittelwert),
    die due angegebene Wahrscheinlichkeit enthält"""
    hi = inverse_normal_cdf(0.5 + probability/2, mu, sigma)
    lo = inverse_normal_cdf(0.5 - probability/2, mu, sigma)
    #laut Buch mit den Funktionen von davor
    #probability_outside = (1-probability) / 2
    #upper_bound = normal_lower_bound(probability_outside, mu, sigma)
    #lower_bound = normal_upper_bound(probability_outside, mu, sigma)
    #return lower_bound, upper_bound
    return lo, hi


# Wir entscheiden, eine Münze 1000 Mal zu werfen. Ist die Hypothese der
# Ausgewogenheit richtig, so sollte X annähernd normalverteilt sein mit
# einem Mittelwert von 500 und Standardabweichung von 15,8
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# Signifikanzniveau von 5%
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(int(lower_bound), math.ceil(upper_bound))


# Die Sensitivität des Tests, also die 1-Wahrscheinlichkeit des Fehlers 2. Art 
# kann man nur bestimmen, wenn man die tatsächliche Wahrscheinlichkeit p kennt
# In wirklichkeit ist die Wahrscheinlichkeit beim Münzwurf 0.55 für Kopf
# Wie ist nun die Wahrscheinlichkeit, dass wir den Test nicht verwerfen?

mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
p_second_error = normal_probability_between(lower_bound, upper_bound, mu_1, sigma_1)
sensitivity = 1-p_second_error
print(sensitivity)


#Einseitiger Test mit signifikanzniveau 5%, dass p nicht übermäßig oft Kopf zeigt
upper_bound = normal_upper_bound(0.95, mu_0, sigma_0)
