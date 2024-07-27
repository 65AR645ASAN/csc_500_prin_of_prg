def check_age_and_permissions(age, has_permission):
    """
    Check if the user is above 18 and has permission.
    Demonstrates short-circuiting with the 'and' operator.
    """
    if age >= 18 and has_permission:
        return "Access Granted"
    else:
        return "Access Denied"


# Example usage - Function Calls:
print(check_age_and_permissions(20, True))  # Output: Access Granted
print(check_age_and_permissions(15, True))  # Output: Access Denied
print(check_age_and_permissions(20, False))  # Output: Access Denied


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
