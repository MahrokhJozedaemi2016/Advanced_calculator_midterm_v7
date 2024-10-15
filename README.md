# Advanced Python Calculator

This project is a command-line calculator designed for educational purposes, showcasing clean code, design patterns, and professional practices. It is structured to be modular and expandable, with features added incrementally to demonstrate best practices in software development.

## Project Overview

The calculator now supports core arithmetic operations (addition, subtraction, multiplication, and division), manages a history of calculations, and includes enhanced error handling for invalid inputs and unknown operations. A new main.py entry point provides a user-friendly command-line interface. Additionally, the Faker library has been integrated for generating random test data, enabling more robust and varied testing.

## Features (Current Step)

- **Basic Arithmetic Operations**:Supports addition, subtraction, multiplication, and division.
- **Calculation History**: Stores a history of calculations, allowing retrieval and search by operation type.
- **Exception Handling**: Handles division by zero, invalid inputs, and unknown operations with appropriate error messages.
- **Faker Library Integration**: Uses Faker to generate random test data for improved testing.
- **Parameterized Testing**: Supports dynamic test case generation with a custom `--num_records` option for Pytest.
- **Command-Line Interface (REPL)**: Provides an interactive interface for users to input commands, perform calculations, view history, and clear history.
- **Plugin System**: Allows the addition of new commands dynamically, enabling seamless integration of new features without modifying the main codebase.
- **Object-Oriented Structure**: Implements classes for each component, with methods for encapsulation and modularity.
- **Test Coverage**: Unit tests for all implemented functions using Pytest, with at least 100% coverage.
- **Adherence to Design Principles**: Follows SOLID, DRY, GRASP, and Separation of Concerns principles for code organization and maintainability.

## Project Structure

The project is organized into the following directory structure:

Advanced_calculator_midterm/
  ├── calculator/
  │    ├── __init__.py # Initialization file for Calculator package
  │    ├── calculator.py # Main Calculator class
  │    ├── calculation.py # Represents individual calculations
  │    ├── calculations.py # Manages history of calculations
  │    ├── commands.py # Command classes for arithmetic operations
  │    ├── operations.py # Arithmetic operations functions
  │    └── plugins/
  │        ├── __init__.py # Initialization file for plugins
  │        ├── add_plugin.py # Plugin for addition operation
  │        ├── subtract_plugin.py # Plugin for subtraction operation
  │        ├── multiply_plugin.py # Plugin for multiplication operation
  │        └── divide_plugin.py # Plugin for division operation
  ├── tests/
  │    ├── __init__.py
  │    ├── conftest.py # Configuration and fixture file for pytest
  │    ├── test_calculator.py # Tests for the main Calculator class
  │    ├── test_calculation.py # Tests for the Calculation class
  │    ├── test_calculations.py # Tests for the Calculations history management
  │    ├── test_main.py # Tests for main.py functionality
  │    ├── test_commands.py # Tests for command classes
  │    ├── test_add_plugin.py # Tests for add plugin
  │    ├── test_subtract_plugin.py # Tests for subtract plugin
  │    ├── test_multiply_plugin.py # Tests for multiply plugin
  │    ├── test_divide_plugin.py # Tests for divide plugin
  │    └── test_operations.py # Tests for arithmetic operations
  ├── main.py # Entry point for the REPL interface
  ├── .gitignore # Files and folders ignored by Git
  ├── .pylintrc # Configuration file for pylint
  ├── pytest.ini # Configuration file for Pytest
  ├── README.md # Project documentation
  └── requirements.txt # List of project dependencies

## Setup Instructions

To set up and run this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone git@github.com:MahrokhJozedaemi2016/Advanced_calculator_midterm.git
    cd Advanced_calculator_midterm
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Tests**:
    ```bash
    pytest
    ```

5. **Generate Test Records with Pytest**:
    You can specify the number of records to generate with the `--num_records` option:
    ```bash
    pytest --num_records=100
    ```
6. **Run the Interactive Calculator: Start the REPL interface**:
   ```bash
   python3 main.py
   ```

To deactivate the virtual environment, use:
```bash
deactivate


---

This project is licensed under the MIT License - see the LICENSE file for details.
