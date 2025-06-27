# Predefined grocery items with prices
grocery_items = {
    "apple": 200,
    "banana": 70,
    "milk": 60,
    "bread": 10,
    "eggs": 22
}

# Cart to hold selected items
cart = {}

print("Welcome to the Grocery Store!")
print("Available items:")
for item, price in grocery_items.items():
    print(f"- {item.title()}: ${price:.2f}")

while True:
    item_name = input(
        "\nEnter item name to add to cart (or type 'checkout' to finish): ").lower()

    if item_name == "checkout":
        break

    if item_name in grocery_items:
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            if quantity > 0:
                if item_name in cart:
                    cart[item_name] += quantity
                else:
                    cart[item_name] = quantity
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Please enter a valid number for quantity.")
    else:
        print("Item not found. Please choose from the available items.")

# Displaying the final bill
print("\n----- Final Bill -----")
total = 0
for item, quantity in cart.items():
    price = grocery_items[item]
    subtotal = price * quantity
    total += subtotal
    print(f"{item.title()} - Quantity: {quantity}, Subtotal: ${subtotal:.2f}")

print(f"Total: ${total:.2f}")
print("Thank you for shopping!")
