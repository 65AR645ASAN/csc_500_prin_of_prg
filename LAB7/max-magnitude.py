"""
Write a function max_magnitude() with two integer input parameters that returns the largest magnitude value.
Use the function in a program that takes two integer inputs, and outputs the largest magnitude value.
"""

one_input, two_input = input().split()


def max_magnitude():
    if one_input > two_input:
        print(one_input)
    else:
        print(two_input)


if __name__ == "__main__":
    max_magnitude()
