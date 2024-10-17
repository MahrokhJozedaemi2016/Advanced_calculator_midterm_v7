"""
This module contains tests for the Calculations class and basic arithmetic operations.

It verifies the functionality of the Calculations class, including adding calculations to history,
retrieving the latest calculation, and managing the calculation history through saving, loading, and deleting.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import os
import pytest

# Import Calculation and Calculations classes from the calculator package
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# File path for testing save, load, and delete operations
history_file_path = 'calculation_history.csv'

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))
    yield
    # Cleanup: remove the file after test completes
    if os.path.exists(history_file_path):
        os.remove(history_file_path)

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history():
    """Test retrieving the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History does not contain the expected number of calculations"

def test_clear_history():
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared successfully"

def test_get_latest():
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    if latest is None:
        assert latest is None
    else:
        assert latest.value1 == Decimal('20') and latest.value2 == Decimal('3'), \
            "Latest calculation does not match expected values"

@pytest.mark.usefixtures("setup_calculations")
def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    calc1 = Calculation(Decimal('1'), Decimal('2'), add)
    calc1.perform()
    Calculations.add_calculation(calc1)

    calc2 = Calculation(Decimal('3'), Decimal('4'), subtract)
    calc2.perform()
    Calculations.add_calculation(calc2)

    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "No 'add' operations found in the history"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected no latest calculation with empty history"

@pytest.mark.usefixtures("setup_calculations")
def test_save_history():
    """Test saving the calculation history to a file."""
    Calculations.save_history(file_name=history_file_path)
    assert os.path.exists(history_file_path), "Failed to save the history to a file"

def test_load_history():
    """Test loading the calculation history from a file."""
    # Clear current history and save a new one
    Calculations.clear_history()
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    Calculations.save_history(file_name=history_file_path)

    # Clear history and load from the file
    Calculations.clear_history()
    Calculations.load_history(file_name=history_file_path)
    loaded_history = Calculations.get_history()
    assert len(loaded_history) > 0, "Failed to load the history from the file"
    assert loaded_history[0].value1 == Decimal('10') and loaded_history[0].value2 == Decimal('5'), \
        "Loaded calculation does not match the saved calculation"

def test_delete_history_file():
    """Test deleting the history file."""
    # Create a file to delete
    Calculations.save_history(file_name=history_file_path)
    Calculations.delete_history_file(file_name=history_file_path)
    assert not os.path.exists(history_file_path), "Failed to delete the history file"
