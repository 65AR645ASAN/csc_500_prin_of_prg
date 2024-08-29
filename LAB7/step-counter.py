def feet_to_steps(user_feet):
    """Converts feet to the number of steps."""
    steps = user_feet / 2.5
    return int(steps)


if __name__ == "__main__":
    # Read the number of feet walked from input
    user_feet = float(input())

    # Call the feet_to_steps function and print the result
    steps_walked = feet_to_steps(user_feet)
    print(steps_walked)
