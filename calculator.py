"""Command-line calculator with seven arithmetic operations."""

import sys


def add(no1, no2):
    return no1 + no2


def sub(no1, no2):
    return no1 - no2


def multiply(no1, no2):
    return no1 * no2


def divide(no1, no2):
    if no2 == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return no1 / no2


def power(no1, no2):
    return no1 ** no2


def modulus(no1, no2):
    if no2 == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return no1 % no2


def floor_div(no1, no2):
    if no2 == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return no1 // no2


OPERATIONS = {
    "add": (add, "+"),
    "sub": (sub, "-"),
    "multiply": (multiply, "*"),
    "divide": (divide, "/"),
    "power": (power, "**"),
    "modulus": (modulus, "%"),
    "floor_div": (floor_div, "//"),
}


def format_number(value):
    """Show whole numbers without a trailing .0."""
    if value.is_integer():
        return str(int(value))
    return f"{value:g}"


def main():
    print("\t\t==========")
    print("\t\tCALCULATOR")
    print("\t\t==========")

    while True:
        operation = input(
            "\nEnter the function you want to perform "
            "(add, sub, multiply, divide, power, modulus, floor_div, quit): "
        ).strip().lower()

        if operation == "quit":
            print("Exiting the calculator...")
            break

        if operation not in OPERATIONS:
            print("Invalid operation choice. Please try again.")
            continue

        try:
            no1 = float(input("Enter first number: "))
            no2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        function, symbol = OPERATIONS[operation]

        try:
            result = function(no1, no2)
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            continue

        print(
            f"{format_number(no1)} {symbol} "
            f"{format_number(no2)} = {format_number(result)}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
