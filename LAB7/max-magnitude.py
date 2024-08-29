"""
Write a function max_magnitude() with two integer input parameters that returns the largest magnitude value.
Use the function in a program that takes two integer inputs, and outputs the largest magnitude value.
"""


def max_magnitude(user_val1, user_val2):
    """Returns the integer with the largest magnitude (absolute value)"""
    if abs(user_val1) > abs(user_val2):
        return user_val1
    else:
        return user_val2


if __name__ == "__main__":
    # Read inputs
    user_val1 = int(input())
    user_val2 = int(input())

    # Get the number with the largest magnitude
    result = max_magnitude(user_val1, user_val2)

    # Output the result
    print(result)
