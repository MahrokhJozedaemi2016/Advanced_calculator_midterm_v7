from decimal import Decimal
from typing import List
import pandas as pd
import os
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculations:
    history: List[Calculation] = []  # Class-level attribute for storing calculation history

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        return cls.history.copy()

    @classmethod
    def clear_history(cls):
        """Completely clear the stored history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def save_history(cls, file_name='calculation_history.csv'):
        """Save the history of calculations to a CSV file."""
        df = pd.DataFrame([{
            'a': str(calc.a),
            'b': str(calc.b),
            'operation': calc.operation.__name__,
            'result': str(calc.perform())
        } for calc in cls.history])
        
        df.to_csv(file_name, index=False)
        print(f"Calculation history saved to {file_name}")

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
            print(f"No history file found with name '{file_name}'.")
            return

        df = pd.read_csv(file_name)
        cls.history.clear()
        for _, row in df.iterrows():
            operation_func = operation_mappings.get(row['operation'])
            if operation_func:
                calculation = Calculation(Decimal(row['a']), Decimal(row['b']), operation_func)
                cls.history.append(calculation)
        print(f"Calculation history loaded from {file_name}")

    @classmethod
    def delete_history_file(cls, file_name='calculation_history.csv'):
        """Delete the calculation history file."""
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"File '{file_name}' has been deleted.")
        else:
            print(f"File '{file_name}' does not exist.")
