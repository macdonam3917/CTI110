#Meliyah MacDonald
#6/29/25
#P3LAB
#Create a code that calculates the most efficient number of dollars and coins, given the amount of money>

#Ask the user to enter a money amount (as a decimal)
money = float(input("Enter a money amount: "))

#Convert the amount to cents (multiply by 100 and convert to integer)
cents = int(money * 100)

#Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

#Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

#Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

#Calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)

#What’s left are pennies
pennies = cents

#Print results only if that coin amount is greater than 0
print("\nYou will need:")

if dollars == 1:
    print("1 dollar")
else:
    if dollars > 1:
        print(str(dollars) + " dollars")

if quarters == 1:
    print("1 quarter")
else:
    if quarters > 1:
        print(str(quarters) + " quarters")

if dimes == 1:
    print("1 dime")
else:
    if dimes > 1:
        print(str(dimes) + " dimes")

if nickels == 1:
    print("1 nickel")
else:
    if nickels > 1:
        print(str(nickels) + " nickels")

if pennies == 1:
    print("1 penny")
else:
    if pennies > 1:
        print(str(pennies) + " pennies")
