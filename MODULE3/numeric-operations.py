class NumericOperations:
    """Class to demonstrate the use of numeric data types and operators in Python."""

    def basic_arithmetic(self, a, b):
        """
        Perform basic arithmetic operations.

        Args:
        a (int, float): First number.
        b (int, float): Second number.

        Returns:
        dict: A dictionary containing results of addition, subtraction, multiplication, and division.
        """
        operations = {
            'addition': a + b,
            'subtraction': a - b,
            'multiplication': a * b,
            'division': a / b if b != 0 else 'Undefined'
        }
        return operations

    def modulus_exponentiation(self, a, b):
        """
        Calculate the modulus and exponentiation of two numbers.

        Args:
        a (int, float): Base number.
        b (int, float): Exponent number.

        Returns:
        dict: A dictionary containing results of modulus and exponentiation.
        """
        results = {
            'modulus': a % b if b != 0 else 'Undefined',
            'exponentiation': a ** b
        }
        return results

    def type_conversions(self, a):
        """
        Demonstrate type conversions between numeric types.

        Args:
        a (int, float): Number to be converted.

        Returns:
        dict: A dictionary containing conversions to integer, float, and complex.
        """
        conversions = {
            'to_integer': int(a),
            'to_float': float(a),
            'to_complex': complex(a)
        }
        return conversions


# Example usage:
numeric_ops = NumericOperations()
print("Basic Arithmetic Operations:")
print(numeric_ops.basic_arithmetic(10, 5))

print("\nModulus and Exponentiation:")
print(numeric_ops.modulus_exponentiation(10, 3))

print("\nType Conversions:")
print(numeric_ops.type_conversions(10.5))
