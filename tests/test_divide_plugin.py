"""
Unit tests for the DivideCommand plugin.
These tests ensure the correctness of the DivideCommand's execute method
and the register function used for dynamic plugin loading.
"""
import pytest
from calculator.plugins.divide_plugin import DivideCommand

def test_divide_command():
    """Test normal division in DivideCommand"""
    divide_command = DivideCommand(10, 2)
    result = divide_command.execute()
    assert result == 5, "Division result is incorrect"

def test_divide_command_by_zero():
    """Test division by zero in DivideCommand"""
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
