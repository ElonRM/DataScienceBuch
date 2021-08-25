from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# Beschrifte jeden Punkt

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(
        label,
        # platziere die Beschriftungen an den Punkten
        xy=(friend_count, minute_count),
        xytext=(5, -5),  # Aber leicht verschoben
        textcoords='offset points'
    )

plt.title("Daily Minutes vs. Number of friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()


# Axes arent comparable
test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes aren't comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
# Mit folgendem Ausdruck werden die Achsen vergleichbar und man sieht, dass test 2 schlechter ausfällt
plt.axis("equal")
plt.show()
