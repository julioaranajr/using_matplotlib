# What is Matplotlib?

- Matplotlib is a comprehensive 2D plotting library for the Python programming language.
- It is widely used for creating static, animated and interactive visualizations in Python.
- Matplotlib was developed by John D. Hunter and is now maintained by a huge team of developers.
- It is open-source and freely available for use under the BSD license.

## To install matplotlib type the following command in the terminal

```bash
pip install matplotlib
```

## to Check the version of Matplotlib:

```python
print('Matplotlib version:', matplotlib.__version__)
```

## Matplotlib Backends

Matplotlib can use different backends for rendering plots. 
The default might not be the best for your needs.
To check the current backend, use the following code:

```python
print('Matplotlib backend:', matplotlib.get_backend())
```

## Check the backend of Matplotlib

to check the current backend, use the following code:

```python
print('Matplotlib backend:', matplotlib.get_backend())
```

## To set a different backend

You can set a different backend using the following code:

```python
import matplotlib matplotlib.use('TkAgg') # Example for TkAgg backend
```

### Common backends include

The most common backends include:

- TkAgg (default for Python’s Tkinter)
- Qt5Agg (for Qt5)
- Agg (for PNG and other file formats, no interactive window)

## Set a different backend

You can set a different backend using the following code:

```python
matplotlib.use('TkAgg')  # Example for TkAgg backend
```

## Check the new backend of Matplotlib

to check the new backend, use the following code:

```python
print('Matplotlib backend:', matplotlib.get_backend())
```

## The Matplotlib Interface

Matplotlib has two interfaces:

- MATLAB-style interface (stateful)
- Object-oriented interface (stateless)

> The object-oriented interface is recommended for more control and customization.

## Import the pyplot module

The most common way to use Matplotlib is through the pyplot module.
You can import it using the following code:

```python
import matplotlib.pyplot as plt

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

```

## Additional dependencies

Matplotlib can be used with other libraries like NumPy, SciPy, and Pillow to enhance its capabilities.

### NumPy

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

### SciPy

SciPy is a free and open-source library for the Python programming language that adds support for scientific and technical computing. It builds on the capabilities of NumPy and provides a large number of higher-level functions that operate on NumPy arrays and are useful for different types of scientific and engineering applications.

### Pillow (PIL)

Pillow is a free and open-source library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. It is a fork of the Python Imaging Library (PIL) and provides a more up-to-date and actively maintained version of the library.

## Conclusion

Matplotlib is a powerful library for creating visualizations in Python. It is widely used for creating static, animated, and interactive plots. It has a MATLAB-style interface and an object-oriented interface. It can be used with other libraries like NumPy, SciPy, and Pillow to enhance its capabilities.

# References

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [DevOpsSchool](https://www.devopsschool.com/blog/what-is-matplotlib-and-use-cases-of-matplotlib/#:~:text=Matplotlib%20is%20a%20comprehensive%202D,a%20huge%20team%20of%20developers.)
