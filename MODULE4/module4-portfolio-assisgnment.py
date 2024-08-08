# COPY THIS LINE OF CODE - BEGINNING
class ItemToProcure:
    def __init__(self, name_of_item="none", price_of_item=0, quantity_of_item=0):
        self.name_of_item = name_of_item
        self.price_of_item = price_of_item
        self.quantity_of_item = quantity_of_item

    def console_log_item_cost(self):
        total_cost = self.price_of_item * self.quantity_of_item
        print(f"{self.name_of_item} {self.quantity_of_item} @ ${self.price_of_item} = ${total_cost}")


def main():
    print("Item 1")
    item1_name = input("Whats the name of item1:\n")
    item1_price = float(input("Whats the price of item1:\n"))
    item1_quantity = int(input("Whats the quantity of item1:\n"))
    item1 = ItemToProcure(item1_name, item1_price, item1_quantity)

    print("\nItem 2")
    item2_name = input("Whats the name of item2:\n")
    item2_price = float(input("Whats the price of item2:\n"))
    item2_quantity = int(input("Whats the quantity of item2:\n"))
    item2 = ItemToProcure(item2_name, item2_price, item2_quantity)

    print("\nHERE IS THE TOTAL COST OF THE TWO ITEMS")
    item1.console_log_item_cost()
    item2.console_log_item_cost()

    total_cost = (item1.price_of_item * item1.quantity_of_item) + (item2.price_of_item * item2.quantity_of_item)
    print(f"\nTotal: ${total_cost}")


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING
