'''
activity 2 (problem 2)
Write a program that reads the following information and prints a payroll statement:

Employee’s name (e.g., Smith)

Number of hours worked in a week (e.g., 10)

Hourly pay rate (e.g., 9.75)

Federal tax withholding rate (e.g., 20%)

State tax withholding rate (e.g., 9%)
'''
employee_name = input("Enter employee's name: ")
work_hours = eval(input("Enter number of hours worked in a week: "))
hourly_payRate = eval(input("Enter hourly pay rate: "))
fedral_tax = eval(input("Enter federal tax withholding rate: "))
state_tax = eval(input("Enter state tax withholding rate: "))

grosspay = work_hours * hourly_payRate
fedTaxWithholding = grosspay * fedral_tax
stateTaxWithholding = grosspay * state_tax
totalDeduction = fedTaxWithholding + stateTaxWithholding
netPay = grosspay - totalDeduction
out = "Employee Name: " + employee_name + "\n\n"
out += "Hours Worked: " + str(work_hours) + '\n'
out += "Pay Rate: $" + str(hourly_payRate) + '\n'
out += "Gross Pay: $" + str(grosspay) + '\n'
out += "Deductions:\n"
out += " Federal Withholding (" + str(fedral_tax * 100) + \
 "%): $" + str(int(fedTaxWithholding * 100) / 100.0) + '\n'
out += " State Withholding (" + str(state_tax * 100) + "%):" + \
 " $" + str(int(stateTaxWithholding * 100) / 100.0) + '\n'
out += " Total Deduction:" + " $" + \
 str(int(totalDeduction * 100) / 100.0) + '\n'
out += "Net Pay:" + " $" + str(int(netPay * 100) / 100.0)
print(out)





