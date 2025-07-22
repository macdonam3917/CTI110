#Meliyah MacDonald
#6/23/25
#P2HW2
#Design program that averages 6 grades

#Ask the user to enter a grade for Module 1
#Ask the user to enter a grade for Module 2
#Ask the user to enter a grade for Module 3
#Ask the user to enter a grade for Module 4
#Ask the user to enter a grade for Module 5
#Ask the user to enter a grade for Module 6
#Put all the grades into a list called grades_list
#Find the lowest grade using min()
#Find the highest grade using max()
#Add all the grades using sum()
#Divide the total by 6 to get the average
#Print the lowest, highest, total, and average nicely

# Ask the user to enter 6 grades
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store all the grades in a list
grades_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# Get the lowest grade
lowest_grade = min(grades_list)

# Get the highest grade
highest_grade = max(grades_list)

# Add all the grades
total_grades = sum(grades_list)

# Find the average grade
average_grade = total_grades / 6

# Print out the results, lined up nicely
print("\nGrade Summary")
print(f"{'Lowest Grade:':<20} {lowest_grade}")
print(f"{'Highest Grade:':<20} {highest_grade}")
print(f"{'Sum of Grades:':<20} {total_grades}")
print(f"{'Average:':<20} {average_grade:.2f}")
