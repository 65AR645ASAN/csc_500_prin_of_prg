# COPY THIS LINE OF CODE - BEGINNING
class ItemToProcure:
    def __init__(self, product_name="none", dollar_value_of_product=0, numerical_quantity_of_product=0):
        self.product_name = product_name
        self.dollar_value_of_product = dollar_value_of_product
        self.numerical_quantity_of_product = numerical_quantity_of_product

    def console_log_product_cost(self):
        total_grocery_cart_cost = self.dollar_value_of_product * self.numerical_quantity_of_product
        print(f"{self.product_name} {self.numerical_quantity_of_product} @ ${self.dollar_value_of_product} = ${total_grocery_cart_cost}")


def initial_product_to_cart(cart):
    print("Whats the details of the first item:")
    product_name = input("Whats the description of the item:\n")
    product_dollar_value = float(input(f"Whats the dollar value of the {product_name}:\n"))
    product_quantity = int(input(f"Whats the quantity of the {product_name}:\n"))
    item = ItemToProcure(product_name, product_dollar_value, product_quantity)
    cart.add_product(item)

    print("\nHERE IS THE TOTAL COST OF THE ITEM")
    item.console_log_product_cost()

    total_grocery_cart_cost = cart.get_cost_of_cart()
    print(f"\nTotal: ${total_grocery_cart_cost}")


class GroceryCartAtStore:
    def __init__(self, grocery_shoppers_name="none", todays_shopping_date="January 1, 2020"):
        self.grocery_shoppers_name = grocery_shoppers_name
        self.todays_shopping_date = todays_shopping_date
        self.products_in_shopping_cart = []

    def add_product(self, item: ItemToProcure):
        self.products_in_shopping_cart.append(item)

    def remove_product(self, product_name: str):
        found = False
        for item in self.products_in_shopping_cart:
            if item.product_name == product_name:
                self.products_in_shopping_cart.remove(item)
                found = True
                break
        if not found:
            print("The Item to be Removed, wasn't found in the cart, So nothing was REMOVED.")

    def adjust_item(self, product_to_modify: ItemToProcure):
        found = False
        for item in self.products_in_shopping_cart:
            if item.product_name == product_to_modify.product_name:
                if product_to_modify.dollar_value_of_product != 0:
                    item.dollar_value_of_product = product_to_modify.dollar_value_of_product
                if product_to_modify.numerical_quantity_of_product != 0:
                    item.numerical_quantity_of_product = product_to_modify.numerical_quantity_of_product
                found = True
                break
        if not found:
            print("The Item to be Modified, wasn't found in the cart, So nothing was MODIFIED.")

    def get_num_items_in_cart(self) -> int:
        total_quantity = sum(item.numerical_quantity_of_product for item in self.products_in_shopping_cart)
        return total_quantity

    def get_cost_of_cart(self) -> float:
        total_grocery_cart_cost = sum(item.dollar_value_of_product * item.numerical_quantity_of_product for item in self.products_in_shopping_cart)
        return total_grocery_cart_cost

    def total_output(self):
        print(f"{self.grocery_shoppers_name}'s Grocery Cart - {self.todays_shopping_date}")
        if not self.products_in_shopping_cart:
            print("THERE IS NOTHING IN THE Grocery Cart, IT IS EMPTY!")
        else:
            print(f"Total Number of Items in the Grocery Cart: {self.get_num_items_in_cart()}")
            for item in self.products_in_shopping_cart:
                item.console_log_product_cost()
            print(f"\nTotal Cost of the Cart: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.grocery_shoppers_name}'s Grocery Cart - {self.todays_shopping_date}")
        print("Item Descriptions")
        for item in self.products_in_shopping_cart:
            print(f"{item.product_name}: {item.dollar_value_of_product}")


def print_menu(cart: GroceryCartAtStore):
    menu = """
    MENU
    ADD - Add item to cart
    REMOVE - Remove item from cart
    MODIFY - Modify item quantity
    IDENTIFY - Output items' descriptions
    OUTPUT - Output Grocery Cart
    QUIT - Quit
    """
    while True:
        print(menu)
        choice = input(f"{cart.grocery_shoppers_name}, choose an option to edit your Grocery Cart:\n")
        if choice == 'QUIT':
            break
        elif choice == 'ADD':
            name = input(f"{cart.grocery_shoppers_name}, what's the description of the item to add to the existing Grocery Cart:\n")
            price = float(input(f"{cart.grocery_shoppers_name}, what's the price of the {name} being added to the existing Grocery Cart:\n"))
            quantity = int(input(f"{cart.grocery_shoppers_name}, what's the quantity of the {name} being added to the existing Grocery Cart:\n"))
            new_item = ItemToProcure(name, price, quantity)
            cart.add_product(new_item)
        elif choice == 'REMOVE':
            name = input(f"{cart.grocery_shoppers_name}, what's the description of the item to remove from the existing Grocery Cart:\n")
            cart.remove_product(name)
        elif choice == 'MODIFY':
            name = input(f"{cart.grocery_shoppers_name}, what's the description of the item to modify in the existing Grocery Cart:\n")
            price = float(input(f"{cart.grocery_shoppers_name}, what's the new price of {name} (or 0 to leave unchanged):\n"))
            quantity = int(input(f"{cart.grocery_shoppers_name}, what's the new quantity of {name} (or 0 to leave unchanged):\n"))
            modified_item = ItemToProcure(name, price, quantity)
            cart.adjust_item(modified_item)
        elif choice == 'IDENTIFY':
            cart.print_descriptions()
        elif choice == 'OUTPUT':
            cart.total_output()


def main():
    grocery_shoppers_name = input("What's the Grocery Shoppers Name:\n")
    todays_shopping_date = input("What's the Date of the Grocery Shopping [Format ex: Aug 20, 2024]:\n")
    cart = GroceryCartAtStore(grocery_shoppers_name, todays_shopping_date)
    initial_product_to_cart(cart)  # Only one item is initially added
    print_menu(cart)  # Proceed with the menu


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING
