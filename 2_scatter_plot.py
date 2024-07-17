# Create a scatter plot and save it as a PNG file
import matplotlib
# Import the pyplot module
import matplotlib.pyplot as plt

# Create a scatter plot
plt.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
# Save the plot as a PNG file
plt.savefig('results/scatter_plot.png')
