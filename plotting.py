import matplotlib
# Import the pyplot module
import matplotlib.pyplot as plt

# Check the version of Matplotlib
print('Matplotlib version:', matplotlib.__version__)

# Check the backend of Matplotlib
print('Matplotlib backend:', matplotlib.get_backend())

# Set a different backend
matplotlib.use('TkAgg')  # Example for TkAgg backend

# Check the new backend of Matplotlib
print('Matplotlib backend:', matplotlib.get_backend())


# Create a simple plot
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.show()

# Create a scatter plot
plt.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.show()

# Create a bar plot
plt.bar([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.show()

# Create a histogram
plt.hist([1, 2, 3, 4, 5])
plt.show()

# Create a pie chart
plt.pie([1, 2, 3, 4, 5])
plt.show()

# Create a box plot
plt.boxplot([1, 2, 3, 4, 5])
plt.show()

# Create a violin plot
plt.violinplot([1, 2, 3, 4, 5])
plt.show()

# Create a heatmap
plt.imshow([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
plt.colorbar()
plt.show()
