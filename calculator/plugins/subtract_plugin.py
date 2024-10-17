"""
This module provides the SubtractCommand plugin for the Calculator.
The SubtractCommand class is responsible for executing subtraction operations.
"""

from calculator.commands import Command

class SubtractCommand(Command):
    """A command to perform subtraction of two values."""

    def __init__(self, value1, value2):
        self.value1 = value1  # Minuend
        self.value2 = value2  # Subtrahend

    def execute(self):
        """Execute the subtraction command and return the result."""
        return self.value1 - self.value2

def register():
    """Register the SubtractCommand class for use in the Calculator."""
    return SubtractCommand
