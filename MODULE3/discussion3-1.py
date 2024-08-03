import numpy as np
import array

# Create a 3x4 array using the arange() function (NumPy array)
numpy_array = np.arange(12).reshape(2, 6)
print("Original NumPy Array:\n", numpy_array)

# Iterate over the NumPy array using nditer
print("Iterating over the NumPy array:")
for element in np.nditer(numpy_array):
    print(element, end=" ")
print()

# Creating a 1D NumPy array (vector)
array_1d = np.array([1, 2, 3, 4, 5])
print("1D NumPy Array:", array_1d)

# Creating a 2D NumPy array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D NumPy Array:\n", array_2d)

# Creating a NumPy array with zeros
zeros_array = np.zeros((3, 3))
print("NumPy Array with zeros:\n", zeros_array)

# Creating a NumPy array with ones
ones_array = np.ones((2, 4))
print("NumPy Array with ones:\n", ones_array)

# Creating a NumPy array with a range of numbers
range_array = np.arange(0, 10, 2)  # start, stop, step
print("NumPy Array with a range of numbers:", range_array)

# Creating a NumPy array with random numbers
random_array = np.random.rand(3, 3)
print("NumPy Array with random numbers:\n", random_array)

# Creating an array of integers using the array module
int_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing and modifying elements in the array module array
int_array[1] = 10
print("Array module array:", int_array)  # Output: array('i', [1, 10, 3, 4, 5])

grades = [85, 92, 78, 90, 88, 76]
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

inventory = [20, 50, 15, 30, 10]  # Quantities of different items
inventory[2] -= 5  # Sold 5 units of the third item
print("Updated inventory:", inventory)

temperatures = [30.5, 32.0, 31.5, 29.8, 30.2, 31.0, 30.9]
max_temp = max(temperatures)
print("Highest temperature recorded:", max_temp)

students = ['alex', 'bill', 'catherine', 'andy', 'molly', 'rose']
capitalized_students = [student.capitalize() for student in students]
print("Capitalized student names:", capitalized_students)

List = ["Tutorialspoint", "is", "the", "best", "platform", "to", "learn", "new", "skills"]
print(List)
print("Accessing element from the list")
print(List[0])
print(List[3])
print("Accessing element from the list by using negative indexing")
print(List[-2])
print(List[-3])

String = "Tutorialspoint is the best platform to learn new skills"
print(String)
print(type(String))
print("Accessing characters of a string:")
print(String[6])
print(String[10])
print("Accessing characters of a string by using negative indexing")
print(String[-6])
print(String[-21])

tuple = ('Tutorialspoint', 'is', 'the', 'best', 'platform', 'to', 'learn', 'new', 'skills')
print(tuple)
print("Accessing elements of the tuple:")
print(tuple[5])
print(tuple[2])
print("Accessing elements of the tuple by negative indexing: ")
print(tuple[-6])
print(tuple[-1])

# Following defines an empty list.
number = []
i = 0

while i < 10:
    # Appending elements in the list
    number.append(i + 100)
    i = i + 1

i = 0
while i < 10:
    # Accessing elements from the list
    print("number[", i, "] = ", number[i])
    i = i + 1
