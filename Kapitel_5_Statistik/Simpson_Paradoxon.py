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