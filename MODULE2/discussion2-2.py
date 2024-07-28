def demonstrate_and_short_circuit(x, y):
    """
    Demonstrates short-circuiting in 'and' expression.
    """
    print("AND Short-Circuiting:")
    result = x and y
    print(f"{x} and {y} => {result}")
    return result


def demonstrate_or_short_circuit(x, y):
    """
    Demonstrates short-circuiting in 'or' expression.
    """
    print("OR Short-Circuiting:")
    result = x or y
    print(f"{x} or {y} => {result}")
    return result


# Example usage:

# AND Short-Circuiting Examples
# When the first statement is true, Python evaluates the second statement.
# When the first statement is false, Python returns the first statement's value.
print(demonstrate_and_short_circuit(True, "Second value not evaluated"))
print(demonstrate_and_short_circuit(False, "Second value evaluated"))
print(demonstrate_and_short_circuit(True, False))
print(demonstrate_and_short_circuit(False, True))

# OR Short-Circuiting Examples
# When the first statement is true, Python returns the first statement's value.
# When the first statement is false, Python evaluates the second statement.
print(demonstrate_or_short_circuit(True, "Second value not evaluated"))
print(demonstrate_or_short_circuit(False, "Second value evaluated"))
print(demonstrate_or_short_circuit(False, True))
print(demonstrate_or_short_circuit(False, False))

# Explanation of "AND" and "OR" operator behavior
print("""
In the case of an 'and' expression, the Python interpreter first evaluates the first operand:
- If the first operand is 'False', Python returns that value without evaluating the second operand.
- If the first operand is 'True', Python evaluates the second operand and returns its value.

In the case of an 'or' expression, the Python interpreter first evaluates the first operand:
- If the first operand is 'True', Python returns that value without evaluating the second operand.
- If the first operand is 'False', Python evaluates the second operand and returns its value.

This 'laziness' in evaluation, known as 'short-circuiting', is common in many programming languages.
""")
