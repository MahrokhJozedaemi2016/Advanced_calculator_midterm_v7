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
                # Check if calc is a command object (e.g., AddCommand)
                if hasattr(calc, 'execute'):
                    operation_name = calc.__class__.__name__.replace('Command', '').lower()  # Get 'add', 'subtract', etc.
                    result = calc.execute()
                    value1 = calc.value1
                    value2 = calc.value2
                else:
                    # In case it's a Calculation object
                    operation_name = calc.operation.__name__
                    result = calc.perform()
                    value1 = calc.value1
                    value2 = calc.value2

                # Append the operation to history_data
                history_data.append({
                    'value1': value1,
                    'value2': value2,
                    'operation': operation_name,
                    'result': result
                })

            # Debug print to check history_data before saving
            print(f"Saving the following data to CSV: {history_data}")
            logging.info("Saving the following data to CSV: %s", history_data)

            # Writing data to CSV
            if history_data:
                df = pd.DataFrame(history_data)
                df.to_csv(file_name, index=False)
                print(f"History saved to {file_name}")
                logging.info("Calculation history saved to %s", file_name)
            else:
                print("No data to save.")
                logging.warning("No data available to save.")
        except (FileNotFoundError, IOError, pd.errors.EmptyDataError) as e:
            print(f"Error saving history: {e}")
            logging.error("Error saving calculation history to %s: %s", file_name, e)

    @classmethod
    def load_history(cls, file_name='calculation_history.csv'):
        """Load the history of calculations from a CSV file."""
        operation_mappings = get_operation_mappings()  # Use utility function for operation mappings

        if not os.path.exists(file_name):
            logging.warning("No history file found with name '%s'.", file_name)
            return

        try:
            data = pd.read_csv(file_name)
            print(f"Loaded data from CSV: {data}")  # Debugging line to check CSV content
            cls.history.clear()
            for _, row in data.iterrows():
                operation_func = operation_mappings.get(row['operation'])
                print(f"Mapping operation: {row['operation']} -> {operation_func}")  # Debugging line
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
