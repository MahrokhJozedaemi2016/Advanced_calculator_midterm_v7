"""
This module contains tests for the Calculations class and basic arithmetic operations.

It verifies the functionality of the Calculations class, including adding calculations to history,
retrieving the latest calculation, and managing the calculation history through saving, loading, and deleting.
"""

import os
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add

# File path for testing save, load, and delete operations
HISTORY_FILE_PATH = 'data/calculation_history.csv'

@pytest.fixture
def setup_calculations():
    """Set up calculations and ensure necessary directories exist for testing."""
    # Ensure 'data/' directory exists
    os.makedirs(os.path.dirname(HISTORY_FILE_PATH), exist_ok=True)

    # Clear any existing history and set up test data
    Calculations.clear_history()

    # Set up exact test data (e.g., 10 add 5)
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)

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
    assert len(Calculations.get_history()) == 0, "Expected history to be empty after clearing"


def test_clear_history():
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared successfully"


def test_get_latest():
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest is None or (latest.value1 == Decimal('10') and latest.value2 == Decimal('5')), \
        "Latest calculation does not match expected values"


@pytest.mark.usefixtures("setup_calculations")
def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "Expected at least one 'add' operation in history"


@pytest.mark.usefixtures("setup_calculations")
def test_save_history():
    """Test saving the calculation history to a file."""
    Calculations.save_history(file_name=HISTORY_FILE_PATH)
    assert os.path.exists(HISTORY_FILE_PATH), "History file was not created successfully"


@pytest.mark.usefixtures("setup_calculations")
def test_load_history():
    """Test loading the calculation history from a file."""
    # Save current history
    Calculations.save_history(file_name=HISTORY_FILE_PATH)
    assert os.path.exists(HISTORY_FILE_PATH), "File was not saved correctly."

    # Clear history and load from file
    Calculations.clear_history()
    Calculations.load_history(file_name=HISTORY_FILE_PATH)
    loaded_history = Calculations.get_history()

    # Check if history was loaded correctly
    assert len(loaded_history) > 0, "Failed to load the history from the file"

    # Ensure the loaded values match the saved test data (10 and 5)
    assert loaded_history[0].value1 == Decimal('10') and loaded_history[0].value2 == Decimal('5'), \
        "Loaded calculation does not match the saved calculation"


@pytest.mark.usefixtures("setup_calculations")
def test_delete_history_file():
    """Test deleting the history file."""
    Calculations.save_history(file_name=HISTORY_FILE_PATH)
    Calculations.delete_history_file(file_name=HISTORY_FILE_PATH)
    assert not os.path.exists(HISTORY_FILE_PATH), "Failed to delete the history file"


def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected no latest calculation with an empty history"
