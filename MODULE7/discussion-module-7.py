# Using predefined function
total = sum([1, 2, 3, 4])


# Example of user-defined function
def custom_sum(numbers: list) -> int:
    result = 0
    for num in numbers:
        result += num
    return result


print(custom_sum([1, 2, 3, 4]))  # Output: 10


def calculate_custom_score(data: dict) -> float:
    # Custom logic to calculate score
    score = (data['value1'] * 2.5) + (data['value2'] * 1.5) - data['value3']
    return score


data = {'value1': 10, 'value2': 20, 'value3': 5}
print(calculate_custom_score(data))  # Output: 60.0


def process_customer_data(customers: list) -> list:
    processed_data = []
    for customer in customers:
        # Assume some complex processing here
        processed_data.append(customer.upper())
    return processed_data


customers = ['Alice', 'Bob', 'Charlie']
print(process_customer_data(customers))  # Output: ['ALICE', 'BOB', 'CHARLIE']
