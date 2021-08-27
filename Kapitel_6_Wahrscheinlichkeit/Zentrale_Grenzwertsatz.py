from collections import Counter
import math
import random
import matplotlib.pyplot as plt


def bernulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0


def binomial(n: int, p: float) -> int:
    """Liefert die Summe von n Bernoulli(p)-Tests"""
    return sum(bernulli_trial(p) for _ in range(n))


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return(1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2


def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """Wählt Punkte aus einem Binomial(n,p) und plottet deren Histogram"""
    data = [binomial(n, p) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], # -0.4, da die Blaken 0.8 breit sind
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
    
    mu = n*p
    sigma = math.sqrt(n*p*(1-p))

    #Zeige neäherte Normalverteilung als Linie
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()


#binomial_histogram(0.75, 100, 100000)

