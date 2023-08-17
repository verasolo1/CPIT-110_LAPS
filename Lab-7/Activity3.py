"""
Activity 3 (problem 3)
----
Write a program that displays the following two tables side by side (note that 1 mile is
1.609 kilometers and that 1 kilometer is 0.621 mile):
"""
print(format("Miles", "<10s"),
      format("Kilometers", "<10s"),
      "      |    ",
      format("Kilometers", ">10s"),
      format("Miles", ">10s"))
print("--------------------------------------------------------")
# variables
count = 0
miles = 1
kilometers = 20
# First Row
while count < 10:
    miles_to_kilometers = miles * 1.609
    kilometers_to_miles = kilometers / 1.609
    print(format(miles, "<10d"),
          format(miles_to_kilometers, "<10.3f"),
          "      |    ",
          # Second Row
          format(int(kilometers), ">3.0f"),
          format(kilometers_to_miles, ">15.3f"))
    count += 1
    miles += 1
    kilometers += 5
