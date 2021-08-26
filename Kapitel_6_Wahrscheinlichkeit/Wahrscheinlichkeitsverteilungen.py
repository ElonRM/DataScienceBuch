import math
import matplotlib.pyplot as plt
import numpy


def uniform_cdf(x: float) -> float:
    """Wahrscheinlichkeit, dass eine gleichverteilte Zufallsgröße <=x ist"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


xs = [x / 100.0 for x in range(-100, 200)]
plt.plot(xs, [uniform_cdf(x_i) for x_i in xs])
plt.legend()
plt.axis([-1, 2, -0.5, 2])
plt.title("The uniform cdf")
plt.show()


SQRT_TWO_PY = math.sqrt(2*math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return(math.exp(-(x-mu) ** 2 / (2 * sigma ** 2))/(sigma*SQRT_TWO_PY))

xs = [x/10 for x in range(-50,50)]
plt.plot(xs, [normal_pdf(x,sigma = 1) for x in xs], '-', label = 'mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x,sigma = 2) for x in xs], '--', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x,sigma = 0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x,mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend()
plt.title("Various normal pdfs")
plt.show()