"""
This module contains tests for the Calculator class and its associated commands.
It tests basic arithmetic operations, plugin functionality, and design patterns.
"""

import pytest
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Suppress pylint warnings for redefined fixture and unused arguments
# pylint: disable=redefined-outer-name, unused-argument

@pytest.fixture(scope="module")
def calc():
    """Fixture to set up a calculator instance before each test"""
    return Calculator()

def test_add_command(calc):
    """Test addition command in the calculator"""
    add_command = AddCommand(10, 5)
    result = calc.compute(add_command)
    assert result == 15, "Addition result is incorrect"

def test_subtract_command(calc):
    """Test subtraction command in the calculator"""
    sub_command = SubtractCommand(10, 5)
    result = calc.compute(sub_command)
    assert result == 5, "Subtraction result is incorrect"

def test_multiply_command(calc):
    """Test multiplication command in the calculator"""
    multiply_command = MultiplyCommand(10, 5)
    result = calc.compute(multiply_command)
    assert result == 50, "Multiplication result is incorrect"

def test_divide_command(calc):
    """Test division command in the calculator"""
    divide_command = DivideCommand(10, 5)
    result = calc.compute(divide_command)
    assert result == 2, "Division result is incorrect"

def test_divide_by_zero(calc):
    """Test division by zero, expecting a ValueError"""
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.compute(divide_command)

def test_load_plugin_success():
    """Test loading a plugin successfully"""
    calc = Calculator()
    calc.load_plugin('add_plugin')
    assert 'add_plugin' in calc.plugins
    assert calc.plugins['add_plugin'] is not None

def test_load_plugin_failure():
    """Test failure case for loading a non-existent plugin"""
    calc = Calculator()
    with pytest.raises(ImportError, match="Failed to load plugin: non_existent_plugin"):
        calc.load_plugin('non_existent_plugin')

def test_create_command_success():
    """Test creating a command from a loaded plugin"""
    calc = Calculator()
    calc.load_plugin('add_plugin')
    command = calc.create_command('add_plugin', 2, 3)
    assert command is not None
    assert command.execute() == 5

def test_create_command_failure():
    """Test failure case for creating a command from a non-loaded plugin"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Plugin not found: non_existent_plugin"):
        calc.create_command('non_existent_plugin', 2, 3)

def test_singleton_instance():
    """Test singleton pattern to ensure only one instance of Calculator exists"""
    calc1 = Calculator()
    calc2 = Calculator()
    assert calc1 is calc2, "Calculator instances are not the same; Singleton pattern not implemented correctly."

def test_divide_command_default(calc):
    """Test default division in the calculator"""
    divide_command = DivideCommand(10, 3)
    result = divide_command.execute()
    assert result == pytest.approx(3.3333, 0.0001), "Default division result is incorrect"

def test_divide_command_integer(calc):
    """Test integer division strategy in the calculator"""
    divide_command = DivideCommand(10, 3, strategy=DivideCommand.integer_division)
    result = divide_command.execute()
    assert result == 3, "Integer division result is incorrect"

def test_divide_by_zero_integer(calc):
    """Test integer division by zero, expecting a ValueError"""
    divide_command = DivideCommand(10, 0, strategy=DivideCommand.integer_division)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
