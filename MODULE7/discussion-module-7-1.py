# Criterion 1: Availability and Suitability of Predefined Functions

# Using a predefined function (built-in)
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # Predefined function to calculate the sum
print(f"Total using predefined function (sum): {total}")


# User-defined alternative to sum numbers
def custom_sum(numbers: list) -> int:
    result = 0
    for num in numbers:
        result += num
    return result


# User-defined alternative to sum numbers
def custom_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


# Using the user-defined function
custom_total = custom_sum(numbers)
print(f"Total using user-defined function (custom_sum): {custom_total}")

# Criterion 2: Customization and Flexibility

# Predefined functions might not be suitable for custom logic
data = {'value1': 10, 'value2': 20, 'value3': 5}


# User-defined function to calculate a custom score based on specific business logic
def calculate_custom_score(data: dict) -> float:
    # Custom formula to calculate score
    score = (data['value1'] * 2.5) + (data['value2'] * 1.5) - data['value3']
    return score


# Using the user-defined function for customized score calculation
custom_score = calculate_custom_score(data)
print(f"Custom score using user-defined function (calculate_custom_score): {custom_score}")


# Criterion 3: Reusability and Maintainability

# Example of user-defined function for processing customer data
def process_customer_data(customers: list) -> list:
    processed_data = []
    for customer in customers:
        # Custom processing logic (e.g., converting names to uppercase)
        processed_data.append(customer.upper())
    return processed_data


# Using the user-defined function for reusability and maintainability
customers = ['Alice', 'Bob', 'Charlie']
processed_customers = process_customer_data(customers)
print(f"Processed customer data using user-defined function (process_customer_data): {processed_customers}")
