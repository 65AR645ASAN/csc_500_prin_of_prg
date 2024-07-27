def short_circuit_and(condition1, condition2):
    """
    Demonstrates short-circuiting with the 'and' operator.
    """
    if condition1 and condition2:
        return "Both conditions are True"
    else:
        return "At least one condition is False"

print(short_circuit_and(False, True))  
print(short_circuit_and(True, True))  
