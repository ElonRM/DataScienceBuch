# Anstatt mithilfe eines Signifikanzniveaus Grenzen für ein Test festzulegen,
# kann man eine Wahrscheinlichkeit dafür berechnen, dass man einen mindestens
# so extremen Wert wie den gerade beobachteten sehen wird unter der Annahme,
# dass H_0 war ist.
from typing import Tuple
import math
import os
import sys
import random
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import Testen_von_Hypothesen as pbty

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    Wie wahrscheinlich ist es, dass man einen mindestens so extremen Wert
    wie x erhält, wenn die Werte aus einem N(mu, sigma) stammen.
    """
    if x > mu:
        return 2 * pbty.normal_probability_above(x, mu, sigma)
    if x < mu:
        return 2 * pbty.normal_probability_below(x, mu, sigma)

mu_0, sigma_0 = pbty.normal_approximation_to_binomial(1000, 0.5)


#Veranschaulichung der Stetigkeitskorrektur

extreme_value_count = 0
trials = 10000
for _ in range(trials):
    num_heads = sum(1 if random.random() > 0.5 else 0
                    for _ in range(1000))
    if num_heads <= 470 or num_heads >= 530:
        extreme_value_count +=1

print("Mit Stetigkeitskorrektur: ", two_sided_p_value(470.5, mu_0, sigma_0))# 0.062077
print("Ohne Stetigkeitskorrektur: ", two_sided_p_value(470, mu_0, sigma_0))# 0.057779
print("Reales Versuchsegbenis: ", extreme_value_count/trials) # 0.06168 bei trials = 100000

upper_p_value = pbty.normal_probability_above
lower_p_value = pbty.normal_probability_below

#Bei dem Test wird 525x kopf betrachtet

print("upper_p_value_525: ", upper_p_value(524.5, mu_0, sigma_0)) #0.0606

#Demnach würden wir H_0 nicht verwerfen, da die Warscheinlichkeit hierfür über 5% liegt

print("upper_p_value_527: ", upper_p_value(526.5, mu_0, sigma_0))


# KONFIDENZINTERVALLE


# Bei einem Münzwurf Test erscheint aus 1000 Würfen 523x Kopf
# Daraus schätzt man, dass p_Kopf = 0.523 ist
mu_1, sigma_1 = pbty.normal_approximation_to_binomial(1000, 0.523)
# Nun sagt man (als Beispiel), dass man sich zu 95% sicher ist, dass das folgende Intervall
# den wahren Parameter p enthält. Nimmt man z.B 0.4 ist die Wahrscheinlichkeit nur noch 40%,
# dass das wahre p im Intervall ist
hi_p, low_p = pbty.normal_two_sided_bounds(0.95, mu_1, sigma_1)
print(f"Das wahre p ist zu 95% im Intervall", [low_p, hi_p])