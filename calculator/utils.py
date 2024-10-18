# utils.py
"""
Utility functions for the calculator, such as operation mappings.
"""
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def get_operation_mappings():
    """
    Returns a dictionary mapping operation names to their respective command classes.
    """
    return {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand
    }
