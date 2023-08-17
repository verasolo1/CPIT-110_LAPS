"""
Activity 2 (problem 2)
----
Write a program that displays the following two tables side by side (note that 1 kilogram is
2.2 pounds and that 1 pound is 0.45 kilograms) :
"""
print(format("Kilograms", "<10s"),
      format("pounds", ">10s"),
      "      |    ",
      format("pounds", "<10s"),
      format("Kilograms", ">10s"))
print("--------------------------------------------------------")
Kilograms = 1
pounds = 20
count = 0
while count < 100:
    kilograms_to_pounds = Kilograms * 2.2
    pounds_to_kilograms = pounds / 2.2
    print(format(Kilograms, "<10d"),
          format(kilograms_to_pounds, "10.1f"),
          "      |    ",
          format(pounds_to_kilograms, "10.2f"))
    Kilograms += 2
    pounds += 5
    count += 1
