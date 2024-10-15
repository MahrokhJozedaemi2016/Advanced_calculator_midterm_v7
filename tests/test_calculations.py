'''My Calculator Test'''

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
import os

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
    assert len(Calculations.get_history()) == 0, "History does not contain number of calculations"

def test_clear_history():
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest():
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest() 
    if latest is None:
        assert latest is None
    else:
        assert latest.a == Decimal('20') and latest.b == Decimal('3')

@pytest.mark.usefixtures("setup_calculations")
def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    # Adding operations to the history
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
    assert Calculations.get_latest() is None

def test_save_history(setup_calculations):
    """Test saving the calculation history to a file."""
    Calculations.save_history(file_path=history_file_path)
    assert os.path.exists(history_file_path), "Failed to save the history to a file"

def test_load_history():
    """Test loading the calculation history from a file."""
    # Clear current history and save a new one
    Calculations.clear_history()
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    Calculations.save_history(file_path=history_file_path)

    # Clear history and load from the file
    Calculations.clear_history()
    Calculations.load_history(file_path=history_file_path)
    assert len(Calculations.get_history()) > 0, "Failed to load the history from the file"

def test_delete_history_file():
    """Test deleting the history file."""
    # Create a file to delete
    Calculations.save_history(file_path=history_file_path)
    Calculations.delete_history_file(file_path=history_file_path)
    assert not os.path.exists(history_file_path), "Failed to delete the history file"
