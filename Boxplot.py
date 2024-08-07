import matplotlib.pyplot as plt
import random

data = [random.gauss(0, 1 ) for _ in range(100)]
outliers = [-10, 10]

plt.clf()
plt.boxplot(data + outliers, vert=False, patch_artist=True)
plt.title("Boxplot example with outliers")
plt.xlabel("Values")
plt.xticks(range(-15, 16, 5))
plt.savefig("./boxplot.png")
plt.show()