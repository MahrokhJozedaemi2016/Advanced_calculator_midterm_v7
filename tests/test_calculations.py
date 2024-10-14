'''My Calculator Test'''

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest

# Import Calculation and Calculations classes from the calculator package
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# pytest.fixture is a decorator that marks a function as a fixture
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

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

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "No addition operations found in history"

    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) >= 1, "No subtraction operations found in history"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None 

