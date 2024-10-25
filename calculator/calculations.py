"""
Module for managing a history of calculations and performing operations using Pandas.
"""

import os
import logging
from decimal import Decimal
from typing import List
import pandas as pd
from calculator.calculation import Calculation
from calculator.utils import get_operation_mappings  # Import operation mappings from utils

class Calculations:
    """Manages a history of calculations and supports history storage and retrieval."""

    # Class-level attribute for storing calculation history as a list of Calculation objects
    history: List[Calculation] = []

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
    def save_history(cls, file_name='data/calculation_history.csv'):
        """Save the history of calculations to a CSV file."""
        try:
            # Ensure that the 'data' directory exists
            os.makedirs(os.path.dirname(file_name), exist_ok=True)

            # Load any existing history from the file (if it exists)
            if os.path.exists(file_name):
                existing_data = pd.read_csv(file_name)
            else:
                existing_data = pd.DataFrame(columns=['operation', 'result'])

            # Prepare the new history data to be appended
            new_history_data = []
            for calc in cls.history:
                # Format the operation name correctly
                if hasattr(calc, 'execute'):
                    operation_name = f"{calc.value1} {calc.__class__.__name__.replace('Command', '').lower()} {calc.value2}"
                    result = calc.execute()
                else:
                    operation_name = f"{calc.value1} {calc.operation.__name__} {calc.value2}"
                    result = calc.perform()

                # Append the operation and result to new history data
                new_history_data.append({
                    'operation': operation_name,
                    'result': result
                })

            # Convert the new history to a DataFrame and concatenate with existing data
            new_df = pd.DataFrame(new_history_data)
            full_history = pd.concat([existing_data, new_df], ignore_index=True)

            # Remove duplicates by keeping only the last occurrence of each operation
            full_history.drop_duplicates(inplace=True)

            # Write the full history (existing + new) back to the CSV
            full_history.to_csv(file_name, index=False)
            logging.info("Calculation history saved to %s", file_name)
        except (FileNotFoundError, IOError, pd.errors.EmptyDataError) as e:
            logging.error("Error saving calculation history to %s: %s", file_name, e)

    @classmethod
    def load_history(cls, file_name='data/calculation_history.csv'):
        """Load the history of calculations from a CSV file."""
        operation_mappings = get_operation_mappings()

        if not os.path.exists(file_name):
            logging.warning("No history file found with name '%s'.", file_name)
            return

        try:
            data = pd.read_csv(file_name)
            logging.info("Loaded data from CSV: %s", data)
            cls.history.clear()
            for _, row in data.iterrows():
                operation_split = row['operation'].split(' ')
                value1, operation, value2 = Decimal(operation_split[0]), operation_split[1], Decimal(operation_split[2])
                operation_func = operation_mappings.get(operation)
                if operation_func:
                    calculation = Calculation(value1, value2, operation_func)
                    cls.history.append(calculation)  # Add to history without executing
            logging.info("Calculation history loaded from %s", file_name)
        except (FileNotFoundError, IOError, pd.errors.EmptyDataError) as e:
            logging.error("Error loading calculation history from %s: %s", file_name, e)

    @classmethod
    def delete_history_file(cls, file_name='data/calculation_history.csv'):
        """Delete the calculation history file."""
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                logging.info("File '%s' has been deleted.", file_name)
            else:
                logging.warning("File '%s' does not exist.", file_name)
        except OSError as e:
            logging.error("Error deleting file '%s': %s", file_name, e)
