"""

Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats)
 as input, and output the gas cost for 10 miles, 50 miles, and 400 miles.

Output each floating-point value with two digits after the decimal point, which can be
achieved as follows:
print('{:.2f}'.format(your_value))

"""


def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    """Calculates the cost of driving the given number of miles."""
    return (driven_miles / miles_per_gallon) * dollars_per_gallon


if __name__ == "__main__":
    # Read inputs
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    # Calculate costs for different mileages
    cost_10_miles = driving_cost(10, miles_per_gallon, dollars_per_gallon)
    cost_50_miles = driving_cost(50, miles_per_gallon, dollars_per_gallon)
    cost_400_miles = driving_cost(400, miles_per_gallon, dollars_per_gallon)

    # Print costs formatted to two decimal places
    print('{:.2f}'.format(cost_10_miles))
    print('{:.2f}'.format(cost_50_miles))
    print('{:.2f}'.format(cost_400_miles))
