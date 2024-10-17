"""
This module provides the MultiplyCommand plugin for the Calculator.
The MultiplyCommand class is responsible for executing multiplication operations.
"""

from calculator.commands import Command

class MultiplyCommand(Command):
    """A command to perform multiplication of two values."""

    def __init__(self, value1, value2):
        self.value1 = value1  # First operand
        self.value2 = value2  # Second operand

    def execute(self):
        """Execute the multiplication command and return the result."""
        return self.value1 * self.value2

def register():
    """Register the MultiplyCommand class for use in the Calculator."""
    return MultiplyCommand
