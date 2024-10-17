"""
Module for Calculation class which represents basic calculations for the calculator.
"""
# pylint: disable=unused-import
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    """Represents a calculation consisting of two operands and an operation."""
    def __init__(self, value1: Decimal, value2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initializes the Calculation with two values and an operation.

        :param value1: The first operand for the calculation.
        :param value2: The second operand for the calculation.
        :param operation: The operation to perform (function).
        """
        self.value1 = value1
        self.value2 = value2
        self.operation = operation  # Store the operation

    # This method provides an alternative constructor that
    # can be used without instantiating the class directly
    @staticmethod
    def create(value1: Decimal, value2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Description of what this method does."""
        return Calculation(value1, value2, operation)

    def perform(self) -> Decimal:
        """
        Executes the calculation using the specified operation.

        :return: The result of the operation on value1 and value2.
        """
        return self.operation(self.value1, self.value2)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.value1}, {self.value2}, {self.operation.__name__})"
