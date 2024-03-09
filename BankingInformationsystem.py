def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

while True:
    print("\nOptions:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'q' to quit")

    user_input = input(": ")

    if user_input == 'q':
        break

    if user_input in ['add', 'subtract', 'multiply', 'divide']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == 'add':
            print("Result:", add(num1, num2))
        elif user_input == 'subtract':
            print("Result:", subtract(num1, num2))
        elif user_input == 'multiply':
            print("Result:", multiply(num1, num2))
        elif user_input == 'divide':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")
