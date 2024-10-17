"""
Main module for the interactive calculator application.

This application provides a REPL interface for basic arithmetic operations and
manages calculation history with support for plugins and logging.
"""
import os
import logging
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from calculator.calculator import Calculator
from calculator.calculations import Calculations
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Load environment variables from .env file
load_dotenv()

class CalculatorApp:
    """Application class for the interactive calculator with history management."""

    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "development").lower()
        self.setup_logging()
        self.operation_mappings = {
            'add': AddCommand,
            'subtract': SubtractCommand,
            'multiply': MultiplyCommand,
            'divide': DivideCommand
        }
        logging.info("CalculatorApp initialized in %s environment.", self.environment)

    def setup_logging(self):
        """Set up logging configuration based on environment variables."""
        logging.getLogger().handlers = []
        log_file = os.getenv("LOG_FILE", "app.log")
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.getLevelName(log_level))
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logging.getLogger().addHandler(file_handler)

        if self.environment == "development":
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.getLevelName(log_level))
            console_handler.setFormatter(file_formatter)
            logging.getLogger().addHandler(console_handler)

        logging.getLogger().setLevel(logging.getLevelName(log_level))
        logging.info("Logging configured for %s environment.", self.environment)

    def display_menu(self):
        """Displays the list of available commands."""
        print("\nAvailable commands:")
        print("  add: Add two numbers")
        print("  subtract: Subtract two numbers")
        print("  multiply: Multiply two numbers")
        print("  divide: Divide two numbers")
        print("  history: View calculation history")
        print("  clear_history: Clear calculation history")
        print("  save_history: Save history to a file")
        print("  load_history: Load history from a file")
        print("  delete_history_file: Delete the history file")
        print("  exit: Exit the calculator")

    def is_valid_number(self, value):
        """Checks if the input value is a valid number."""
        try:
            Decimal(value)
            return True
        except InvalidOperation:
            return False

    def calculate_and_store(self, value1, value2, operation_name):
        """Performs the calculation and stores it in history."""
        try:
            value1_decimal, value2_decimal = map(Decimal, [value1, value2])
            command_class = self.operation_mappings.get(operation_name)

            if command_class:
                command = command_class(value1_decimal, value2_decimal)
                calc = Calculator()
                result = calc.compute(command)

                print(f"The result of {operation_name} between {value1} and {value2} is {result}")
                Calculations.add_calculation(command)
                logging.info("Calculation %s with values %s, %s added to history.", operation_name, value1, value2)
            else:
                print(f"Unknown operation: {operation_name}")
                logging.warning("Unknown operation requested: %s", operation_name)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            logging.error("Attempted division by zero in operation %s with values %s, %s", operation_name, value1, value2)
        except InvalidOperation:
            print(f"Invalid number input: {value1} or {value2} is not a valid number.")
            logging.error("Invalid input detected for operation %s: %s, %s", operation_name, value1, value2)
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"An error occurred: {e}")
            logging.error("An unexpected error occurred in operation %s with values %s, %s: %s", operation_name, value1, value2, e)

    def prompt_for_numbers(self, operation_name):
        """Prompts the user to input two numbers for the operation, using LBYL to validate inputs."""
        print(f"\nEnter two numbers for {operation_name}:")
        value1 = input("Enter the first number: ")
        value2 = input("Enter the second number: ")

        # LBYL check: Ensure both inputs are valid numbers before proceeding
        if not self.is_valid_number(value1) or not self.is_valid_number(value2):
            print(f"Invalid input: {value1} or {value2} is not a valid number.")
            logging.error("Invalid input detected: %s, %s", value1, value2)
            return None, None

        return value1, value2

    def interactive_calculator(self):  # pylint: disable=too-many-branches
        """Runs the interactive calculator."""
        print("Welcome to the interactive calculator!")
        print("Type 'menu' to see the available commands or 'exit' to quit.")
        logging.info("Interactive calculator started.")

        while True:
            user_input = input("\nEnter a command: ").strip().lower()

            if user_input == 'exit':
                print("Goodbye!")
                logging.info("Calculator session ended by user.")
                break
            if user_input == 'menu':
                self.display_menu()
            elif user_input == 'history':
                history = Calculations.get_history()
                if history:
                    for idx, operation in enumerate(history, 1):
                        print(f"{idx}: {operation}")
                    logging.info("Displayed calculation history.")
                else:
                    print("No history available.")
                    logging.info("User requested history but none is available.")
            elif user_input == 'clear_history':
                Calculations.clear_history()
                print("Calculation history cleared.")
                logging.info("Calculation history cleared.")
            elif user_input == 'save_history':
                Calculations.save_history()
                logging.info("Calculation history saved to file.")
            elif user_input == 'load_history':
                Calculations.load_history()
                logging.info("Calculation history loaded from file.")
            elif user_input == 'delete_history_file':
                Calculations.delete_history_file()
                logging.info("Calculation history file deleted.")
            elif user_input in self.operation_mappings:
                value1, value2 = self.prompt_for_numbers(user_input)
                if value1 and value2:
                    self.calculate_and_store(value1, value2, user_input)
            else:
                print("Invalid input. Please type 'menu' to see the available commands.")
                logging.warning("Invalid input received: %s", user_input)

if __name__ == "__main__":
    app = CalculatorApp()
    app.interactive_calculator()
