import os
import importlib
import logging
from calculator.commands import Command

class Calculator:
    def __init__(self):
        self.history = []  # Maintain a history of executed commands
        self.plugins = {}  # Dictionary to store loaded plugins

        # Log initialization with environment context
        environment = os.getenv("ENVIRONMENT", "development").lower()
        logging.info("Calculator initialized with empty history and plugins in %s environment.", environment)

    def compute(self, command: Command):
        """Execute a command and store it in the history."""
        try:
            result = command.execute()  # Execute the provided command
            self.add_to_history(command)  # Use add_to_history to store the command
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
            # Dynamically import the plugin module
            plugin_module = importlib.import_module(f"calculator.plugins.{plugin_name}")
            # Register and retrieve the command class from the plugin
            command_class = plugin_module.register()
            self.plugins[plugin_name] = command_class
            logging.debug("Successfully loaded plugin: %s", plugin_name)  # Debug log for plugin loading
        except ImportError as e:
            logging.error("Failed to load plugin: %s. Error: %s", plugin_name, e)
            raise ImportError(f"Failed to load plugin: {plugin_name}") from e

    def create_command(self, plugin_name: str, *args):
        """Create and return a command from the loaded plugin."""
        if plugin_name in self.plugins:
            try:
                command = self.plugins[plugin_name](*args)  # Create command with the provided arguments
                logging.debug("Created command %s with arguments %s", plugin_name, args)  # Debug for command creation
                return command
            except Exception as e:
                logging.error("Failed to create command %s with arguments %s. Error: %s", plugin_name, args, e)
                raise
        else:
            error_message = f"Plugin not found: {plugin_name}"
            logging.warning(error_message)
            raise ValueError(error_message)
