# Advanced Python Calculator

This project is a command-line calculator designed for educational purposes, showcasing clean code, design patterns, and professional practices. It is structured to be modular and expandable, with features added incrementally to demonstrate best practices in software development. 

## Project Overview

The calculator starts with basic arithmetic functionality, allowing users to perform addition and subtraction. This foundation will be built upon with features such as a command-line REPL interface, a plugin system, logging, environment variables, and data handling with Pandas.

## Features (Current Step)

- **Basic Arithmetic Operations**: Supports addition and subtraction.
- **Test Coverage**: Unit tests for all implemented functions using Pytest.

## Project Structure

The project is organized into the following directory structure:

Advanced_calculator_midterm/ ├── calculator/ │ ├── init.py # Contains the add and subtract functions ├── tests/ │ ├── init.py │ ├── test_calculator.py # Unit tests for calculator functions ├── .gitignore # Files and folders ignored by Git ├── .pylintrc # Configuration file for pylint ├── pytest.ini # Configuration file for Pytest ├── README.md # Project documentation └── requirements.txt # List of project dependencies


## Setup Instructions

To set up and run this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone <git@github.com:MahrokhJozedaemi2016/Advanced_calculator_midterm.git>
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

