def short_circuit_and(condition1, condition2):
    """
    Demonstrates short-circuiting with the 'and' operator.
    """
    if condition1 and condition2:
        return "Both conditions are True"
    else:
        return "At least one condition is False"

def short_circuit_or(condition1, condition2):
    """
    Demonstrates short-circuiting with the 'or' operator.
    """
    if condition1 or condition2:
        return "At least one condition is True"
    else:
        return "Both conditions are False"

# Example usage
print(short_circuit_and(False, True))  # Output: "At least one condition is False"
print(short_circuit_or(True, False))   # Output: "At least one condition is True"
