#Meliyah MacDonald
#7/10/25
#P4HW2
#Payroll Calculator


def calculate_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    return regular_pay, overtime_pay, gross_pay, overtime_hours

print("Welcome to the Payroll Calculator!")
print('Type "Done" when you finish entering employees.\n')

total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter the employee's name: ")

while employee_name.strip().lower() != "done":
    # Get hours and pay rate (assumes user enters valid numbers)
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's hourly pay rate: "))

    regular_pay, overtime_pay, gross_pay, overtime_hours = calculate_pay(hours_worked, pay_rate)

    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display payroll summary for this employee
    print("\n------ Payroll Summary ------")
    print(f"Employee Name:      {employee_name}")
    print(f"Pay Rate:           ${pay_rate:.2f}")
    print(f"Hours Worked:       {hours_worked}")
    print(f"Overtime Hours:     {overtime_hours}")
    print(f"Regular Pay:        ${regular_pay:.2f}")
    print(f"Overtime Pay:       ${overtime_pay:.2f}")
    print(f"Gross Pay:          ${gross_pay:.2f}\n")

    # Ask for next employee name
    employee_name = input("Enter the employee's name: ")

# After loop ends, print totals
print("====== Payroll Totals ======")
print(f"Number of Employees Processed: {employee_count}")
print(f"Total Regular Pay:             ${total_regular_pay:.2f}")
print(f"Total Overtime Pay:            ${total_overtime_pay:.2f}")
print(f"Total Gross Pay:               ${total_gross_pay:.2f}")
print("All set! Thank you!")
