print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

Operation = input()

if Operation == "1":
    n1 = eval(input("Enter The First Number: "))
    n2 = eval(input("Enter The Second Number: "))
    print("Result...", (n1 + n2))

elif Operation == "2":
    n1 = eval(input("Enter The First Number: "))
    n2 = eval(input("Enter The Second Number: "))
    print("Result...", (n1 - n2))

elif Operation == "3":
    n1 = eval(input("Enter The First Number: "))
    n2 = eval(input("Enter The Second Number: "))
    print("Result...", (n1 * n2))

elif Operation == "4":
    n1 = eval(input("Enter The First Number: "))
    n2 = eval(input("Enter The Second Number: "))
    print("Result...", (n1 // n2), end='\r BYE')
else:
    print("INVAILD..")
