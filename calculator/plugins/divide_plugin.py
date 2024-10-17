"""
This module provides the DivideCommand plugin for the Calculator.
The DivideCommand class is responsible for executing divide operations.
"""

from calculator.commands import Command

class DivideCommand(Command):
    """A command to perform division of two values."""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        """Execute the division command."""
        if self.value2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.value1 / self.value2

def register():
    """Register the DivideCommand class for use in the Calculator."""
    return DivideCommand
