def is_leap_year(user_year):
    """Determines if a given year is a leap year."""
    # Check if the year is divisible by 4
    if user_year % 4 == 0:
        # If it is a century year, check if it is divisible by 400
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    # Read the year from input
    user_year = int(input())

    # Determine if the year is a leap year using the is_leap_year function
    if is_leap_year(user_year):
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
