def add(a, b):
    print("Addition: ", a + b)

def subtract(a, b):
    print("Subtraction: ", a - b)

def multiply(a, b):
    print("Multiplication: ", a * b)

def divide(a, b):
    if b != 0:
        print("Division: ", a / b)
    else:
        print("Error: Division by zero is not allowed.")

def power(a, b):
    print("Power: ", a ** b)

def modulus(a, b):
    if b != 0:
        print("Modulus: ", a % b)
    else:
        print("Error: Modulus by zero is not allowed.")
