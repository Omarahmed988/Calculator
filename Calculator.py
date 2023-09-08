def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("Welcome to the Codsoft Calculator:').")
    print("Please select an operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = int(input("Enter the number corresponding to the desired operation: "))

        if choice not in range(1, 5):
            print("Invalid choice. Please enter a valid number.")
        else:
            break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        operator = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operator = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operator = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operator = "/"
    else:
        print("Invalid choice.")
        return

    print("The result of", num1, operator, num2, "is:", result)

if __name__ == "__main__":
    main()