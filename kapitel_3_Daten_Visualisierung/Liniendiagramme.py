from matplotlib import pyplot as plt

variance = [2**n for n in range(9)]
bias_squared = [2**(8-n) for n in range(9)]
total_error = [x+y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]  # erzeugt die späteren x-Werte (1,2.)

# Wir können plt.plot mehrmals aufrufen um mehrere
# Datenreihen in einem Diagramm darzustellen
plt.plot(xs, variance,      "g-", label="variance")
plt.plot(xs, bias_squared,  "r-", label="bias^2")
plt.plot(xs, total_error,   "b-", label="total error")

# Weil wir jeder Datenreihe ein Label zugewiesen haben,
# bekommen wir die Legende frei Haus
# loc = 9 bedeutet "oben mittig"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()
