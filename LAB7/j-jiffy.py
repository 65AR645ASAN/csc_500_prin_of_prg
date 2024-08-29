def seconds_to_jiffies(user_seconds):
    """Converts seconds to the number of jiffies."""
    jiffies = user_seconds * 100
    return jiffies


if __name__ == "__main__":
    # Read the number of seconds from input
    user_seconds = float(input())

    # Call the seconds_to_jiffies function and store the result
    jiffies = seconds_to_jiffies(user_seconds)

    # Output the result formatted to two decimal places
    print('{:.2f}'.format(jiffies))
