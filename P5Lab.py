import random

def disperse_change(change):
    #Convert dollars to cents to avoid float issues
    cents = int(round(change * 100))

    #Calculate number of each coin type
    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents  #Whatever left are pennies

    #Print the coins needed
    print("\nYou will need:")

    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(str(dollars) + " dollars")

    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(str(quarters) + " quarters")

    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(str(dimes) + " dimes")

    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(str(nickels) + " nickels")

    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(str(pennies) + " pennies")

def main():
    print("Welcome to the Checkout Machine!\n")

    #Create a random total owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print("Amount owed: $" + str(amount_owed))

    #Ask user how much they are paying
    cash_given = float(input("Enter amount of cash you are providing: $"))

    #Check if enough money was provided
    if cash_given < amount_owed:
        print("Not enough money provided. Transaction canceled.")
    else:
        #Calculate change
        change = round(cash_given - amount_owed, 2)
        print("Change owed: $" + str(change))

        #print the coins needed
        disperse_change(change)


main()
