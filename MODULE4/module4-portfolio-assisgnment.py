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
