'''
Activity 1 (Problem 1)
Body mass index (BMI) is a measure of health based on weight. It can be calculated by
taking your weight in kilograms and dividing it by the square of your height in meters.
Write a program that prompts the user to enter a weight in pounds and height in inches
and displays the BMI.
--
BMI = Weight (kg) / Height (m)**2
'''
while True:
 i = 1
 Weight_pounds = eval(input("enter weight in pounds : "))
 Height_inches = eval(input("enter height in inches : "))

 poundTOkilogram = 0.45359237
 inchesTOmeters = 0.0254

 Weight_kilogram = Weight_pounds * poundTOkilogram
 Height_meters = Height_inches * inchesTOmeters

 BMI = Weight_kilogram / Height_meters **2
 print("BMI = ", BMI)
 if Weight_pounds == i:
     break