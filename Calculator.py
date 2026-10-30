"""Simple Calculator - Arithmetic Operations mini project.
"""
from math import isfinite


def calculate(first, second, choice):
    """Calculate with finite real numbers and a menu choice."""
    if not isfinite(first) or not isfinite(second):
        raise ValueError("Please enter finite numbers only.")
    if choice == "1":
        result = first + second
    elif choice == "2":
        result = first - second
    elif choice == "3":
        result = first * second
    elif choice == "4":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = first / second
    else:
        raise ValueError("Invalid operation.")
    if not isfinite(result):
        raise OverflowError("Result is too large. Use smaller numbers.")
    return result


def main():
    """Repeat the calculator menu until Exit is selected."""
    symbols = {"1": "+", "2": "-", "3": "*", "4": "/"}
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit")
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice == "5":
                print("Thank you for using the calculator!")
                break
            if choice not in symbols:
                print("Invalid choice! Please enter 1 to 5.")
                continue
            try:
                first = float(input("Enter first number: "))
                second = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            try:
                result = calculate(first, second, choice)
            except (ValueError, ZeroDivisionError, OverflowError) as error:
                print("Error:", error)
                continue
            print(f"Result: {first} {symbols[choice]} {second} = {result}")
        except (EOFError, KeyboardInterrupt):
            print("\nCalculator closed.")
            break


if __name__ == "__main__":
    main()