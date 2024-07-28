import random

# Functions of the Random Module

# choice, choices, shuffle - choosing random elements from lists and sequences
# Example usage for later (with explanation):
items = [1, 2, 3, 4, 5]
print("random.choice(items) =", random.choice(items))  # Randomly choose one item
print("random.choices(items, k=3) =", random.choices(items, k=3))  # Randomly choose 3 items with replacement
random.shuffle(items)  # Shuffle the list in place
print("Shuffled items =", items)

# randrange - integer in range(start, stop, step)
print("random.randrange(1, 100, 3) =", random.randrange(1, 100, 3))  # Output: random integer between 1 and 100, stepping by 3

# randint - integer in [min, max]
print("random.randint(1, 10) =", random.randint(1, 10))  # Output: random integer between 1 and 10

# random - real number in [0.0, 1.0)
print("random.random() =", random.random())  # Output: random float between 0.0 and 1.0

# seed - sets value that influences sequence of numbers generated
random.seed(42)  # Setting the seed to 42
print("random.random() with seed 42 =", random.random())  # Output: deterministic random float due to seed

# uniform - real number in [min, max]
print("random.uniform(2.5, 10.75) =", random.uniform(2.5, 10.75))  # Output: random float between 2.5 and 10.75
