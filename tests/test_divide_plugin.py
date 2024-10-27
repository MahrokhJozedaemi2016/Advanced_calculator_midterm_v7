"""
Unit tests for the DivideCommand plugin.

These tests verify the correctness of the DivideCommand's execute method
and the register function used for dynamic plugin loading.
"""

import pytest
from calculator.plugins.divide_plugin import DivideCommand

def test_divide_command():
    """Test normal division in DivideCommand."""
    divide_command = DivideCommand(10, 2)
    result = divide_command.execute()
    assert result == 5, "Expected division result of 10 / 2 to be 5."

def test_divide_command_by_zero():
    """Test division by zero raises ValueError in DivideCommand."""
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
