"""
Unit tests for the SubtractCommand plugin.
These tests ensure the correctness of the SubtractCommand's execute method
and the register function used for dynamic plugin loading.
"""
from calculator.plugins.subtract_plugin import SubtractCommand, register

def test_subtract_command_execute():
    """Test the execute method of SubtractCommand"""
    subtract_command = SubtractCommand(10, 4)
    result = subtract_command.execute()
    assert result == 6, "SubtractCommand execute method failed"

def test_subtract_command_register():
    """Test the register function for SubtractCommand"""
    command_class = register()
    assert command_class == SubtractCommand, "SubtractCommand register function failed"
