"""
Explanation:
Step 4: The ShoppingCart class is built with methods to add, remove, modify items, and calculate the total cost and quantity of items in the cart.
Step 5: The print_menu() function handles the user interaction for managing the shopping cart. The menu continues to prompt until the user selects the quit option ('q').
Step 6: The main section sets up a ShoppingCart object and invokes the print_menu() function to manage the shopping cart operations.
This setup provides a comprehensive framework for the online shopping cart application, covering the creation, management, and display of items in a customer's cart.
"""


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.product_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.product_name == item_to_modify.product_name:
                if item_to_modify.dollar_value_of_item != 0:
                    item.dollar_value_of_item = item_to_modify.dollar_value_of_item
                if item_to_modify.numerical_quantity_of_product != 0:
                    item.numerical_quantity_of_product = item_to_modify.numerical_quantity_of_product
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.numerical_quantity_of_product for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.dollar_value_of_item * item.numerical_quantity_of_product for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.console_log_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.product_name}: {item.dollar_value_of_item}")
