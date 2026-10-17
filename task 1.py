# Task 2: Command-line calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Not divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("for stop  'q' \n")

    while True:
        choice = input("Operation chunein (+, -, *, /, q): ")
        if choice == "q":
            print("Calculator is close !")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("wrong operation. Try again.\n")
            continue

        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except ValueError:
            print("Write only numbers.\n")
            continue

        if choice == "+":
            result = add(x, y)
        elif choice == "-":
            result = subtract(x, y)
        elif choice == "*":
            result = multiply(x, y)
        else:
            result = divide(x, y)

        print("Result:", result, "\n")

if __name__ == "__main__":
    calculator()