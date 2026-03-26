try:
    # Taking input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Menu
    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))

    # Operations
    if choice == 1:
        result = num1 + num2

    elif choice == 2:
        result = num1 - num2

    elif choice == 3:
        result = num1 * num2

    elif choice == 4:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2

    else:
        raise ValueError("Invalid menu choice")

# Exception Handling
except ValueError as ve:
    print("Value Error:", ve)

except ZeroDivisionError as zde:
    print("Zero Division Error:", zde)

except Exception:
    print("Something went wrong")

# Success case
else:
    print("Result:", result)

# Always runs
finally:
    print("Program Ended")