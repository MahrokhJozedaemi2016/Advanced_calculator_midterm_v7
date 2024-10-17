"""
This module defines command classes for arithmetic operations, including addition,
subtraction, multiplication, and division. Each command encapsulates a specific
operation and follows the Command design pattern.
"""

import logging

class Command:
    """Abstract base class for all commands with an execute method."""

    def execute(self):
        """Execute the command operation. Subclasses must implement this method."""
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

class AddCommand(Command):
    """Command to add two values."""


    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        """Execute addition and return the result."""
        result = self.value1 + self.value2
        logging.debug("Executing AddCommand: %s + %s = %s", self.value1, self.value2, result)
        return result

    def __repr__(self):
        return f"Add {self.value1} and {self.value2} = {self.execute()}"

class SubtractCommand(Command):
    """Command to subtract the second value from the first."""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        """Execute subtraction and return the result."""
        result = self.value1 - self.value2
        logging.debug("Executing SubtractCommand: %s - %s = %s", self.value1, self.value2, result)
        return result

    def __repr__(self):
        return f"Subtract {self.value1} and {self.value2} = {self.execute()}"

class MultiplyCommand(Command):
    """Command to multiply two values."""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        """Execute multiplication and return the result."""
        result = self.value1 * self.value2
        logging.debug("Executing MultiplyCommand: %s * %s = %s", self.value1, self.value2, result)
        return result

    def __repr__(self):
        return f"Multiply {self.value1} and {self.value2} = {self.execute()}"

class DivideCommand(Command):
    """Command to divide the first value by the second using a specified strategy."""

    def __init__(self, value1, value2, strategy=None):
        self.value1 = value1
        self.value2 = value2
        self.strategy = strategy if strategy else self.default_division

    def execute(self):
        """Execute division using the specified strategy."""
        if self.value2 == 0:
            logging.error("Attempted to divide by zero: %s / %s", self.value1, self.value2)
            raise ValueError("Cannot divide by zero.")
        result = self.strategy(self.value1, self.value2)
        logging.debug(
            "Executing DivideCommand with strategy %s: %s / %s = %s",
            self.strategy.__name__, self.value1, self.value2, result
        )
        return result

    @staticmethod
    def default_division(value1, value2):
        """Default division strategy, performing standard division."""
        return value1 / value2

    @staticmethod
    def integer_division(value1, value2):
        """Alternative division strategy, performing integer division."""
        return value1 // value2

    def __repr__(self):
        try:
            result = self.execute()
            return f"Divide {self.value1} by {self.value2} = {result}"
        except ValueError:
            return f"Divide {self.value1} by {self.value2} = Cannot divide by zero"
