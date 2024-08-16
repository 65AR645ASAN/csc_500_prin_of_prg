# Copy this line - Beginning of Program

# Part 1: Mean Rainfall Calculation

years = int(input("Years to Break Up into Months: "))

cumulative_rainfall_in_inches_ = 0
cumulative_months = 0

for year in range(1, years + 1):
    print(f"Year >>> {year}:")

    for month in range(1, 13):
        rainfall = float(input(f"Inches of Rain per month >>> {month}: "))

        cumulative_rainfall_in_inches_ += rainfall

    cumulative_months += 12

# Calculate the Mean rainfall
Mean_rainfall = cumulative_rainfall_in_inches_ / cumulative_months

print(f"\nCumulative Number of months: {cumulative_months}")
print(f"Cumulative inches of rainfall: {cumulative_rainfall_in_inches_:.2f}")
print(f"Mean rainfall per month: {Mean_rainfall:.2f} inches")

# Part 2: Bookstore Points Calculation

number_of_books_procured = int(input("How Many Books are Procured This Month: "))

if number_of_books_procured == 0:
    numeral_of_points_earned = 0
elif number_of_books_procured == 2:
    numeral_of_points_earned = 5
elif number_of_books_procured == 4:
    numeral_of_points_earned = 15
elif number_of_books_procured == 6:
    numeral_of_points_earned = 30
elif number_of_books_procured >= 8:
    numeral_of_points_earned = 60
else:
    numeral_of_points_earned = 0

print(f"Total Amount of Points Awarded: {numeral_of_points_earned}")
# Copy this line - End of Program
