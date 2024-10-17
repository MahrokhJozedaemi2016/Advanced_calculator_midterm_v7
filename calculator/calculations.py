"""
Module for managing a history of calculations and performing operations using Pandas.
"""

import os
import logging
from decimal import Decimal
from typing import List
import pandas as pd
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculations:
    """Manages a history of calculations and supports history storage and retrieval."""

    history: List[Calculation] = []  # Class-level attribute for storing calculation history

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        logging.debug("Adding calculation to history: %s", calculation)
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        logging.info("Retrieving the entire calculation history.")
        return cls.history.copy()

    @classmethod
    def clear_history(cls):
        """Completely clear the stored history of calculations."""
        logging.info("Clearing the calculation history.")
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        if cls.history:
            logging.info("Retrieving the latest calculation.")
            return cls.history[-1]
        logging.warning("No calculations in history to retrieve.")
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        logging.info("Finding calculations with operation '%s'.", operation_name)
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def save_history(cls, file_name='calculation_history.csv'):
        """Save the history of calculations to a CSV file."""
        try:
            history_data = []
            for calc in cls.history:
                if hasattr(calc, 'execute'):
                    result = calc.execute()
                    operation_name = calc.__class__.__name__.replace('Command', '').lower()
                elif hasattr(calc, 'perform'):
                    result = calc.perform()
                    operation_name = calc.operation.__name__
                else:
                    result = None
                    operation_name = "unknown"

                history_data.append({
                    'value1': calc.value1,
                    'value2': calc.value2,
                    'operation': operation_name,
                    'result': result
                })

            df = pd.DataFrame(history_data)
            df.to_csv(file_name, index=False)
            logging.info("Calculation history saved to %s", file_name)
        except (FileNotFoundError, IOError, pd.errors.EmptyDataError) as e:
            logging.error("Error saving calculation history to %s: %s", file_name, e)

    @classmethod
    def load_history(cls, file_name='calculation_history.csv'):
        """Load the history of calculations from a CSV file."""
        operation_mappings = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        if not os.path.exists(file_name):
            logging.warning("No history file found with name '%s'.", file_name)
            return

        try:
            data = pd.read_csv(file_name)
            cls.history.clear()
            for _, row in data.iterrows():
                operation_func = operation_mappings.get(row['operation'])
                if operation_func:
                    calculation = Calculation(Decimal(row['value1']), Decimal(row['value2']), operation_func)
                    cls.history.append(calculation)
            logging.info("Calculation history loaded from %s", file_name)
        except (FileNotFoundError, IOError, pd.errors.EmptyDataError) as e:
            logging.error("Error loading calculation history from %s: %s", file_name, e)

    @classmethod
    def delete_history_file(cls, file_name='calculation_history.csv'):
        """Delete the calculation history file."""
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                logging.info("File '%s' has been deleted.", file_name)
            else:
                logging.warning("File '%s' does not exist.", file_name)
        except OSError as e:
            logging.error("Error deleting file '%s': %s", file_name, e)
