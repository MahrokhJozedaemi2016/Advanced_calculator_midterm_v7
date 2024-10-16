# Advanced Python Calculator

This project is a command-line calculator designed for educational purposes, showcasing clean code, design patterns, and professional practices. It is modular, expandable, and demonstrates best practices in software development.

## Project Overview

The calculator supports core arithmetic operations (addition, subtraction, multiplication, and division), manages a history of calculations, and includes enhanced error handling for invalid inputs and unknown operations. The project now includes a fully interactive REPL (Read-Eval-Print Loop) interface as well as extended logging capabilities configurable by environment variables. It also uses the Faker library for generating random test data and Pandas for loading, saving, clearing, and deleting calculation history.

## Features (Current Step)

- **Basic Arithmetic Operations**:Supports addition, subtraction, multiplication, and division
- **Calculation History**:Stores calculation history and allows retrieval, saving, loading, clearing, and deletion within the REPL interface.
- **Enhanced Logging**:Uses environment-specific logging configurations (e.g., logging only to a file in production and to both console and file in development).
- **Exception Handling**: Manages errors for division by zero, invalid inputs, and unknown operations with appropriate error messages.
- **Faker Library Integration**:Uses Faker to generate random test data for enhanced testing. 
- **Parameterized Testing**: Supports dynamic test case generation with a custom --num_records option for Pytest.
- **Command-Line Interface (REPL)**: Provides an interactive interface for users to input commands, perform calculations, view history, and clear history.
- **Plugin System**: Allows the addition of new commands dynamically, enabling seamless integration of new features without modifying the main codebase.
- **Object-Oriented Structure**: Implements classes for each component, with methods for encapsulation and modularity.
- **Test Coverage**: Unit tests for all implemented functions using Pytest, with at least 100% coverage.
- **Adherence to Design Principles**: Follows SOLID, DRY, GRASP, and Separation of Concerns principles for code organization and maintainability.

## Project Structure

The project is organized into the following directory structure:

Advanced_calculator_midterm/
├── calculator/
│    ├── __init__.py                # Initialization file for Calculator package
│    ├── calculator.py              # Main Calculator class
│    ├── calculation.py             # Represents individual calculations
│    ├── calculations.py            # Manages history of calculations, including save/load features
│    ├── commands.py                # Command classes for arithmetic operations
│    ├── operations.py              # Arithmetic operations functions
│    └── plugins/
│        ├── __init__.py            # Initialization file for plugins
│        ├── add_plugin.py          # Plugin for addition operation
│        ├── subtract_plugin.py     # Plugin for subtraction operation
│        ├── multiply_plugin.py     # Plugin for multiplication operation
│        └── divide_plugin.py       # Plugin for division operation
├── tests/
│    ├── __init__.py
│    ├── conftest.py                # Configuration and fixture file for pytest
│    ├── test_calculator.py         # Tests for the main Calculator class
│    ├── test_calculation.py        # Tests for the Calculation class
│    ├── test_calculations.py       # Tests for the Calculations history management
│    ├── test_main.py               # Tests for main.py functionality
│    ├── test_commands.py           # Tests for command classes
│    ├── test_add_plugin.py         # Tests for add plugin
│    ├── test_subtract_plugin.py    # Tests for subtract plugin
│    ├── test_multiply_plugin.py    # Tests for multiply plugin
│    ├── test_divide_plugin.py      # Tests for divide plugin
│    └── test_operations.py         # Tests for arithmetic operations
├── main.py                         # Entry point for the REPL interface
├── .gitignore                      # Files and folders ignored by Git
├── .pylintrc                       # Configuration file for pylint
├── pytest.ini                      # Configuration file for Pytest
├── README.md                       # Project documentation
└── requirements.txt                # List of project dependencies

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
4. Configure the Environment Variables:
Create a .env file in the project root with environment-specific settings. For example:
```bash
ENVIRONMENT=development
LOG_LEVEL=DEBUG
LOG_FILE=app.log
```

5. **Run Tests**:
    ```bash
    pytest
    ```

6. **Generate Test Records with Pytest**:
    specify the number of records to generate with the `--num_records` option:
    ```bash
    pytest --num_records=100
    ```
7. **Run the Interactive Calculator: Start the REPL interface**:
   ```bash
   python3 main.py
   ```
8. **Calculation History Management Commands**:
Once inside the REPL, use the following commands to manage calculation history:
**.Save_history**: Saves the current history to a CSV file.
**.load_history**: Loads calculation history from a CSV file.
**.clear_history**: Clears the current calculation history.
**.delete_history**: Deletes the history CSV file.

To deactivate the virtual environment, use:
```bash
deactivate


## Environment Variables
This project utilizes environment variables for flexible configuration, which you can set up in a .env file at the project root. The following variables are available:
- ENVIRONMENT: Specifies the environment mode. Options are:

- development – Logs output to both console and file for easy debugging.
- production – Logs output only to a file to avoid cluttering the console.
- LOG_LEVEL: Specifies the logging level (e.g., DEBUG, INFO, WARNING). In development, this is typically set to DEBUG for detailed output, while in production, it might be set to INFO or WARNING to reduce verbosity.
- LOG_FILE: Specifies the file where logs are saved (e.g., app.log). In both environments, logs are written to this file.

## Environment Behavior
- Development Mode: In this mode, logs are displayed in both the console and the specified log file. This helps with debugging by providing real-time feedback on application behavior.
- Production Mode: Logs are recorded only in the specified log file, which keeps the console output clean and is suitable for deployment scenarios.

Be sure to include your .env file in .gitignore to prevent it from being tracked in version control, as it may contain sensitive information.

---

This project is licensed under the MIT License - see the LICENSE file for details.
