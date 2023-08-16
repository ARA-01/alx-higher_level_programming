#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

# Define a dictionary that maps operators to their corresponding functions
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if operator not in operations:
        print("Unknown operator. Available operators:", ", ".join(operations.keys()))
        sys.exit(1)

    result = operations[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
