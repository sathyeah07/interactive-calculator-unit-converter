def calculator():
    print("\n--- Basic Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator.")

    except ValueError:
        print("Please enter valid numbers.")


def converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion: ")

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            miles = value * 0.621371
            print("Miles:", miles)

        elif choice == "2":
            fahrenheit = (value * 9 / 5) + 32
            print("Fahrenheit:", fahrenheit)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n==============================")
    print(" Interactive Calculator")
    print(" & Unit Converter")
    print("==============================")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        converter()

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice. Please try again.")
