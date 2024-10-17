"""
This module provides shared fixtures and setup functions for generating test data with Pytest.
"""
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Initialize Faker for generating random data
fake = Faker()

def generate_test_data(num_records):
    """
    Generate random test data for arithmetic operations.
    """
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Generate test data
    for _ in range(num_records):
        value1 = Decimal(fake.random_number(digits=2))
        value2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for divide operations
        if operation_func == divide: # pylint: disable=W0143
            value2 = Decimal('1') if value2 == Decimal('0') else value2

        try:
            expected = operation_func(value1, value2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        except ValueError as ve:
            if str(ve) == "Cannot divide by zero":
                expected = "Cannot divide by zero"
            else:
                raise ve  # Re-raise other value errors not related to divide by zero

        yield value1, value2, operation_name, operation_func, expected


def pytest_addoption(parser):
    """
    Add a command line option to specify the number of records to generate.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")


def pytest_generate_tests(metafunc):
    """
    Generate test parameters dynamically based on the number of records specified.
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"value1", "value2", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))

        # Adjust parameters according to the requested test function
        if 'operation_name' in metafunc.fixturenames:
            modified_parameters = [(value1, value2, op_name, expected) for value1, value2, op_name, _, expected in parameters]
        else:
            modified_parameters = [(value1, value2, op_func, expected) for value1, value2, _, op_func, expected in parameters]

        # Parametrize the test function with the generated data
        metafunc.parametrize("value1,value2,operation,expected", modified_parameters)
