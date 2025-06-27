#################### Vending Machine Program#####################

items = {
    "1": {"name": "Chips", "price": 1.50},
    "2": {"name": "Soda", "price": 1.00},
    "3": {"name": "Chocolate Bar", "price": 1.25},
    "4": {"name": "Water", "price": 0.75},
    "5": {"name": "Gum", "price": 0.50}
}

print("Welcome to the Vending Machine!")
print("Here are the available items:")
for number, info in items.items():
    print(f"{number}. {info['name']} - ${info['price']:.2f}")

cart = []

while True:
    choice = input(
        "\nEnter the item number to select (or type 'done' to finish): ").strip()
    if choice.lower() == "done":
        break
    elif choice in items:
        cart.append(items[choice])
        print(f"Added {items[choice]['name']} to your cart.")
    else:
        print("Invalid item number. Please try again.")

print("\n--- Receipt ---")
total = 0
for item in cart:
    print(f"{item['name']} - ${item['price']:.2f}")
    total += item["price"]
print(f"Total: ${total:.2f}")
print("Thank you for using the Vending Machine!")
