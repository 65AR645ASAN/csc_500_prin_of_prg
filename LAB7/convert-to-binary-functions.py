def int_to_reverse_binary(integer_value):
    binary_reverse = ''
    while integer_value > 0:
        output = integer_value % 2
        binary_reverse = binary_reverse + str(output)
        integer_value = integer_value // 2

    return binary_reverse


def string_reverse(input_string):
    """Reverses the given input string."""
    output = input_string[::-1]
    print(output)
    return output


if __name__ == "__main__":
    integer_value = int(input())
    input_string = int_to_reverse_binary(integer_value)
    string_reverse(input_string)
