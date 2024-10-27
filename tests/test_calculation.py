"""
This module contains tests for the calculator operations and the Calculation class.

The tests verify the correctness of basic arithmetic operations and the 
functionality of the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


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


def test_multiply_operation():
    """
    Test multiplication operation in the calculator.
    """
    calc = Calculation(Decimal('7'), Decimal('8'), multiply)
    assert calc.perform() == Decimal('56'), "Failed multiplication operation"


def test_invalid_operation():
    """
    Test handling of an invalid operation (None) to ensure error handling works.
    """
    with pytest.raises(TypeError):
        calc = Calculation(Decimal('10'), Decimal('5'), None)  # None as an invalid operation
        calc.perform()


def test_alternative_constructor():
    """
    Test the alternative 'create' method to ensure it initializes the Calculation correctly.
    """
    calc = Calculation.create(Decimal('15'), Decimal('5'), add)
    assert isinstance(calc, Calculation), "Failed to create Calculation instance with alternative constructor"
    assert calc.perform() == Decimal('20'), "Failed addition using alternative constructor"


def test_calculation_repr():
    """
    Test the __repr__ method for a readable string representation of the calculation.
    """
    calc = Calculation(Decimal('12'), Decimal('4'), subtract)
    assert repr(calc) == "Calculation(12, 4, subtract)", "Failed string representation for Calculation"
