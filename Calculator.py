# Write all the functions of a calculator like
# Accept 2 numbers as input and display the sum as output
# Add 2 numbers. Example: {2} + {3} = {5}
# write unit test cases for the calculator functions
# Calculator.py

import random
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def modulus(a, b):
    """Return the modulus of two numbers."""
    return a % b
def exponent(a, b):
    """Return the exponentiation of a number."""
    return a ** b
def floor_division(a, b):
    """Return the floor division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b
def calculator(a, b, operation):
    """Perform a calculation based on the operation specified."""
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    elif operation == 'divide':
        return divide(a, b)
    elif operation == 'modulus':
        return modulus(a, b)
    elif operation == 'exponent':
        return exponent(a, b)
    elif operation == 'floor_division':
        return floor_division(a, b)
    else:
        raise ValueError("Invalid operation specified.")
def fn_generate_random(seed_value):
    """Generate a random number based on a seed value."""
    random.seed(seed_value)
    return random.randint(1, 100)

def main():
    """Main function to run the calculator."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide, modulus, exponent, floor_division): ").strip().lower()
        result = calculator(a, b, operation)
        print(f"The result of {a} {operation} {b} is: {result}")
        print("#####################")
        c=float(input("Enter the Random number:"))
        random_number = fn_generate_random(c)
        print(f"The Random Number generated is : {random_number}")

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
# Unit tests for the calculator functions
