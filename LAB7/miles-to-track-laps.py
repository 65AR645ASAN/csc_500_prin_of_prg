'''
One lap around a standard high-school running track is exactly 0.25 miles.
Write the function miles_to_laps() that takes a number of miles as an
argument and returns
the number of laps.

Complete the program to output the number of laps.

Output each floating-point value with two digits after the decimal point,
which can be achieved as follows:

print('{:.2f}'.format(your_value))

 '''

single_lap = 0.25


def miles_to_laps(num_of_miles):
    total_num_of_miles = float(num_of_miles)
    num_of_laps = total_num_of_miles / single_lap
    print('{:.2f}'.format(num_of_laps))
    return num_of_laps


if __name__ == '__main__':
    num_of_miles = input()
    miles_to_laps(num_of_miles)
