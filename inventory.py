# Simple Inventory Management System

# Inventory dictionary: item_name -> quantity
inventory = {
    "Apples": 30,
    "Bananas": 45,
    "Oranges": 20
}

def display_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("No items in inventory.")
    else:
        for item, qty in inventory.items():
            print(f"{item}: {qty} in stock")
    print("-------------------------\n")

def add_item():
    item = input("Enter item name to add: ").capitalize()
    qty = int(input(f"Enter quantity of {item}: "))
    if item in inventory:
        inventory[item] += qty
    else:
        inventory[item] = qty
    print(f"{item} added/updated successfully.")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        qty = int(input(f"Enter new quantity for {item}: "))
        inventory[item] = qty
        print(f"{item} updated successfully.")
    else:
        print("Item not found.")

def remove_item():
    item = input("Enter item name to remove: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print("Item not found.")

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        update_item()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
