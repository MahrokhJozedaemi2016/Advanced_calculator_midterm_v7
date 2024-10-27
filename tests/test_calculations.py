"""
This module contains tests for the Calculations class and basic arithmetic operations.

It verifies the functionality of the Calculations class, including adding calculations to history,
retrieving the latest calculation, and managing the calculation history through saving and loading.
"""

import os
from decimal import Decimal
from unittest import mock
import pytest
import pandas as pd
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add

# Test-specific file path to avoid interfering with the main history file
TEST_HISTORY_FILE_PATH = 'data/test_calculation_history.csv'

@pytest.fixture
def setup_calculations():
    """Fixture to set up calculations and ensure necessary directories for testing."""
    os.makedirs(os.path.dirname(TEST_HISTORY_FILE_PATH), exist_ok=True)
    Calculations.clear_history()
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    yield
    if os.path.exists(TEST_HISTORY_FILE_PATH):
        os.remove(TEST_HISTORY_FILE_PATH)

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
    """Test retrieving the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest is None or (latest.value1 == Decimal('10') and latest.value2 == Decimal('5')), \
        "Latest calculation does not match expected values"

@pytest.mark.usefixtures("setup_calculations")
def test_find_by_operation():
    """Test finding calculations in the history by specific operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "Expected at least one 'add' operation in history"

@pytest.mark.usefixtures("setup_calculations")
def test_save_history():
    """Test saving the calculation history to a file."""
    Calculations.save_history(file_name=TEST_HISTORY_FILE_PATH)
    assert os.path.exists(TEST_HISTORY_FILE_PATH), "History file was not created successfully"

@pytest.mark.usefixtures("setup_calculations")
def test_load_history():
    """Test loading the calculation history from a file."""
    Calculations.save_history(file_name=TEST_HISTORY_FILE_PATH)
    Calculations.clear_history()
    Calculations.load_history(file_name=TEST_HISTORY_FILE_PATH)
    loaded_history = Calculations.get_history()
    assert len(loaded_history) > 0, "Failed to load the history from the file"
    assert loaded_history[0].value1 == Decimal('10') and loaded_history[0].value2 == Decimal('5'), \
        "Loaded calculation does not match the saved calculation"

def test_get_latest_with_empty_history():
    """Test retrieving the latest calculation when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected no latest calculation with an empty history"

@pytest.mark.usefixtures("setup_calculations")
def test_find_by_nonexistent_operation():
    """Test finding calculations with a non-existent operation type in history."""
    non_existent_operations = Calculations.find_by_operation("multiply")
    assert len(non_existent_operations) == 0, "Expected no 'multiply' operations in history"

def test_save_history_ioerror(caplog):
    """Test handling of an IOError when saving history by checking logs."""
    with mock.patch("pandas.DataFrame.to_csv", side_effect=IOError("Mocked IOError for testing")):
        Calculations.save_history(file_name=TEST_HISTORY_FILE_PATH)
    assert any("Error saving calculation history" in record.message for record in caplog.records), \
        "Expected IOError log message not found in caplog"

def test_load_history_empty_data_error(caplog):
    """Test handling of EmptyDataError when loading history by checking logs."""
    # Create an empty file to ensure it exists for the read attempt
    with open(TEST_HISTORY_FILE_PATH, 'a', encoding='utf-8'):
        pass

        # Mock pandas.read_csv to raise an EmptyDataError when reading this file
    with mock.patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError("Mocked EmptyDataError")):
        Calculations.load_history(file_name=TEST_HISTORY_FILE_PATH)

    # Verify that the appropriate error message is logged
    assert any("Error loading calculation history" in record.message for record in caplog.records), \
        "Expected EmptyDataError log message not found in caplog"
