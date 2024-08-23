# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Appending an element
fruits.append('date')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Inserting an element at index 1
fruits.insert(1, 'blueberry')
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date']

# Extending the list with another list
fruits.extend(['elderberry', 'fig'])
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Updating an element
fruits[1] = 'blackberry'
print(fruits)  # Output: ['apple', 'blackberry', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Removing an element by value
fruits.remove('cherry')
print(fruits)  # Output: ['apple', 'blackberry', 'banana', 'date', 'elderberry', 'fig']

# Removing an element by index and returning it
removed_fruit = fruits.pop(2)
print(fruits)  # Output: ['apple', 'blackberry', 'date', 'elderberry', 'fig']
print(removed_fruit)  # Output: 'banana'

# Removing an element using del
del fruits[0]
print(fruits)  # Output: ['blackberry', 'date', 'elderberry', 'fig']

# Creating a dictionary
person = {'name': 'John', 'age': 30}

# Inserting a new key-value pair
person['city'] = 'New York'
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Updating an existing key
person['age'] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Updating multiple key-value pairs
person.update({'name': 'Jane', 'profession': 'Engineer'})
print(person)  # Output: {'name': 'Jane', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}


# Removing an element by key
del person['city']
print(person)  # Output: {'name': 'Jane', 'age': 31, 'profession': 'Engineer'}

# Removing and returning a value by key
age = person.pop('age')
print(person)  # Output: {'name': 'Jane', 'profession': 'Engineer'}
print(age)  # Output: 31

# Removing the last inserted key-value pair
last_item = person.popitem()
print(person)  # Output: {'name': 'Jane'}
print(last_item)  # Output: ('profession', 'Engineer')

















