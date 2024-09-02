class CoffeeShopItem:
    def __init__(self, name, price):
        self.__name = None
        self.__name = name          # Private attribute
        self.__price = price        # Private attribute

    def display_info(self):
        print(f"Item: {self.__name}, Price: ${self.__price:.2f}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:  # Ensuring the price is non-negative
            self.__price = price
        else:
            print("Invalid price")

# Creating instances of different items in the coffee shop
frappuccino = CoffeeShopItem("Frappuccino", 4.50)
coffee = CoffeeShopItem("Coffee", 2.00)
creme_brulee_iced_coffee = CoffeeShopItem("Creme Brulee Iced Coffee", 5.75)
banana_cake = CoffeeShopItem("Banana Cake", 3.25)
muffin = CoffeeShopItem("Muffin", 2.75)
yogurt = CoffeeShopItem("Yogurt", 1.50)

# Accessing private attributes directly (not recommended, will raise an AttributeError)
try:
    print(frappuccino.__name)
except AttributeError as e:
    print(e)  # Output: 'CoffeeShopItem' object has no attribute '__name'

# Using getter method to access the private attribute
print(frappuccino.get_name())  # Output: Frappuccino

# Modifying private attributes using setter methods
frappuccino.set_price(4.75)
print(frappuccino.get_price())  # Output: 4.75

# Displaying information for all items
coffee.display_info()                 # Output: Item: Coffee, Price: $2.00
creme_brulee_iced_coffee.display_info()  # Output: Item: Creme Brulee Iced Coffee, Price: $5.75
banana_cake.display_info()            # Output: Item: Banana Cake, Price: $3.25
muffin.display_info()                 # Output: Item: Muffin, Price: $2.75
yogurt.display_info()                 # Output: Item: Yogurt, Price: $1.50
