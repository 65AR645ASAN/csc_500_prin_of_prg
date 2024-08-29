def swap_values(user_val1, user_val2):
    """Swaps the two input values and returns them."""
    return user_val2, user_val1


if __name__ == "__main__":
    # Read two integer inputs from the user
    user_val1 = int(input())
    user_val2 = int(input())

    # Call the swap_values function to get the swapped values
    swapped_val1, swapped_val2 = swap_values(user_val1, user_val2)

    # Print the swapped values
    print(swapped_val1, swapped_val2)
