import math
import cmath
import random

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

def nth_root(x, n):
    if x < 0 and n % 2 == 0:
        return f"Error: Even root of negative number"
    return x ** (1/n)

def complex_sqrt(x):
    return cmath.sqrt(x)

def exponential(x):
    return math.exp(x)

def natural_log(x):
    if x <= 0:
        return "Error: Invalid input for natural logarithm"
    return math.log(x)

def absolute_value(x):
    return abs(x)

def floor(x):
    return math.floor(x)

def ceiling(x):
    return math.ceil(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def arcsin(x):
    if x < -1 or x > 1:
        return "Error: Input must be between -1 and 1"
    return math.degrees(math.asin(x))

def arccos(x):
    if x < -1 or x > 1:
        return "Error: Input must be between -1 and 1"
    return math.degrees(math.acos(x))

def arctan(x):
    return math.degrees(math.atan(x))

def random_number(start, end):
    return random.randint(start, end)

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Nth Root")
    print("7. Complex Square Root")
    print("8. Exponential")
    print("9. Natural Logarithm")
    print("10. Absolute Value")
    print("11. Floor")
    print("12. Ceiling")
    print("13. Sine")
    print("14. Cosine")
    print("15. Tangent")
    print("16. Arcsine")
    print("17. Arccosine")
    print("18. Arctangent")
    print("19. Random Number")
    print("20. Exit")

    choice = input("Enter choice (1-20): ")

    if choice == '20':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ('7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'):
        num1 = float(input("Enter a number: "))
    elif choice == '19':
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))

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
        print("Result:", nth_root(num1, int(num2)))
    elif choice == '7':
        print("Result:", complex_sqrt(num1))
    elif choice == '8':
        print("Result:", exponential(num1))
    elif choice == '9':
        print("Result:", natural_log(num1))
    elif choice == '10':
        print("Result:", absolute_value(num1))
    elif choice == '11':
        print("Result:", floor(num1))
    elif choice == '12':
        print("Result:", ceiling(num1))
    elif choice == '13':
        print("Result:", sine(num1))
    elif choice == '14':
        print("Result:", cosine(num1))
    elif choice == '15':
        print("Result:", tangent(num1))
    elif choice == '16':
        print("Result:", arcsin(num1))
    elif choice == '17':
        print("Result:", arccos(num1))
    elif choice == '18':
        print("Result:", arctan(num1))
    elif choice == '19':
        print("Result:", random_number(start, end))
    else:
        print("Invalid input")