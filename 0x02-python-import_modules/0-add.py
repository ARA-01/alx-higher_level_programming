#!/usr/bin/python3

if __name__ == "__main__":
# Assign values to variables
    a = 1
    b = 2

# Import the function from add_0.py
from add_0 import add

# Calculate the result
result = add(a, b)

# Print the result using string formatting
print(f"{a} + {b} = {result}")
