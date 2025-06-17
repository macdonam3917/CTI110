#Meliyah MacDonald
#6/16/25
#P1HW2
#This program calculates travel expenses





#enter trip budget
budget = int(input("Enter your total budget for the trip (numbers only): "))

#enter travel destination
destination = input("Enter travel destination: ")

#amount they will spend on gas
gas = int(input("Enter the amount you will spend on gas (numbers only): "))

#amount they will spend on accommodations
accommodation = int(input("Enter the amount you will spend on accommodations (numbers only): "))

#amount they will spend on food
food = int(input("Enter the amount you will spend on food (numbers only): "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("Trip Summary:")
print("Destination:", destination)
print("Total Budget: $", budget)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)
