"""
This module provides the AddCommand plugin for the Calculator.
The AddCommand class is responsible for executing addition operations.
"""

from calculator.commands import Command

class AddCommand(Command):
    """A command to perform addition of two values."""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        """Execute the addition command."""
        return self.value1 + self.value2

def register():
    """Register the AddCommand class for use in the Calculator."""
    return AddCommand
