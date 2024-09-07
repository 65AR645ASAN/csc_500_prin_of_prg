class LuxCar:
    def __init__(self, model, price, speed, mileage, origin_country):
        self.__model = model                # Private attribute
        self.__price = price                # Private attribute
        self.__speed = speed                # Private attribute
        self.__mileage = mileage            # Private attribute
        self.__origin_country = origin_country  # Private attribute

    # Display car information
    def display_info(self):
        print(f"Model: {self.__model}, Price: ${self.__price:.2f}, "
              f"Speed: {self.__speed} mph, Mileage: {self.__mileage} mpg, "
              f"Country of Origin: {self.__origin_country}")

    # Getters and Setters for the private variables

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:  # Ensure non-negative price
            self.__price = price
        else:
            raise AssertionError("Price cannot be negative")

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed >= 0:  # Ensure non-negative speed
            self.__speed = speed
        else:
            raise AssertionError("Speed cannot be negative")

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= 0:  # Ensure non-negative mileage
            self.__mileage = mileage
        else:
            raise AssertionError("Mileage cannot be negative")

    def get_origin_country(self):
        return self.__origin_country

    def set_origin_country(self, origin_country):
        self.__origin_country = origin_country


# Creating instances of luxury cars
ferrari = LuxCar("Ferrari SF90", 500000, 211, 18, "Italy")
tesla = LuxCar("Tesla Model S Plaid", 135000, 200, 120, "USA")
bmw = LuxCar("BMW M5", 120000, 190, 20, "Germany")

# Accessing private attributes using getter methods
print(ferrari.get_model())  # Output: Ferrari SF90
print(tesla.get_origin_country())  # Output: USA

# Modifying private attributes using setter methods
try:
    bmw.set_price(-5000)  # This will raise an AssertionError
except AssertionError as e:
    print(e)  # Output: Price cannot be negative

# Displaying information for all cars
ferrari.display_info()  # Output: Model: Ferrari SF90, Price: $500000.00, Speed: 211 mph, Mileage: 18 mpg, Country of Origin: Italy
tesla.display_info()  # Output: Model: Tesla Model S Plaid, Price: $135000.00, Speed: 200 mph, Mileage: 120 mpg, Country of Origin: USA
bmw.display_info()  # Output: Model: BMW M5, Price: $120000.00, Speed: 190 mph, Mileage: 20 mpg, Country of Origin: Germany
