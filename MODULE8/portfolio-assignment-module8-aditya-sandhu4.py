# COPY THIS LINE OF CODE - BEGINNING
class ObjectToProcure:
    def __init__(self, product_name="none", dollar_value_of_product=0, numerical_quantity_of_product=0):
        self.product_name = product_name
        self.dollar_value_of_product = dollar_value_of_product
        self.numerical_quantity_of_product = numerical_quantity_of_product

    def console_log_product_cost(self):
        total_grocery_cart_cost = self.dollar_value_of_product * self.numerical_quantity_of_product
        print(
            f"{self.product_name} {self.numerical_quantity_of_product} @ ${self.dollar_value_of_product} = ${total_grocery_cart_cost}")


def initial_product_to_cart(cart):
    product_name = input("Whats the description of the first Object:\n")
    product_dollar_value = float(input(f"Whats the dollar value of the {product_name}:\n"))
    product_quantity = int(input(f"Whats the quantity of the {product_name}:\n"))
    Object = ObjectToProcure(product_name, product_dollar_value, product_quantity)
    cart.add_product(Object)

    print("\nHERE IS THE TOTAL COST OF THE Object")
    Object.console_log_product_cost()

    total_grocery_cart_cost = cart.get_cost_of_cart()
    print(f"\nTotal: ${total_grocery_cart_cost}")


class GroceryCartAtStore:
    def __init__(self, grocery_shoppers_name="none", todays_shopping_date="September 7, 2024"):
        self.grocery_shoppers_name = grocery_shoppers_name
        self.todays_shopping_date = todays_shopping_date
        self.products_in_shopping_cart = []

    def add_product(self, Object: ObjectToProcure):
        self.products_in_shopping_cart.append(Object)

    def remove_product(self, product_name: str):
        found = False
        for Object in self.products_in_shopping_cart:
            if Object.product_name == product_name:
                self.products_in_shopping_cart.remove(Object)
                found = True
                break
        if not found:
            print("The Object to be Removed, wasn't found in the cart, So nothing was REMOVED.")

    def adjust_Object(self, product_to_modify: ObjectToProcure):
        found = False
        for Object in self.products_in_shopping_cart:
            if Object.product_name == product_to_modify.product_name:
                if product_to_modify.dollar_value_of_product != 0:
                    Object.dollar_value_of_product = product_to_modify.dollar_value_of_product
                if product_to_modify.numerical_quantity_of_product != 0:
                    Object.numerical_quantity_of_product = product_to_modify.numerical_quantity_of_product
                found = True
                break
        if not found:
            print("The Object to be Modified, wasn't found in the cart, So nothing was MODIFIED.")

    def get_num_objects_in_cart(self) -> int:
        total_quantity = sum(Object.numerical_quantity_of_product for Object in self.products_in_shopping_cart)
        return total_quantity

    def get_cost_of_cart(self) -> float:
        total_grocery_cart_cost = sum(Object.dollar_value_of_product * Object.numerical_quantity_of_product for Object in
                                      self.products_in_shopping_cart)
        return total_grocery_cart_cost

    def total_output(self):
        print(f"{self.grocery_shoppers_name}'s Grocery Cart - {self.todays_shopping_date}")
        if not self.products_in_shopping_cart:
            print("THERE IS NOTHING IN THE Grocery Cart, IT IS EMPTY!")
        else:
            print(f"Total Number of objects in the Grocery Cart: {self.get_num_objects_in_cart()}")
            for Object in self.products_in_shopping_cart:
                Object.console_log_product_cost()
            print(f"\nTotal Cost of the Cart: ${self.get_cost_of_cart()}")

    def print_identity(self):
        print(f"{self.grocery_shoppers_name}'s Grocery Cart - {self.todays_shopping_date}")
        print("Object identity")
        for Object in self.products_in_shopping_cart:
            print(f"{Object.product_name}: {Object.dollar_value_of_product}")


def print_menu(cart: GroceryCartAtStore):
    menu = """
    MENU
    ADD - Add Object to cart
    REMOVE - Remove Object from cart
    MODIFY - Modify Object quantity
    IDENTIFY - Output objects' identity
    OUTPUT - Output Grocery Cart
    QUIT - Quit
    """
    while True:
        print(menu)
        selection = input(f"{cart.grocery_shoppers_name}, choose an option to edit your Grocery Cart:\n")
        if selection == 'QUIT':
            break
        elif selection == 'ADD':
            name = input(
                f"{cart.grocery_shoppers_name}, what's the description of the Object to add to the existing Grocery Cart:\n")
            price = float(input(
                f"{cart.grocery_shoppers_name}, what's the price of the {name} being added to the existing Grocery Cart:\n"))
            quantity = int(input(
                f"{cart.grocery_shoppers_name}, what's the quantity of the {name} being added to the existing Grocery Cart:\n"))
            new_Object = ObjectToProcure(name, price, quantity)
            cart.add_product(new_Object)
        elif selection == 'REMOVE':
            name = input(
                f"{cart.grocery_shoppers_name}, what's the description of the Object to remove from the existing Grocery Cart:\n")
            cart.remove_product(name)
        elif selection == 'MODIFY':
            name = input(
                f"{cart.grocery_shoppers_name}, what's the description of the Object to modify in the existing Grocery Cart:\n")
            price = float(
                input(f"{cart.grocery_shoppers_name}, what's the new price of {name} (or 0 to leave unchanged):\n"))
            quantity = int(
                input(f"{cart.grocery_shoppers_name}, what's the new quantity of {name} (or 0 to leave unchanged):\n"))
            modified_Object = ObjectToProcure(name, price, quantity)
            cart.adjust_Object(modified_Object)
        elif selection == 'IDENTIFY':
            cart.print_identity()
        elif selection == 'OUTPUT':
            cart.total_output()


def main():
    grocery_shoppers_name = input("What's the Grocery Shoppers Name:\n")
    todays_shopping_date = input("What's the Date of the Grocery Shopping [Format ex: Month Date, Year [Sept 1st, 2024]]:\n")
    print(f"Client name: {grocery_shoppers_name}")
    print(f"Today's date: {todays_shopping_date}")

    cart = GroceryCartAtStore(grocery_shoppers_name, todays_shopping_date)
    initial_product_to_cart(cart)
    print_menu(cart)


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING
