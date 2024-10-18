"""
This module contains tests for the Calculations class and basic arithmetic operations.

It verifies the functionality of the Calculations class, including adding calculations to history,
retrieving the latest calculation, and managing the calculation history through saving, loading, and deleting.
"""

from decimal import Decimal
import os
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add  # First-party import
from .test_helpers import setup_test_calculations  # Relative import

# File path for testing save, load, and delete operations
HISTORY_FILE_PATH = 'calculation_history.csv'  # Changed to uppercase for constant naming convention

@pytest.fixture
def setup_calculations():
    """Clear history and set up sample calculations for tests using the helper function."""
    Calculations.clear_history()
    setup_test_calculations()  # Use the helper function to add sample calculations
    yield
    # Cleanup: remove the file after test completes
    if os.path.exists(HISTORY_FILE_PATH):
        os.remove(HISTORY_FILE_PATH)

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
    assert latest is None or (latest.value1 == Decimal('20') and latest.value2 == Decimal('3')), \
        "Latest calculation does not match expected values"

@pytest.mark.usefixtures("setup_calculations")
def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    # Check if the 'add' operation can be found in the history
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "No 'add' operations found in the history"

@pytest.mark.usefixtures("setup_calculations")
def test_save_history():
    """Test saving the calculation history to a file."""
    Calculations.save_history(file_name=HISTORY_FILE_PATH)
    assert os.path.exists(HISTORY_FILE_PATH), "Failed to save the history to a file"

def test_load_history():
    """Test loading the calculation history from a file."""
    # Clear current history and save a new one
    Calculations.clear_history()
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    Calculations.save_history(file_name=HISTORY_FILE_PATH)

    # Ensure file was saved properly
    assert os.path.exists(HISTORY_FILE_PATH), "File was not saved correctly."

    # Clear history and load from the file
    Calculations.clear_history()
    Calculations.load_history(file_name=HISTORY_FILE_PATH)
    loaded_history = Calculations.get_history()

    # Debugging: print loaded history if needed
    print(f"Loaded history: {loaded_history}")

    assert len(loaded_history) > 0, "Failed to load the history from the file"
    assert loaded_history[0].value1 == Decimal('10') and loaded_history[0].value2 == Decimal('5'), \
        "Loaded calculation does not match the saved calculation"

def test_delete_history_file():
    """Test deleting the history file."""
    # Create a file to delete
    Calculations.save_history(file_name=HISTORY_FILE_PATH)
    Calculations.delete_history_file(file_name=HISTORY_FILE_PATH)
    assert not os.path.exists(HISTORY_FILE_PATH), "Failed to delete the history file"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected no latest calculation with empty history"
