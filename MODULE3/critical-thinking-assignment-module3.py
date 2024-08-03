# Copy this line - Beggining of Program
# PART 1
def calculate_meal_total():
    """
        Calculates the total amount of a meal with an 18% tip and 7% sales tax.
        """
    # Get the charge for the food from the user
    charge_for_food = float(input("Enter the charge for the food: $"))

    # Calculate the tip (18%)
    tip = charge_for_food * 0.18

    # Calculate the sales tax (7%)
    sales_tax = charge_for_food * 0.07

    # Calculate the total amount
    total_amount = charge_for_food + tip + sales_tax

    # Display the amounts
    print(f"Charge for the food: ${charge_for_food:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales tax (7%): ${sales_tax:.2f}")
    print(f"Total amount: ${total_amount:.2f}")


# PART 2
def calculate_alarm_time():
    """
    Calculates the time when an alarm will go off given the current time and a wait time in hours.
    """
    # Get the current time in hours from the user (24-hour format)
    current_time = int(input("Enter the current time (in 24-hour format): "))

    # Get the number of hours to wait for the alarm
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the time when the alarm will go off
    alarm_time = (current_time + hours_to_wait) % 24

    # Display the alarm time
    print(f"The alarm will go off at: {alarm_time:02d}:00")


def main():
    """
    Main function to run the meal total calculation and alarm time calculation.
    """
    # PART 1
    print("Meal Total Calculator")
    calculate_meal_total()
    # PART 2
    print("\nAlarm Time Calculator")
    calculate_alarm_time()


# Call the main function
# RUN ENTIRE PROGRAM
if __name__ == "__main__":
    main()

# Copy this line - End of Program
