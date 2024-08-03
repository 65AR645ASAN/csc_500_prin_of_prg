import numpy as np
import array


class ArrayExamples:
    """Class to demonstrate various array operations using NumPy and Python array module."""

    def display_numpy_array(self):
        """Create and display a 3x4 NumPy array."""
        numpy_array = np.arange(12).reshape(2, 6)
        print("Original NumPy Array:\n", numpy_array)
        print("Iterating over the NumPy array:")
        for element in np.nditer(numpy_array):
            print(element, end=" ")
        print()

    def create_1d_array(self):
        """Create and display a 1D NumPy array."""
        array_1d = np.array([1, 2, 3, 4, 5])
        print("1D NumPy Array:", array_1d)

    def create_2d_array(self):
        """Create and display a 2D NumPy array."""
        array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("2D NumPy Array:\n", array_2d)

    def array_with_zeros(self):
        """Create and display a NumPy array filled with zeros."""
        zeros_array = np.zeros((3, 3))
        print("NumPy Array with zeros:\n", zeros_array)

    def array_with_ones(self):
        """Create and display a NumPy array filled with ones."""
        ones_array = np.ones((2, 4))
        print("NumPy Array with ones:\n", ones_array)

    def array_with_range(self):
        """Create and display a NumPy array with a range of numbers."""
        range_array = np.arange(0, 10, 2)
        print("NumPy Array with a range of numbers:", range_array)

    def array_with_random(self):
        """Create and display a NumPy array with random numbers."""
        random_array = np.random.rand(3, 3)
        print("NumPy Array with random numbers:\n", random_array)

    def array_module_example(self):
        """Create and modify an array using the Python array module."""
        int_array = array.array('i', [1, 2, 3, 4, 5])
        int_array[1] = 10
        print("Array module array:", int_array)

    def list_manipulation(self):
        """Perform operations on lists and display the results."""
        grades = [85, 92, 78, 90, 88, 76]
        average_grade = sum(grades) / len(grades)
        print("Average grade:", average_grade)

        inventory = [20, 50, 15, 30, 10]
        inventory[2] -= 5
        print("Updated inventory:", inventory)

        temperatures = [30.5, 32.0, 31.5, 29.8, 30.2, 31.0, 30.9]
        max_temp = max(temperatures)
        print("Highest temperature recorded:", max_temp)

        students = ['alex', 'bill', 'catherine', 'andy', 'molly', 'rose']
        capitalized_students = [student.capitalize() for student in students]
        print("Capitalized student names:", capitalized_students)

    def list_access(self):
        """Demonstrate accessing elements in a list."""
        List = ["Tutorialspoint", "is", "the", "best", "platform", "to", "learn", "new", "skills"]
        print(List)
        print("Accessing element from the list")
        print(List[0])
        print(List[3])
        print("Accessing element from the list by using negative indexing")
        print(List[-2])
        print(List[-3])

    def string_example(self):
        """Demonstrate accessing characters in a string."""
        String = "Tutorialspoint is the best platform to learn new skills"
        print(String)
        print(type(String))
        print("Accessing characters of a string:")
        print(String[6])
        print(String[10])
        print("Accessing characters of a string by using negative indexing")
        print(String[-6])
        print(String[-21])

    def tuple_example(self):
        """Demonstrate accessing elements in a tuple."""
        tuple_example = ('Tutorialspoint', 'is', 'the', 'best', 'platform', 'to', 'learn', 'new', 'skills')
        print(tuple_example)
        print("Accessing elements of the tuple:")
        print(tuple_example[5])
        print(tuple_example[2])
        print("Accessing elements of the tuple by negative indexing: ")
        print(tuple_example[-6])
        print(tuple_example[-1])

    def list_with_while_loop(self):
        """Demonstrate appending and accessing elements in a list using a while loop."""
        number = []
        i = 0

        while i < 10:
            number.append(i + 100)
            i += 1

        i = 0
        while i < 10:
            print("number[", i, "] = ", number[i])
            i += 1


if __name__ == "__main__":
    array_examples = ArrayExamples()
    array_examples.display_numpy_array()
    array_examples.create_1d_array()
    array_examples.create_2d_array()
    array_examples.array_with_zeros()
    array_examples.array_with_ones()
    array_examples.array_with_range()
    array_examples.array_with_random()
    array_examples.array_module_example()
    array_examples.list_manipulation()
    array_examples.list_access()
    array_examples.string_example()
    array_examples.tuple_example()
    array_examples.list_with_while_loop()
