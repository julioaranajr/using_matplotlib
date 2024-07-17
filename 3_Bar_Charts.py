import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']

# Data for the first bar chart
values1 = [10, 20, 30, 40]

# Data for the second bar chart
values2 = [20, 30, 40, 50]

# Data for the third bar chart
values3 = [30, 40, 50, 60]

# Data for the fourth bar chart
values4 = [40, 50, 60, 70]

# Data for the fifth bar chart
values5 = [50, 60, 70, 80]

# Data for the sixth bar chart
values6 = [60, 70, 80, 90]

# Data for the seventh bar chart
values7 = [70, 80, 90, 100]

# Data for the eighth bar chart
values8 = [80, 90, 100, 110]

plt.bar(labels, values1, color='red', label='First')
plt.bar(labels, values2, color='blue', label='Second', bottom=values1)
plt.bar(labels, values3, color='green', label='Third', bottom=values2)
plt.bar(labels, values4, color='yellow', label='Fourth', bottom=values3)
plt.bar(labels, values5, color='purple', label='Fifth', bottom=values4)
plt.bar(labels, values6, color='orange', label='Sixth', bottom=values5)
plt.bar(labels, values7, color='brown', label='Seventh', bottom=values6)
plt.bar(labels, values8, color='pink', label='Eighth', bottom=values7)

plt.legend()
plt.show()

# Save the plot
plt.savefig('results/3_Bar_Charts.png')