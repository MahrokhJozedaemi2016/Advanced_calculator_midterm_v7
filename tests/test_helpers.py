"""
Helper functions for setting up calculations for tests.
Provides a setup function to initialize common calculations for consistent testing.
"""

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

def setup_test_calculations() -> None:
    """
    Sets up a variety of calculations in the history to support test cases.
    This function clears any existing history and adds sample calculations,
    ensuring a consistent starting state for tests.
    """
    # Clear any existing history
    Calculations.clear_history()

    # Add sample calculations to the history
    calculations = [
        Calculation(Decimal('1'), Decimal('2'), add),
        Calculation(Decimal('3'), Decimal('4'), subtract),
        Calculation(Decimal('5'), Decimal('6'), multiply),
        Calculation(Decimal('8'), Decimal('2'), divide),
    ]

    # Perform and add each calculation to the history
    for calc in calculations:
        calc.perform()
        Calculations.add_calculation(calc)
