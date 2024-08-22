"""
Explanation of the Script:
can_enter_club Function: Uses the and operator to check if a person is eligible to enter a club based on their age and possession of ID.
should_take_umbrella Function: Uses the or operator to decide whether to take an umbrella based on weather conditions.
can_board_flight Function: Uses the and operator to determine if a passenger can board a flight based on ticket validity and baggage limit.
is_outside_acceptable_range Function: Uses the or operator to check if a number falls outside an acceptable range.
is_positive_and_even Function: Uses the and operator to check if a number is both positive and even.
Each function is tested with appropriate values, and the results are printed to the console.
"""


# Example using the 'and' operator

# Function to check if a person can enter a club
def can_enter_club(age, has_id):
    # Both conditions must be True for the person to enter
    if age >= 18 and has_id:
        return "Entry allowed"
    else:
        return "Entry denied"


# Test the 'and' example
age = 20
has_id = True
print(f"Age: {age}, Has ID: {has_id} -> {can_enter_club(age, has_id)}")


# Example using the 'or' operator

# Function to determine if you should take an umbrella
def should_take_umbrella(is_raining, is_snowing):
    # At least one condition must be True to take an umbrella
    if is_raining or is_snowing:
        return "Take umbrella"
    else:
        return "No umbrella needed"


# Test the 'or' example
is_raining = False
is_snowing = True
print(f"Is Raining: {is_raining}, Is Snowing: {is_snowing} -> {should_take_umbrella(is_raining, is_snowing)}")


# Additional Example with 'and' operator

# Function to check if a passenger can board a flight
def can_board_flight(has_valid_ticket, not_exceed_baggage_limit):
    # Both conditions must be True for the passenger to board
    if has_valid_ticket and not_exceed_baggage_limit:
        return "Boarding allowed"
    else:
        return "Boarding denied"


# Test the 'and' example
has_valid_ticket = True
not_exceed_baggage_limit = False
print(
    f"Has Valid Ticket: {has_valid_ticket}, Not Exceed Baggage Limit: {not_exceed_baggage_limit} -> {can_board_flight(has_valid_ticket, not_exceed_baggage_limit)}")


# Additional Example with 'or' operator

# Function to check if a number is outside the acceptable range
def is_outside_acceptable_range(number):
    # At least one condition must be True for the number to be outside the range
    if number < 0 or number > 100:
        return "The number is outside the acceptable range."
    else:
        return "The number is within the acceptable range."


# Test the 'or' example
number = 150
print(f"Number: {number} -> {is_outside_acceptable_range(number)}")


# Final Example with 'and' operator

# Function to check if a number is positive and even
def is_positive_and_even(number):
    # Both conditions must be True for the number to be positive and even
    if number > 0 and number % 2 == 0:
        return "The number is positive and even."
    else:
        return "The number does not meet the criteria."


# Test the 'and' example
number = 4
print(f"Number: {number} -> {is_positive_and_even(number)}")


def proceed_to_security_check():
    print("Proceed to security check.")


def go_back_to_counter():
    print("Go back to the counter.")


def scan_boarding_pass():
    print("Scan the boarding pass.")


def check_identification(valid_identification, valid_boarding_pass, identification_type, is_real_id=False):
    # First check using AND operator
    if valid_identification and valid_boarding_pass:
        proceed_to_security_check()
    else:
        go_back_to_counter()
        return

    # Second check using OR operator
    if identification_type == 'passport' or (identification_type == 'govt_issued_id' and is_real_id):
        scan_boarding_pass()
    else:
        go_back_to_counter()


# Example usage
valid_identification = True
valid_boarding_pass = True
identification_type = 'govt_issued_id'
is_real_id = True

check_identification(valid_identification, valid_boarding_pass, identification_type, is_real_id)
