# Advanced Python Calculator

This project is a command-line calculator designed for educational purposes, showcasing clean code, design patterns, and professional practices. It is structured to be modular and expandable, with features added incrementally to demonstrate best practices in software development.

## Project Overview

The calculator now supports core arithmetic operations (addition, subtraction, multiplication, and division) and manages a history of calculations. Exception handling has been added for division by zero, and the project adheres to object-oriented principles and design patterns.

## Features (Current Step)

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Calculation History**: Stores a history of calculations, allowing retrieval and search by operation type.
- **Exception Handling**: Handles division by zero with appropriate error messages.
- **Object-Oriented Structure**: Implements classes for each component, with methods for encapsulation and modularity.
- **Test Coverage**: Unit tests for all implemented functions using Pytest, with at least 100% coverage.
- **Adherence to Design Principles**: Follows SOLID, DRY, GRASP, and Separation of Concerns principles for code organization and maintainability.

## Project Structure

The project is organized into the following directory structure:

Advanced_calculator_midterm/ ├── calculator/ │ ├── init.py # Main Calculator class │ ├── calculation.py # Represents individual calculations │ ├── calculations.py # Manages history of calculations │ ├── operations.py # Arithmetic operations functions ├── tests/ │ ├── init.py │ ├── test_calculator.py # Tests for the main Calculator class │ ├── test_calculation.py # Tests for the Calculation class │ ├── test_calculations.py # Tests for the Calculations history management │ ├── test_operations.py # Tests for arithmetic operations ├── .gitignore # Files and folders ignored by Git ├── .pylintrc # Configuration file for pylint ├── pytest.ini # Configuration file for Pytest ├── README.md # Project documentation └── requirements.txt # List of project dependencies


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

To deactivate the virtual environment, use:
```bash
deactivate


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

