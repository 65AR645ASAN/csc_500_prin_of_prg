def check_age_and_permissions(age, married):
    """
    Check if the user is above 25 and is married.
    Demonstrates short-circuiting with the 'and' operator.
    """
    if age >= 25 and married:
        return "Access Granted for Housing Loan"
    else:
        return "Access Denied for Housing Loan"


# Example usage - Function Calls:
print(check_age_and_permissions(20, True))  # Output: Access Denied

print(check_age_and_permissions(30, False))  # Output: Access Denied

print(check_age_and_permissions(30, True))  # Output: Access Granted


def find_first_true_value(values):
    """
    Find the first true value in the list using 'or' operator.
    Demonstrates short-circuiting with the 'or' operator.
    """
    for value in values:
        if value:
            return value
    return None


# Example usage:
values = [0, False, None, '', 'First True Value', 'Another Value']
print(find_first_true_value(values))  # Output: First True Value


# Example with any() and all()
def check_conditions(conditions):
    """
    Check multiple conditions using any() and all() with short-circuiting.
    """
    if all(conditions):
        return "All conditions are True"
    if any(conditions):
        return "At least one condition is True"
    return "No conditions are True"


# Example usage:
conditions = [True, False, True]
print(check_conditions(conditions))  # Output: At least one condition is True


# Potential issues with complexity
def complex_conditions_check(cond1, cond2, cond3, cond4):
    """
    A complex condition check to demonstrate potential complexity issues.
    """
    if (cond1 and (cond2 or cond3)) and not cond4:
        return "Complex Condition Met"
    else:
        return "Complex Condition Not Met"


# Example usage:
print(complex_conditions_check(True, False, True, False))  # Output: Complex Condition Met
print(complex_conditions_check(True, False, False, True))  # Output: Complex Condition Not Met

# Discussion
print("""
Short-circuiting is beneficial for:
1. Efficiency: Stops evaluating as soon as the result is determined.
2. Safety: Prevents evaluation of expressions that could raise exceptions if prior conditions fail.

However, it can lead to:
1. Complexity: Deeply nested conditions can become hard to read and maintain.
2. Hidden Bugs: If the short-circuiting behavior is not well-understood, it can cause unexpected results.

It's essential to balance the use of short-circuiting with code readability and maintainability.
""")

print('''
In this code:
check_age_and_permissions: Demonstrates short-circuiting with the and operator to ensure both conditions are met 
before granting access. find_first_true_value: Uses the or operator to find the first true value in a list, 
stopping evaluation as soon as a true value is found. check_conditions: Utilizes the any() and all() functions, 
which also support short-circuiting. complex_conditions_check: Shows how short-circuiting can lead to complex and 
hard-to-maintain code. This script highlights the practical applications of short-circuiting, its benefits, 
and the potential pitfalls to be aware of.
''')
