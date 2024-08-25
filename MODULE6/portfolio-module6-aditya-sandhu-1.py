# COPY THIS LINE OF CODE - BEGINNING
class ItemToProcure:
    def __init__(self, product_name="none", dollar_value_of_item=0, numerical_quantity_of_product=0):
        self.product_name = product_name
        self.dollar_value_of_item = dollar_value_of_item
        self.numerical_quantity_of_product = numerical_quantity_of_product

    def console_log_item_cost(self):
        total_cost = self.dollar_value_of_item * self.numerical_quantity_of_product
        print(f"{self.product_name} {self.numerical_quantity_of_product} @ ${self.dollar_value_of_item} = ${total_cost}")


def initial_items_to_cart(cart):
    print("Item 1")
    item1_name = input("Whats the name of item1:\n")
    item1_dollar_value = float(input("Whats the dollar_value of item1:\n"))
    item1_quantity = int(input("Whats the quantity of item1:\n"))
    item1 = ItemToProcure(item1_name, item1_dollar_value, item1_quantity)
    cart.add_item(item1)

    print("\nItem 2")
    item2_name = input("Whats the name of item2:\n")
    item2_dollar_value = float(input("Whats the dollar_value of item2:\n"))
    item2_quantity = int(input("Whats the quantity of item2:\n"))
    item2 = ItemToProcure(item2_name, item2_dollar_value, item2_quantity)
    cart.add_item(item2)

    print("\nHERE IS THE TOTAL COST OF THE TWO ITEMS")
    item1.console_log_item_cost()
    item2.console_log_item_cost()

    total_cost = cart.get_cost_of_cart()
    print(f"\nTotal: ${total_cost}")


class ShoppingCart:
    def __init__(self, grocery_shoppers_name="none", todays_shopping_date="January 1, 2020"):
        self.grocery_shoppers_name = grocery_shoppers_name
        self.todays_shopping_date = todays_shopping_date
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
            print("The Item to be Removed, wasn't found in the cart, So nothing was REMVED.")

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
            print("The Item to be Modified, wasn't found in the cart, So nothing was MODIFIED.")

    def get_num_items_in_cart(self) -> int:
        total_quantity = sum(item.numerical_quantity_of_product for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self) -> float:
        total_cost = sum(item.dollar_value_of_item * item.numerical_quantity_of_product for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.grocery_shoppers_name}'s Shopping Cart - {self.todays_shopping_date}")
        if not self.cart_items:
            print("THERE IS NOTHING IN THE SHOPPING CART, IT IS EMPTY!")
        else:
            print(f"Total Number of Items in the Shopping Cart: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.console_log_item_cost()
            print(f"\nTotal Cost of the Cart: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.grocery_shoppers_name}'s Shopping Cart - {self.todays_shopping_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.product_name}: {item.dollar_value_of_item}")


def print_menu(cart: ShoppingCart):
    menu = """
    MENU
    ADD - Add item to cart
    REMOVE - Remove item from cart
    MODIFY - Modify item quantity
    IDENTIFY - Output items' descriptions
    OUTPUT - Output shopping cart
    QUIT - Quit
    """
    while True:
        print(menu)
        choice = input("Choose a Option to Edit the current Shopping Cart:\n")
        if choice == 'QUIT':
            break
        elif choice == 'ADD':
            name = input("What's the name of an item to add to the existing shopping cart:\n")
            price = float(input("What's the price of the new item being added to the existing shopping cart:\n"))
            quantity = int(input("What's the quantity of the new item being added to the existing shopping cart:\n"))
            new_item = ItemToProcure(name, price, quantity)
            cart.add_item(new_item)
        elif choice == 'REMOVE':
            name = input("What's the name of the item to remove from the existing shopping cart:\n")
            cart.remove_item(name)
        elif choice == 'MODIFY':
            name = input("What's the name of the item to modify in the existing shopping cart:\n")
            price = float(input("What's the new price of the item (or 0 to leave unchanged):\n"))
            quantity = int(input("What's the new quantity of the item (or 0 to leave unchanged):\n"))
            modified_item = ItemToProcure(name, price, quantity)
            cart.modify_item(modified_item)
        elif choice == 'IDENTIFY':
            cart.print_descriptions()
        elif choice == 'OUTPUT':
            cart.print_total()


def main():
    grocery_shoppers_name = input("What's the Grocery Shoppers Name:\n")
    todays_shopping_date = input("What's the Date of the Grocery Shopping [Format ex: Aug 20, 2024]:\n")
    cart = ShoppingCart(grocery_shoppers_name, todays_shopping_date)
    initial_items_to_cart(cart)
    print_menu(cart)


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING
