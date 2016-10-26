#Variables
discontinue = None;

#Functions defined
def add(x, y):
    """Addition"""
    return x + y
def subtract(x, y):
    """Subtraction"""
    return x - y
def multiply(x, y):
    """Multiplication"""
    return x * y
def divide(x, y):
    """Division"""
    return x / y

#User input
while discontinue == None:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))
        continueOn = input("Would you like to do another?(y/n)")
        if continueOn == 'y':
            discontinue = True
        elif continueOn == 'n':
            discontinue = False
        else:
            print("Please enter 'y' or 'n'!")
            continueOn = input("Would you like to do another?(y/n)")
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))
    else:
        print("Invalid input")
