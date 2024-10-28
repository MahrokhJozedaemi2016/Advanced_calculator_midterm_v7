"""
This module contains tests for the CalculatorApp class in the main application file.
It tests various functions to verify their expected output.
"""

from decimal import Decimal
from unittest.mock import patch
import pytest
from main import CalculatorApp
from calculator.calculations import Calculations
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Apply a fixture to mock save_history for all tests
@pytest.fixture(autouse=True)
def mock_save_history():
    """Fixture to automatically mock save_history to prevent file writes during tests."""
    with patch.object(Calculations, 'save_history', return_value=None):
        yield

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of add between 5 and 3 is 8"),
    ("10", "2", 'subtract', "The result of subtract between 10 and 2 is 8"),
    ("4", "5", 'multiply', "The result of multiply between 4 and 5 is 20"),
    ("20", "4", 'divide', "The result of divide between 20 and 4 is 5"),
    ("1", "1", 'divide', "The result of divide between 1 and 1 is 1"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero."),
    ("9", "3", 'unknown', "Unknown operation: unknown."),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_store(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_store function with various inputs."""
    app = CalculatorApp()
    app.calculate_and_store(a_string, b_string, operation_string)
    captured = capsys.readouterr().out.strip().rstrip(".")
    assert captured == expected_string.rstrip(".")

def test_display_menu(capsys):
    """Test the display_menu function outputs the correct menu."""
    app = CalculatorApp()
    app.display_menu()
    captured = capsys.readouterr().out.strip()
    expected_menu = (
        "Available commands:\n"
        "  add: Add two numbers\n"
        "  subtract: Subtract two numbers\n"
        "  multiply: Multiply two numbers\n"
        "  divide: Divide two numbers\n"
        "  history: View calculation history\n"
        "  clear_history: Clear calculation history\n"
        "  save_history: Save history to a file\n"
        "  load_history: Load history from a file\n"
        "  exit: Exit the calculator"
    )
    assert captured == expected_menu

@pytest.mark.parametrize("value, expected", [
    ("5", True),
    ("3.14", True),
    ("-7", True),
    ("a", False),
    ("5b", False)
])
def test_is_valid_number(value, expected):
    """Test the is_valid_number function for valid and invalid inputs."""
    app = CalculatorApp()
    assert app.is_valid_number(value) == expected

def test_prompt_for_numbers_valid(mocker):
    """Test prompt_for_numbers with valid inputs."""
    app = CalculatorApp()
    mocker.patch("builtins.input", side_effect=["3", "4"])
    value1, value2 = app.prompt_for_numbers("add")
    assert value1 == "3" and value2 == "4"

def test_prompt_for_numbers_invalid(mocker, capsys):
    """Test prompt_for_numbers with invalid inputs."""
    app = CalculatorApp()
    mocker.patch("builtins.input", side_effect=["a", "4"])
    value1, value2 = app.prompt_for_numbers("add")
    captured = capsys.readouterr().out.strip()
    assert value1 is None and value2 is None
    assert "Invalid input: a or 4 is not a valid number." in captured

def test_interactive_calculator_exit(mocker, capsys):
    """Test the interactive_calculator method for handling 'exit' command."""
    app = CalculatorApp()
    mocker.patch("builtins.input", side_effect=["exit"])
    app.interactive_calculator()
    captured = capsys.readouterr().out.strip()
    assert "Goodbye!" in captured

def test_clear_history(mocker, capsys):
    """Test the clear_history command clears the history."""
    app = CalculatorApp()
    mocker.patch.object(Calculations, 'clear_history')
    app.clear_history()
    captured = capsys.readouterr().out.strip()
    assert "Calculation history cleared." in captured

def test_save_history(mocker, capsys):
    """Test the save_history command."""
    app = CalculatorApp()
    mocker.patch.object(Calculations, 'save_history')
    app.save_history()
    captured = capsys.readouterr().out.strip()
    assert "Calculation history saved to file." in captured

def test_load_history(mocker, capsys):
    """Test the load_history command."""
    app = CalculatorApp()
    mocker.patch.object(Calculations, 'load_history')
    app.load_history()
    captured = capsys.readouterr().out.strip()
    assert "Calculation history loaded from file." in captured

def test_display_history(mocker, capsys):
    """Test that history displays correctly after calculations are stored."""
    app = CalculatorApp()
    mocker.patch.object(Calculations, 'get_history', return_value=[
        AddCommand(Decimal("5"), Decimal("3")),
        SubtractCommand(Decimal("10"), Decimal("2")),
        MultiplyCommand(Decimal("4"), Decimal("5")),
        DivideCommand(Decimal("20"), Decimal("4")),
    ])
    app.display_history()
    captured = capsys.readouterr().out.strip()
    assert "5 add 3 = 8" in captured
    assert "10 subtract 2 = 8" in captured
    assert "4 multiply 5 = 20" in captured
    assert "20 divide 4 = 5" in captured
