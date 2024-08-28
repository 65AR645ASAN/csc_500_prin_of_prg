# Read inputs and store them in a list
user_input = input().split()
names_and_ages = []

while user_input[0] != '-1':
    name = user_input[0]
    age_str = user_input[1]
    # print(f"\n{name, age_str}")

    try:
        age = int(age_str) + 1
        # print(age)

    except ValueError as e:
        print(f"\nValueError occurred: {e}, so the age is set to '0'")
        age = 0
    names_and_ages.append(f"{name} {age}")
    user_input = input().split()

for entry in names_and_ages:
    print(entry)
