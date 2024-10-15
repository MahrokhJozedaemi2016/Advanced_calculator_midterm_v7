from decimal import Decimal
from typing import List
import pandas as pd
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []  # Class-level attribute for storing calculation history

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        # Return a copy of the history to avoid accidental modification
        return cls.history.copy()

    @classmethod
    def clear_history(cls):
        """Completely clear the stored history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        # Simplified return expression for clarity
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        # Use list comprehension to search for calculations with the specified operation
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def save_history(cls, file_name='calculation_history.csv'):
        """Save the history of calculations to a CSV file."""
        df = pd.DataFrame([{
            'a': calc.a,
            'b': calc.b,
            'operation': calc.operation.__name__,
            'result': calc.perform()
        } for calc in cls.history])
        
        df.to_csv(file_name, index=False)
        print(f"Calculation history saved to {file_name}")

    @classmethod
    def load_history(cls, file_name='calculation_history.csv'):
        """Load the history of calculations from a CSV file."""
        try:
            df = pd.read_csv(file_name)
            cls.history = [
                Calculation(Decimal(row['a']), Decimal(row['b']), eval(row['operation']))
                for _, row in df.iterrows()
            ]
            print(f"Calculation history loaded from {file_name}")
        except FileNotFoundError:
            print(f"No history file found with name '{file_name}'.")

    @classmethod
    def delete_history_file(cls, file_name='calculation_history.csv'):
        """Delete the calculation history file."""
        import os
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"File '{file_name}' has been deleted.")
        else:
            print(f"File '{file_name}' does not exist.")
