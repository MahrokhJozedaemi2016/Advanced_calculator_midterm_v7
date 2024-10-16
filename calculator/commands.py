import logging

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        logging.debug("Executing AddCommand: %s + %s = %s", self.a, self.b, result)
        return result

    def __repr__(self):
        # Include the result in the representation for testing consistency
        return f"Add {self.a} and {self.b} = {self.execute()}"

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        logging.debug("Executing SubtractCommand: %s - %s = %s", self.a, self.b, result)
        return result

    def __repr__(self):
        return f"Subtract {self.a} and {self.b} = {self.execute()}"

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        logging.debug("Executing MultiplyCommand: %s * %s = %s", self.a, self.b, result)
        return result

    def __repr__(self):
        return f"Multiply {self.a} and {self.b} = {self.execute()}"

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            logging.error("Attempted to divide by zero: %s / %s", self.a, self.b)
            raise ValueError("Cannot divide by zero.")
        result = self.a / self.b
        logging.debug("Executing DivideCommand: %s / %s = %s", self.a, self.b, result)
        return result

    def __repr__(self):
        # Ensure divide-by-zero is properly handled in the repr
        try:
            result = self.execute()
            return f"Divide {self.a} by {self.b} = {result}"
        except ValueError:
            return f"Divide {self.a} by {self.b} = Cannot divide by zero"
