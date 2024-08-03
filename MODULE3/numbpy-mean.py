import numpy as np


"""
Method Utilizing an Array Data Structure: numpy.mean() In Python, the NumPy library provides an array data structure 
called ndarray that offers numerous functionalities, including mathematical and statistical operations. One commonly 
used method that utilizes an array data structure is numpy.mean(), which calculates the mean (average) of the 
elements in an array. Here's an example demonstrating the use of numpy.mean():
"""
class ArrayStatistics:
    """Class to demonstrate statistical operations on arrays using NumPy."""

    def calculate_mean(self, data):
        """
        Calculate the mean of a NumPy array.

        Args:
        data (np.ndarray): NumPy array of numerical data.

        Returns:
        float: The mean of the array elements.
        """
        return np.mean(data)


# Example usage:
data = np.array([1, 2, 3, 4, 5])
array_stats = ArrayStatistics()
mean_value = array_stats.calculate_mean(data)
print(f"Mean of the array: {mean_value}")
