# Copy this line - Beginning of Program
# PART 1
def calculate_meal_total():
    food_cost = float(input("food charge: $"))
    tip = food_cost * 0.18
    sales_tax = food_cost * 0.07
    total_amount = food_cost + tip + sales_tax

    print(f"Cost of the food: ${food_cost:.2f}")
    print(f"Tip 18%: ${tip:.2f}")
    print(f"Sales tax 7%: ${sales_tax:.2f}")
    print(f"Total amount: ${total_amount:.2f}")


# PART 2
def calculate_alarm_time():
    current_time = int(input("Enter current time (in 24-hour format): "))
    wait_time = int(input("Enter count of hours for the alarm: "))
    alarm_time = (current_time + wait_time) % 24
    print(f"The alarm is set to go off at: {alarm_time:02d}:00")


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
