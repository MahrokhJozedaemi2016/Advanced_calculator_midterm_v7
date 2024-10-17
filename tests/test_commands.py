"""
This module contains tests for the various command classes in the calculator application.
It verifies the correct behavior of arithmetic operations and error handling.
"""

import pytest
from calculator.commands import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_command_execute_not_implemented():
    """
    Test that the base Command class raises NotImplementedError when execute is called.
    """
    command = Command()
    with pytest.raises(NotImplementedError, match="Subclasses must implement the 'execute' method."):
        command.execute()

def test_add_command_repr():
    """
    Test the string representation (__repr__) of the AddCommand class.
    """
    add_command = AddCommand(2, 3)
    assert repr(add_command) == "Add 2 and 3 = 5", "AddCommand __repr__ failed"

def test_subtract_command_repr():
    """
    Test the string representation (__repr__) of the SubtractCommand class.
    """
    subtract_command = SubtractCommand(5, 3)
    assert repr(subtract_command) == "Subtract 5 and 3 = 2", "SubtractCommand __repr__ failed"

def test_multiply_command_repr():
    """
    Test the string representation (__repr__) of the MultiplyCommand class.
    """
    multiply_command = MultiplyCommand(4, 3)
    assert repr(multiply_command) == "Multiply 4 and 3 = 12", "MultiplyCommand __repr__ failed"

def test_divide_command_repr():
    """
    Test the string representation (__repr__) of the DivideCommand class.
    """
    divide_command = DivideCommand(10, 2)
    assert repr(divide_command) == "Divide 10 by 2 = 5.0", "DivideCommand __repr__ failed"

def test_divide_command_by_zero_repr():
    """
    Test that DivideCommand raises a ValueError when dividing by zero.
    """
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
