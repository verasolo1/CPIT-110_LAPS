'''
Activity 2 (Problem 2)
------------------
Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays
the number of years and days for the minutes.
----
For simplicity, assume a year has 365 days.
'''
while True:
 i = 0
 minutes = eval(input("enter the number of minutes : "))
 NumberOfDays = minutes // (24 * 60)
 NumberOfYears = NumberOfDays // 365
 RemainingDays = NumberOfDays % 365
 RemainingHours = minutes // 60
 print(minutes, 'Minutes is approximately', NumberOfYears, 'Years', RemainingDays, 'Days', 'and', RemainingHours, 'hours' )
 if minutes == i:
     break
