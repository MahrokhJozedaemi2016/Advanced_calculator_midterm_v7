"""
This module contains basic arithmetic operations: addition, subtraction, multiplication, and division.
Each function takes two numeric arguments and returns the result of the operation.
"""

def add(value1, value2):
    """Return the sum of two values."""
    return value1 + value2

def subtract(value1, value2):
    """Return the difference between two values."""
    return value1 - value2

def multiply(value1, value2):
    """Return the product of two values."""
    return value1 * value2

def divide(value1, value2):
    """Return the division of two values. Raises an error if division by zero is attempted."""
    if value2 == 0:
        raise ValueError("Cannot divide by zero.")
    return value1 / value2
