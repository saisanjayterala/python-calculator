import math
import cmath
import statistics
import sys

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

def mean(*args):
    return statistics.mean(args)

def median(*args):
    return statistics.median(args)

def mode(*args):
    try:
        return statistics.mode(args)
    except statistics.StatisticsError:
        return "No unique mode found"

def standard_deviation(*args):
    return statistics.stdev(args)

def to_binary(x):
    return bin(int(x))[2:]

def from_binary(x):
    return int(x, 2)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return f"BMI: {bmi:.2f}"

def exit_calculator():
    print("Exiting the calculator. Goodbye!")
    sys.exit(0)

operations = {
    '1': ('Add', add, 2),
    '2': ('Subtract', subtract, 2),
    '3': ('Multiply', multiply, 2),
    '4': ('Divide', divide, 2),
    '5': ('Power', power, 2),
    '6': ('Nth Root', nth_root, 2),
    '7': ('Complex Square Root', complex_sqrt, 1),
    '8': ('Logarithm', logarithm, 2),
    '9': ('Factorial', factorial, 1),
    '10': ('Sine', sine, 1),
    '11': ('Cosine', cosine, 1),
    '12': ('Tangent', tangent, 1),
    '13': ('Mean', mean, -1),
    '14': ('Median', median, -1),
    '15': ('Mode', mode, -1),
    '16': ('Standard Deviation', standard_deviation, -1),
    '17': ('To Binary', to_binary, 1),
    '18': ('From Binary', from_binary, 1),
    '19': ('Calculate BMI', calculate_bmi, 2),
    '20': ('Exit', exit_calculator, 0)
}

while True:
    print("\nSelect operation:")
    for key, (name, _, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Enter choice (1-20): ")

    if choice not in operations:
        print("Invalid input")
        continue

    operation_name, func, arg_count = operations[choice]

    if arg_count == 0:
        func()
    elif arg_count == 1:
        x = float(input("Enter a number: "))
        print(f"Result: {func(x)}")
    elif arg_count == 2:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Result: {func(x, y)}")
    else:  # Variable number of arguments
        args = []
        while True:
            value = input("Enter a number (or press Enter to finish): ")
            if value == "":
                break
            args.append(float(value))
        if len(args) < 2:
            print("Error: At least two values are required")
        else:
            print(f"Result: {func(*args)}")