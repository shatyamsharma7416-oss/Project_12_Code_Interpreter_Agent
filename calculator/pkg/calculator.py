# Deliberate Broken Calculator Code

def add(a, b)
    return a + b

def subtract(a, b):
    # Bug: This will add instead of subtract
    return a + b 

def multiply(a, b):
    # Bug: Missing return statement entirely
    result = a * b

def divide(a, b):
    # Bug: Will crash with ZeroDivisionError if b is 0
    return a / b


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Bug: input() returns strings, but we are comparing to integers
if choice == 1:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    # Bug: num1 and num2 are strings. "+" will concatenate them (e.g., "5" + "3" = "53")
    print("Result:", add(num1, num2))

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", subtract(num1, num2))

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", multiply(num1, num2))

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", divide(num1, num2))

else
    print("Invalid Input")
