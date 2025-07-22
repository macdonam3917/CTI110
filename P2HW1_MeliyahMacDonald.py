#Meliyah MacDonald
#6/22/25
#P2HW1
#This program calculates travel expenses--Reformatted





# Ask the user for their total trip budget
budget = float(input("Enter your total budget for the trip (numbers only): "))

# Ask the user for their travel destination
destination = input("Enter your travel destination: ")

# Ask the user how much they will spend on gas
gas_cost = float(input("Enter how much you will spend on gas: "))

# Ask the user how much they will spend on accommodations
accommodation_cost = float(input("Enter how much you will spend on accommodations: "))

# Ask the user how much they will spend on food
food_cost = float(input("Enter how much you will spend on food: "))

# Calculate the total of all expenses
total_expenses = gas_cost + accommodation_cost + food_cost

# Calculate how much money will be left after the trip
money_left = budget - total_expenses

# Show the trip summary using formatted output
print("Trip Summary:")
print(f"{'Destination:':<20} {destination}")
print(f"{'Total Budget:':<20} ${budget:.2f}")
print(f"{'Total Expenses:':<20} ${total_expenses:.2f}")
print(f"{'Money Left:':<20} ${money_left:.2f}")
