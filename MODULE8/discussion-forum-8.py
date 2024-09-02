class Car:
    def __init__(self, make, model, year):
        self.make = make            # Public attribute
        self.model = model          # Public attribute
        self.__year = year          # Private attribute

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.__year}")

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1885:  # The first car was made in 1886
            self.__year = year
        else:
            print("Invalid year")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing public attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry

# Accessing private attribute directly (not recommended, will raise an AttributeError)
try:
    print(my_car.__year)
except AttributeError as e:
    print(e)  # Output: 'Car' object has no attribute '__year'

# Using getter method to access the private attribute
print(my_car.get_year())  # Output: 2020

# Modifying private attribute using setter method
my_car.set_year(2022)
print(my_car.get_year())  # Output: 2022
