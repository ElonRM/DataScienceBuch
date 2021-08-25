from matplotlib import pyplot as plt
from collections import Counter


plots = ["movies", "grades", "mentions"]
# Funktioniert nicht wirklich...
selected_plot = plots[2]
#grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

x_values = {
    "movies": ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"],
    "grades": [x + 5 for x in Counter(min((grade) // 10 * 10, 90) for grade in [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]).keys()],
    "mentions": [2017, 2018],
}

y_values = {
    "movies": [5, 11, 3, 8, 10],
    "grades": Counter(min((grade) // 10 * 10, 90) for grade in [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]).values(),
    "mentions": [500, 505],
}

x_labels = {
    "movies": None,
    "grades": "Decile",
    "mentions": None,
}

y_labels = {
    "movies": "# of Academy Awards",
    "grades": "# of students",
    "mentions": "# of times I heard someone say 'data science'",
}

axis_ranges = {
    "movies": None,
    "grades": [-5, 105, 0, max(y_values["grades"])+1],
    "mentions": [min(x_values["mentions"])-0.5, max(x_values["mentions"])+0.5, 0, max(y_values["mentions"])+50],
}

x_ticks = {
    "movies": [range(len(x_values["movies"])), x_values["movies"]],
    "grades": [10 * i for i in range(11)],
    "mentions": x_values["mentions"],
}
y_ticks = {
    "movies": None,
    "grades": None,
    "mentions": [100 * i for i in range((max(y_values["mentions"])//100)+1)],
}

bar_width = {
    "movies": [False],
    "grades": [True, 10],
    "mentions": [False],
}

edge_color = {
    "movies": None,
    "grades": (0, 0, 0),
    "mentions": None,
}

titles = {
    "movies": "My Favorite Movies",
    "grades": "Distribution of Exam 1 grades",
    "mentions": "Not so huge anymore",
}


plt.bar(x_values[selected_plot],
        # gibt jedem Balken die korrekte Höhe (Anzahö, wie oft die Note vorkam)
        y_values[selected_plot],
        # bar_width[selected_plot][1] if bar_width[selected_plot][0] == True else pass,
        edgecolor=edge_color[selected_plot]
        )

plt.xticks(x_ticks[selected_plot])
plt.yticks(y_ticks[selected_plot])
plt.axis(axis_ranges[selected_plot])
plt.xlabel(x_labels[selected_plot])
plt.ylabel(y_labels[selected_plot])
plt.title(titles[selected_plot])
plt.show()
