def print_pattern():
    print("3 2 1 Go!")
    print("*****")
    print("*   *")
    print("*****")
    print("*   *")
    print("*****")


def calculate_dog_years():
    try:
        human_years = int(input('Enter age of dog (in human years): '))
        print()
        dog_years = 7 * human_years
        print(human_years, 'human years is about', end=' ')
        print(dog_years, 'dog years.')
    except ValueError:
        print("Invalid input! Please enter a valid integer for the dog's age.")


def sum_two_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1 + num2)
    except ValueError:
        print("Invalid input! Please enter valid integers.")


def calculate_triangle_area():
    try:
        print('Enter triangle base (cm): ')
        triangle_base = int(input())
        print('Enter triangle height (cm): ')
        triangle_height = int(input())
        triangle_area = (triangle_base * triangle_height) / 2
        print('Triangle area = (', end=' ')
        print(triangle_base, end=' ')
        print('*', end=' ')
        print(triangle_height, end=' ')
        print(') / 2 = ', end=' ')
        print(triangle_area, end=' ')
        print('cm**2')
    except ValueError:
        print("Invalid input! Please enter valid integers for the triangle base and height.")


def calculate_total_beans():
    num_beans = 500
    num_jars = 3
    total_beans = num_beans * num_jars
    print(num_beans, 'beans in', end=' ')
    print(num_jars, 'jars yields', end=' ')
    print(total_beans, 'total')


def print_predictions():
    print('Predictions are hard.')
    print('Especially about the future.')
    user_num = 5
    print('user_num is:', user_num)


def calculate_salaries(hourly_wage):
    annual_salary = hourly_wage * 40 * 50
    print('Annual salary is: ')
    print(annual_salary)
    print()
    monthly_salary = annual_salary / 12
    print('Monthly salary is: ')
    print(monthly_salary)
    print()


# Main execution
print_pattern()
calculate_dog_years()
sum_two_numbers()
calculate_triangle_area()
calculate_total_beans()
print_predictions()
calculate_salaries(20)
