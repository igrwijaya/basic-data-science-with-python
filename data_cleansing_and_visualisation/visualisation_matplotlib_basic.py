import matplotlib.pyplot as plt
import numpy as np

# LINE CHART
plt.plot([1,2,3,4],[1,4,9,16])
plt.title("First Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()

# BAR CHART
divisions = ["Div A", "Div B", "Div C", "Div D", "Div E"]
div_avg_marks = [70, 82, 73, 65, 68]

plt.bar(divisions, div_avg_marks, color="red")
plt.title("Bar Graph")
plt.xlabel("Division")
plt.ylabel("Marks")
plt.show()

# PIE CHART
firms = ["Firm A", "Firm B", "Firm C", "Firm D", "Firm E"]
shares = [70, 82, 73, 65, 68]
explode = [0, 0.1, 0, 0, 0]

plt.pie(shares, explode=explode, labels=firms, shadow=True, startangle=45)
plt.axis("equal")
plt.legend(title="Here Legend Tittle")
plt.show()

# HISTOGRAM
x = np.random.random_integers(1, 500, 1000)
print(x)

plt.title("Histogram")
plt.xlabel("Random Data")
plt.ylabel("Frequency")
plt.hist(x,10, color="red")
plt.show()

# SCATTER PLOT
rndHeight = np.random.randint(50, 200, 20)
rndWeight = np.random.randint(50, 90, 20)

height = np.array(rndHeight)
weight = np.array(rndWeight)

plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height, weight)
plt.title("Scatter")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()