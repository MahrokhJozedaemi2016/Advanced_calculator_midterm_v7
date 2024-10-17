"""
Calculator module to perform operations using a dynamic plugin system and maintain a history of calculations.
"""
import os
import importlib
import logging
from calculator.commands import Command, DivideCommand

class Calculator:
    """
    The Calculator class handles the execution of arithmetic operations and manages plugins
    for dynamically adding new commands. It also maintains a history of executed commands.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'history'):
            self.history = []  # Maintain a history of executed commands
            self.plugins = {}  # Dictionary to store loaded plugins
            environment = os.getenv("ENVIRONMENT", "development").lower()
            logging.info("Calculator initialized with empty history and plugins in %s environment.", environment)

    def compute(self, command: Command):
        """Execute a command and store it in the history."""
        try:
            result = command.execute()  # Execute the provided command
            self.add_to_history(command)  # Store the command in history
            logging.info("Executed command: %s with result: %s", command, result)
            return result  # Return the result of the command
        except Exception as e:
            logging.error("Failed to execute command: %s due to error: %s", command, e)
            raise

    def add_to_history(self, command: Command):
        """Add a command to the history and log at DEBUG level."""
        self.history.append(command)
        logging.debug("Added command %s to history.", command)

    def load_plugin(self, plugin_name: str):
        """Dynamically load a plugin by its name from the plugins folder."""
        try:
            plugin_module = importlib.import_module(f"calculator.plugins.{plugin_name}")
            command_class = plugin_module.register()
            self.plugins[plugin_name] = command_class
            logging.debug("Successfully loaded plugin: %s", plugin_name)
        except ImportError as e:
            logging.error("Failed to load plugin: %s. Error: %s", plugin_name, e)
            raise ImportError(f"Failed to load plugin: {plugin_name}") from e

    def create_command(self, plugin_name: str, *args, strategy=None):
        """Create and return a command from the loaded plugin with an optional strategy for division."""
        if plugin_name == 'divide':
            command = DivideCommand(*args, strategy=strategy)
            logging.debug("Created DivideCommand with strategy %s and arguments %s", strategy, args)
            return command

        if plugin_name in self.plugins:
            try:
                command = self.plugins[plugin_name](*args)  # Create command with the provided arguments
                logging.debug("Created command %s with arguments %s", plugin_name, args)
                return command
            except Exception as e:
                logging.error("Failed to create command %s with arguments %s. Error: %s", plugin_name, args, e)
                raise
        else:
            error_message = f"Plugin not found: {plugin_name}"
            logging.warning(error_message)
            raise ValueError(error_message)
