# Movie Ticket Booking Simulation

movies = {
    "1": {"title": "ክሱት", "time": "6:00 PM", "price": 8.00},
    "2": {"title": "ዘጠኝ ሞት", "time": "7:30 PM", "price": 7.50},
    "3": {"title": "የሱፍ አበባ", "time": "8:15 PM", "price": 9.00},
    "4": {"title": "የወንዶች ጉዳይ 1", "time": "5:45 PM", "price": 6.50}
}

total_tickets = 0
total_cost = 0.0

print("Welcome to the Movie Ticket Booking System!")
print("Available movies:")

for key, info in movies.items():
    print(
        f"{key}. {info['title']} at {info['time']} - ${info['price']:.2f} per ticket")

while True:
    choice = input(
        "\nEnter the number of the movie you'd like to book: ").strip()

    if choice not in movies:
        print("Invalid choice. Please try again.")
        continue

    try:
        num_tickets = int(input("How many tickets would you like to book? "))
        if num_tickets <= 0:
            print("Number of tickets must be positive.")
            continue
    except ValueError:
        print("Invalid number of tickets.")
        continue

    selected = movies[choice]
    cost = num_tickets * selected["price"]
    total_tickets += num_tickets
    total_cost += cost

    print(
        f"\nBooking confirmed: {num_tickets} tickets for '{selected['title']}' at {selected['time']}")
    print(f"Total for this booking: ${cost:.2f}")

    another = input(
        "Would you like to book another movie? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Final summary
print("\n Booking Summary:")
print(f"Total tickets booked: {total_tickets}")
print(f"Total cost: ${total_cost:.2f}")
print("Thank you for using the Movie Ticket Booking System!")
