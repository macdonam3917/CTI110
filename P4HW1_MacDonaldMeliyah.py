#Meliyah MacDonald
#7/9/25
#P4HW1
#Recreate P2HW2

#Enter however many scores
num_scores = int(input("How many scores would you like to enter? "))

#Create empty list to store valid scores
scores = []

#Loop to collect correct number of valid scores
for i in range(num_scores):
    while True:  # Inner loop to validate input
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break  # Valid score entered, break inner loop
        else:
            print("Invalid score! Please enter a number between 0 and 100.")

#calculations
lowest_score = min(scores)
highest_score = max(scores)
total_score = sum(scores)
average_score = total_score / num_scores

#Display results
print("\nScore Summary")
print(f"{'Lowest Score:':<20} {lowest_score}")
print(f"{'Highest Score:':<20} {highest_score}")
print(f"{'Total Score:':<20} {total_score}")
print(f"{'Average Score:':<20} {average_score:.2f}")
