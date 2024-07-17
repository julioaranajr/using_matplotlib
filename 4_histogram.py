# Histograms

from matplotlib import pyplot as plt

# Create a histogram with labels
plt.hist([1, 2, 3, 4, 5], bins=[0, 1, 2, 3, 4, 5], edgecolor='black')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Histogram Title')

# Save the histogram to a file
plt.savefig('results/histogram.png')
