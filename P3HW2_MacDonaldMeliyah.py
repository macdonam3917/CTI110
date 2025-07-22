#Meliyah MacDonald
#7/2/25
#Build code for employee pay

#enter the employee's name
employee_name = input("Enter the employee's name: ")

#enter hours worked and convert to float
hours_worked = float(input("Enter number of hours worked this week: "))

#enter the employee's hourly pay rate and convert to float
pay_rate = float(input("Enter the employee's hourly pay rate: "))

#Calculate pay based on whether employee worked overtime
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    regular_pay = regular_hours * pay_rate
    overtime_pay = 0

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the payroll summary using f-strings for formatting
print("------ Payroll Summary ------")
print(f"Employee Name:      {employee_name}")
print(f"Pay Rate:           ${pay_rate:.2f}")
print(f"Hours Worked:       {hours_worked}")
print(f"Overtime Hours:     {overtime_hours}")
print(f"Overtime Pay:       ${overtime_pay:.2f}")
print(f"Regular Pay:        ${regular_pay:.2f}")
print(f"Gross Pay:          ${gross_pay:.2f}")
