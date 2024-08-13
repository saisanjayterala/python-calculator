import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Invalid input for square root"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error: Invalid input for logarithm"
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error: Factorial not defined for negative numbers"
    return math.factorial(int(x))

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Factorial")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")

    choice = input("Enter choice (1-12): ")

    if choice == '12':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    elif choice in ('6', '8', '9', '10', '11'):
        num1 = float(input("Enter a number: "))

    elif choice == '7':
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter base: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    elif choice == '5':
        print("Result:", power(num1, num2))

    elif choice == '6':
        print("Result:", square_root(num1))

    elif choice == '7':
        print("Result:", logarithm(num1, num2))

    elif choice == '8':
        print("Result:", factorial(num1))

    elif choice == '9':
        print("Result:", sine(num1))

    elif choice == '10':
        print("Result:", cosine(num1))

    elif choice == '11':
        print("Result:", tangent(num1))

    else:
        print("Invalid input")