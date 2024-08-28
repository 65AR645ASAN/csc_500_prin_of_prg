# Python Functions Demonstrating Different Exception Types

"""
Great! It looks like all exceptions were successfully triggered and handled as expected. The output confirms that each specific exception type has been demonstrated with a corresponding error message.

Here's a quick summary of what each function does and the output it generates:

1. trigger_arithmetic_error(): Triggers an `ArithmeticError` by dividing by zero.
   - Output: `ArithmeticError occurred: division by zero`

2. trigger_attribute_error(): Triggers an `AttributeError` by attempting to call a method on `None`.
   - Output: `AttributeError occurred: 'NoneType' object has no attribute 'some_method'`

3. trigger_import_error(): Triggers an `ImportError` by attempting to import a non-existent module.
   - Output: `ImportError occurred: No module named 'non_existent_module'`

4. trigger_index_error(): Triggers an `IndexError` by accessing an out-of-bounds index in a list.
   - Output: `IndexError occurred: list index out of range`

5. trigger_io_error(): Triggers an `IOError` by trying to open a non-existent file.
   - Output: `IOError occurred: [Errno 2] No such file or directory: 'non_existent_file.txt'`

6. trigger_key_error(): Triggers a `KeyError` by accessing a non-existent key in a dictionary.
   - Output: `KeyError occurred: 'b'`

7. trigger_recursion_error(): Triggers a `RecursionError` by causing infinite recursion.
   - Output: `RecursionError occurred: maximum recursion depth exceeded`

8. trigger_runtime_error(): Triggers a `RuntimeError` by manually raising it.
   - Output: `RuntimeError occurred: This is a runtime error`

9. trigger_syntax_error(): Triggers a `SyntaxError` by executing invalid Python syntax.
   - Output: `SyntaxError occurred: invalid syntax (<string>, line 1)`

10. trigger_system_error(): Triggers a `SystemError` by manually raising it.
    - Output: `SystemError occurred: This is a system error`

11. trigger_type_error(): Triggers a `TypeError` by attempting to add a string to an integer.
    - Output: `TypeError occurred: can only concatenate str (not "int") to str`

12. trigger_value_error(): Triggers a `ValueError` by attempting to convert a non-integer string to an integer.
    - Output: `ValueError occurred: invalid literal for int() with base 10: 'invalid_int'`

The code finished with an exit code of 0, indicating that all functions executed successfully and the exceptions were properly handled.

Feel free to use this script as a reference for understanding Python exceptions and their handling!
"""


def trigger_arithmetic_error():
    try:
        result = 1 / 0  # Division by zero
    except ArithmeticError as e:
        print(f"ArithmeticError occurred: {e}")


def trigger_attribute_error():
    try:
        None.some_method()  # Attempt to access a method on a NoneType
    except AttributeError as e:
        print(f"AttributeError occurred: {e}")


def trigger_import_error():
    try:
        import non_existent_module  # Attempt to import a non-existent module
    except ImportError as e:
        print(f"ImportError occurred: {e}")


def trigger_index_error():
    try:
        lst = [1, 2, 3]
        print(lst[5])  # Accessing an out-of-bounds index
    except IndexError as e:
        print(f"IndexError occurred: {e}")


def trigger_io_error():
    try:
        with open('non_existent_file.txt', 'r') as file:
            file.read()  # Attempting to read a non-existent file
    except IOError as e:
        print(f"IOError occurred: {e}")


def trigger_key_error():
    try:
        d = {'a': 1}
        print(d['b'])  # Accessing a non-existent key
    except KeyError as e:
        print(f"KeyError occurred: {e}")


def trigger_recursion_error():
    try:
        def recursive_function():
            return recursive_function()  # Infinite recursion

        recursive_function()
    except RecursionError as e:
        print(f"RecursionError occurred: {e}")


def trigger_runtime_error():
    try:
        raise RuntimeError('This is a runtime error')  # Manually raising a RuntimeError
    except RuntimeError as e:
        print(f"RuntimeError occurred: {e}")


def trigger_syntax_error():
    try:
        exec('x === 1')  # Invalid syntax
    except SyntaxError as e:
        print(f"SyntaxError occurred: {e}")


def trigger_system_error():
    try:
        # Manually raise a SystemError
        raise SystemError('This is a system error')  # Manually raising a SystemError
    except SystemError as e:
        print(f"SystemError occurred: {e}")


def trigger_type_error():
    try:
        print('a' + 1)  # Adding a string and an integer
    except TypeError as e:
        print(f"TypeError occurred: {e}")


def trigger_value_error():
    try:
        int('invalid_int')  # Converting a non-integer string to int
    except ValueError as e:
        print(f"ValueError occurred: {e}")


# Run all functions to demonstrate exceptions
if __name__ == "__main__":
    trigger_arithmetic_error()
    trigger_attribute_error()
    trigger_import_error()
    trigger_index_error()
    trigger_io_error()
    trigger_key_error()
    trigger_recursion_error()
    trigger_runtime_error()
    trigger_syntax_error()
    trigger_system_error()
    trigger_type_error()
    trigger_value_error()
