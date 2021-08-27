import math
import matplotlib.pyplot as plt
import numpy


def plot_uniform_cdf():
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


def plot_normal_pdf():
    SQRT_TWO_PY = math.sqrt(2*math.pi)

    def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return(math.exp(-(x-mu) ** 2 / (2 * sigma ** 2))/(sigma*SQRT_TWO_PY))

    xs = [x/10 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1)
             for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2)
             for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5)
             for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1)
             for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.title("Various normal pdfs")
    plt.show()


def plot_normal_cdf():

    def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return(1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

    xs = [x/10 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x) for x in xs], '-', label='mu: 0, sigma: 1')
    plt.plot(xs, [normal_cdf(x, sigma=2)
             for x in xs], '--', label='mu: 0, sigma: 2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5)
             for x in xs], ':', label='mu: 0, sigma: 0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1)
             for x in xs], '-.', label='mu: -1, sigma: 1')
    plt.legend(loc=4)
    plt.title("Various normal cdfs")
    plt.show()


def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001
                       ) -> float:
    """findet eine Näherung für den inversen Wert durch binäre Suche"""
    
    def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return(1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

    #Wenn keine Standardverteilung vorliegt, skaliere zur SNV um
    if mu != 0 or sigma != 1:
        #Ist Z standardverteilt, so ist X = µ + Z*sigma normalverteilt
        return mu + sigma * inverse_normal_cdf(p, tolerance= tolerance)
    
    low_z = -10.0
    hi_z = 10.0
    while hi_z-low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        #print(hi_z, low_z, normal_cdf(mid_z))
        if(normal_cdf(mid_z)> p):
            hi_z = (hi_z+low_z)/2
        else:
            low_z = (hi_z+low_z)/2
 
    return( (hi_z+low_z) /2)

#print(inverse_normal_cdf(p=0.8))  


#plot_normal_cdf()
