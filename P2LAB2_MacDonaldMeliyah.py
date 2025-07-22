#Meliyah MacDonald
#6/22/25
#P2LAB2
#Create a dictionary of vehicles along with MPG values.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the keys from the dictionary
keys = vehicles.keys()

# Print the vehicle options
print("Available vehicles:")
print(keys)

# Prompt the user to choose one
vehicle = input("Enter the vehicle from the list shown: ")

# Get the MPG of the selected vehicle
mpg = vehicles[vehicle]

# Prompt the user to enter the number of miles they plan to drive
miles = float(input("Enter the number of miles planned to drive: "))

# Calculate gallons needed
gallons_needed = miles / mpg

# Display the result rounded to 2 decimal places
print(f"Gallons of gas needed to drive a {vehicle} for {miles} miles: {round(gallons_needed, 2)} gallons")
