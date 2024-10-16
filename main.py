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
        # Remove existing logging handlers
        logging.getLogger().handlers = []

        # Define logging file and level
        log_file = os.getenv("LOG_FILE", "app.log")
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        # File Handler for all environments
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.getLevelName(log_level))
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logging.getLogger().addHandler(file_handler)

        # Console Handler (only for development)
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

    def calculate_and_store(self, a, b, operation_name):
        """Performs the calculation and stores it in history."""
        logging.debug("Starting calculation with inputs: %s, %s for operation %s", a, b, operation_name)
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            CommandClass = self.operation_mappings.get(operation_name)

            if CommandClass:
                command = CommandClass(a_decimal, b_decimal)
                calc = Calculator()
                result = calc.compute(command)
                
                print(f"The result of {operation_name} between {a} and {b} is {result}")
                Calculations.add_calculation(command)
                logging.info("Calculation %s with values %s, %s added to history.", operation_name, a, b)
            else:
                print(f"Unknown operation: {operation_name}")
                logging.warning("Unknown operation requested: %s", operation_name)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            logging.error("Attempted division by zero in operation %s with values %s, %s", operation_name, a, b)
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
            logging.error("Invalid input detected for operation %s: %s, %s", operation_name, a, b)
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error("An unexpected error occurred in operation %s with values %s, %s: %s", operation_name, a, b, e)

    def prompt_for_numbers(self, operation_name):
        """Prompts the user to input two numbers for the operation."""
        print(f"\nEnter two numbers for {operation_name}:")
        try:
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            return a, b
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error in number prompt: {e}")
            return None, None

    def interactive_calculator(self):
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
            elif user_input == 'menu':
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
                a, b = self.prompt_for_numbers(user_input)
                if a and b:
                    self.calculate_and_store(a, b, user_input)
            else:
                print("Invalid input. Please type 'menu' to see the available commands.")
                logging.warning(f"Invalid input received: {user_input}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.interactive_calculator()
