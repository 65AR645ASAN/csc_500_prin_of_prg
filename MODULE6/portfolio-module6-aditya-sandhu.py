# COPY THIS LINE OF CODE - BEGINNING
class ItemToProcure:
    def __init__(self, product_name="none", dollar_value_of_item=0, numerical_quantity_of_product=0):
        self.product_name = product_name
        self.dollar_value_of_item = dollar_value_of_item
        self.numerical_quantity_of_product = numerical_quantity_of_product

    def console_log_item_cost(self):
        total_cost = self.dollar_value_of_item * self.numerical_quantity_of_product
        print(f"{self.product_name} {self.numerical_quantity_of_product} @ ${self.dollar_value_of_item} = ${total_cost}")


def main():
    print("Item 1")
    item1_name = input("Whats the name of item1:\n")
    item1_dollar_value = float(input("Whats the dollar_value of item1:\n"))
    item1_quantity = int(input("Whats the quantity of item1:\n"))
    item1 = ItemToProcure(item1_name, item1_dollar_value, item1_quantity)

    print("\nItem 2")
    item2_name = input("Whats the name of item2:\n")
    item2_dollar_value = float(input("Whats the dollar_value of item2:\n"))
    item2_quantity = int(input("Whats the quantity of item2:\n"))
    item2 = ItemToProcure(item2_name, item2_dollar_value, item2_quantity)

    print("\nHERE IS THE TOTAL COST OF THE TWO ITEMS")
    item1.console_log_item_cost()
    item2.console_log_item_cost()

    total_cost = (item1.dollar_value_of_item * item1.numerical_quantity_of_product) + (item2.dollar_value_of_item * item2.numerical_quantity_of_product)
    print(f"\nTotal: ${total_cost}")


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToProcure):
        self.cart_items.append(item)

    def remove_item(self, product_name: str):
        found = False
        for item in self.cart_items:
            if item.product_name == product_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify: ItemToProcure):
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

    def get_num_items_in_cart(self) -> int:
        total_quantity = sum(item.numerical_quantity_of_product for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self) -> float:
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


class ItemToProcure:
    def __init__(self, product_name="none", dollar_value_of_item=0, numerical_quantity_of_product=0):
        self.product_name = product_name
        self.dollar_value_of_item = dollar_value_of_item
        self.numerical_quantity_of_product = numerical_quantity_of_product

    def console_log_item_cost(self):
        total_cost = self.dollar_value_of_item * self.numerical_quantity_of_product
        print(f"{self.product_name} {self.numerical_quantity_of_product} @ ${self.dollar_value_of_item} = ${total_cost}")


def print_menu(cart: ShoppingCart):
    menu = """
    MENU
    a - Add item to cart
    r - Remove item from cart
    m - Modify item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    """
    while True:
        print(menu)
        choice = input("Choose an option:\n")
        if choice == 'q':
            break
        elif choice == 'a':
            name = input("Enter the item name:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToProcure(name, price, quantity)
            cart.add_item(new_item)
        elif choice == 'r':
            name = input("Enter the name of the item to remove:\n")
            cart.remove_item(name)
        elif choice == 'm':
            name = input("Enter the item name to modify:\n")
            price = float(input("Enter the new price (or 0 to leave unchanged):\n"))
            quantity = int(input("Enter the new quantity (or 0 to leave unchanged):\n"))
            modified_item = ItemToProcure(name, price, quantity)
            cart.modify_item(modified_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
