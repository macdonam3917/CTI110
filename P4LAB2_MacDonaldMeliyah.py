#Meliyah MacDonald
#7/9/25
#P4LAB2
#Create code for integers


run_again = "yes" 

while run_again.lower() == "yes":
    #enter a number
    number = int(input("Please enter an integer: "))

    # =Check if the number is 0 or higher
    if number >= 0:
        print(f"\nMultiplication table for {number}:\n")
        
        #loop
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
    else:
        #message for neg numbers
        print("Sorry, I cannot accept negative numbers.")

    #Ask the user wants to run the program again
    run_again = input("\nDo you want to try again? (yes or no): ")
