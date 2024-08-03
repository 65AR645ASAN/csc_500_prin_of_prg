class InventoryManager:
    """Class to manage an inventory of items."""

    def __init__(self, initial_inventory):
        """
        Initialize the InventoryManager with an initial inventory.

        Args:
        initial_inventory (list of int): List containing the initial quantities of items.
        """
        self.inventory = initial_inventory

    def sell_item(self, index, quantity):
        """
        Sell a specified quantity of an item from the inventory.

        Args:
        index (int): The index of the item in the inventory list.
        quantity (int): The quantity of the item to be sold.

        Returns:
        None
        """
        if 0 <= index < len(self.inventory):
            self.inventory[index] -= quantity
            if self.inventory[index] < 0:
                self.inventory[index] = 0
        else:
            print("Invalid index. Please provide a valid index within the inventory range.")

    def display_inventory(self):
        """Display the current state of the inventory."""
        print("Updated inventory:", self.inventory)


# Example usage:
initial_inventory = [20, 50, 15, 30, 10]
inventory_manager = InventoryManager(initial_inventory)

# Sell 5 units of the third item (index 2)
inventory_manager.sell_item(2, 5)

# Display the updated inventory
inventory_manager.display_inventory()