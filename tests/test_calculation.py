"""
This module contains tests for the calculator operations and the Calculation class.

The tests verify the correctness of basic arithmetic operations and the 
functionality of the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, divide
from .test_helpers import setup_test_calculations  # Use relative import


def test_add_operation():
    """
    Test addition operation in the calculator.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    assert calc.perform() == Decimal('15'), "Failed addition operation"


def test_subtract_operation():
    """
    Test subtraction operation in the calculator.
    """
    calc = Calculation(Decimal('20'), Decimal('3'), subtract)
    assert calc.perform() == Decimal('17'), "Failed subtraction operation"


def test_divide_operation():
    """
    Test division operation in the calculator.
    """
    calc = Calculation(Decimal('50'), Decimal('10'), divide)
    assert calc.perform() == Decimal('5'), "Failed division operation"


def test_find_by_operation():
    """
    Test finding calculations in the history by operation type.
    """
    setup_test_calculations()  # Ensure setup happens here and history is cleared

    # Test if the 'add' operation can be found in the history
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "Expected at least one addition operation in history."


def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
