# Simple line plot


# Import the pyplot module
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a simple plot
plt.plot(x, y) # This is the line that creates the plot of x and y
# plt.show() # This is the line that shows the plot
plt.savefig('results/simple_line.png')

# Add labels and title to the plot

plt.plot(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Simple Line Plot')

# To save the plot as an image file, you can use the savefig() function
# in the result folder
plt.savefig('results/simple_line_with_labels.png')
