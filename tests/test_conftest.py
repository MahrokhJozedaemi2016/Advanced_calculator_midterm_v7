"""
Unit tests for the data generation utility in conftest.
"""

from decimal import Decimal
import pytest
from .conftest import generate_test_data

def test_generate_test_data_division():
    """
    Test generate_test_data for division operation, specifically handling division by zero.
    """
    data_generator = generate_test_data(10)
    for value1, value2, operation_name, _, expected in data_generator:  # Replaced operation_func with _
        assert isinstance(value1, Decimal), "value1 is not of type Decimal"
        assert isinstance(value2, Decimal), "value2 is not of type Decimal"
        assert operation_name in ["add", "subtract", "multiply", "divide"], "Invalid operation name"

        if operation_name == "divide" and value2 == Decimal("0"):
            assert expected in ["ZeroDivisionError", "Cannot divide by zero"], "Division by zero not handled correctly"

def test_all_operations_present():
    """
    Ensure that each operation (add, subtract, multiply, divide) appears at least once
    in the generated test data set of a larger size (e.g., 20 records).
    """
    num_records = 20
    operations_seen = {"add": False, "subtract": False, "multiply": False, "divide": False}

    for _, _, operation_name, _, _ in generate_test_data(num_records):
        if operation_name in operations_seen:
            operations_seen[operation_name] = True

    assert all(operations_seen.values()), "Not all operations were generated at least once"

@pytest.mark.parametrize("num_records", [1, 5, 10])
def test_record_count(num_records):
    """
    Verify that generate_test_data generates the correct number of records.
    """
    data = list(generate_test_data(num_records))
    assert len(data) == num_records, f"Expected {num_records} records, but got {len(data)}"
