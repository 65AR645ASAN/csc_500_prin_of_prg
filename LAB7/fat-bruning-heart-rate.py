def get_age():
    """Gets the age input from the user and checks if it's within the valid range."""
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    """Calculates the fat-burning heart rate for a given age."""
    max_heart_rate = 220 - age
    fat_burn_rate = 0.7 * max_heart_rate
    return fat_burn_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as ve:
        print(ve)
        print("Could not calculate heart rate info.")
