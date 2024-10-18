"""
Helper functions for setting up calculations for tests.
"""
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

def setup_test_calculations():
    """Sets up common calculations for tests to avoid repetition."""
    # Clear history before setting up
    Calculations.clear_history()

    # Add sample calculations
    calc1 = Calculation(Decimal('1'), Decimal('2'), add)
    calc1.perform()
    Calculations.add_calculation(calc1)

    calc2 = Calculation(Decimal('3'), Decimal('4'), subtract)
    calc2.perform()
    Calculations.add_calculation(calc2)
