# Copy this line - Beginning of Program
# PART 1
def calculate_meal_total():
    """
        Calculates the total amount of a meal with an 18% tip and 7% sales tax.
        """
    charge_for_food = float(input("food charge: $"))
    tip = charge_for_food * 0.18
    sales_tax = charge_for_food * 0.07
    total_amount = charge_for_food + tip + sales_tax

    print(f"Charge for the food: ${charge_for_food:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales tax (7%): ${sales_tax:.2f}")
    print(f"Total amount: ${total_amount:.2f}")


# PART 2
def calculate_alarm_time():
    """
    Calculates when an alarm will go off given the current time and a wait time in hours.
    """
    current_time = int(input("Enter current time (in 24-hour format): "))
    hours_to_wait = int(input("Enter number of hours to wait for the alarm: "))
    alarm_time = (current_time + hours_to_wait) % 24
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
