import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
import math

num_friends = np.random.binomial(100, 0.08, 204)
friends_counter = Counter(num_friends)
plt.bar(friends_counter.keys(), friends_counter.values(), edgecolor=(0, 0, 0))
#plt.xticks([20*i for i in range(6)])
#plt.yticks([i*5 for i in range(math.ceil(max(friends_counter.values())//5+2))])
plt.axis([0, 101, 0, max(friends_counter.values())+1])
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.title("Histogram of friends count")
plt.show()
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
largest_value = sorted_values[-1]
second_largest_number = sorted_values[-2]
