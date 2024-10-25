## Implementation Status

The project currently supports core arithmetic operations (addition, subtraction, multiplication, and division), manages a robust history of calculations, and provides a user-friendly REPL command-line interface with error handling. Recent updates include Advanced Data Handling with Pandas, which enables efficient reading from and writing to CSV files for calculation history management. This addition allows users to load, save, clear, and delete history records in an optimized and streamlined manner. The project’s architecture follows fundamental design principles, such as SOLID, DRY, and Separation of Concerns, ensuring scalability and maintainability.
Additional design patterns and software development practices, such as PEP 8 compliance, parameterized testing, and logging based on environment variables, have been integrated to enhance functionality, robustness, and code quality.

### Design Patterns Applied So Far

1. **Command Pattern**:  
- **Purpose**:  Encapsulates each arithmetic operation (Add, Subtract, Multiply, Divide) as a command, making it easy to add or modify operations.  
- **.Aplication**: Each arithmetic command inherits from a Command base class, ensuring a consistent interface. The Calculator clas   s uses these commands, promoting clean separation of concerns and enabling easy extensibility.  
   
2. **Plugin System with Factory Pattern**:  
- **Purpose**: Provides flexibility to dynamically load and integrate new commands as plugins, reducing the need for core code modifications.
- **Application**:  Plugins represent separate commands dynamically imported by the Calculator through a load_plugin method. This follows the **Factory** Pattern, allowing the Calculator to act as a factory that produces command objects based on the loaded plugins. For example, the add_plugin.py dynamically adds new arithmetic commands.   

3. **Facade Pattern**:    
- **Purpose**:Simplifies interactions with complex data handling, especially with additional data management features introduced in this step, such as using Pandas for history operations.  
- **Application**:The Calculations class serves as a **Facade** for history management, offering a simplified interface for storing, loading, saving, and deleting calculation records. This implementation isolates Pandas-specific code within the class, creating a cleaner and more user-friendly interface.  

4. **Singleton Pattern**:   
- **Purpose**: Ensures only one instance of the Calculator class exists, providing a consistent calculator instance across the application.  
- **Application**: The Singleton Pattern is implemented by overriding the __new__ method in the Calculator class to prevent multiple instances from being created. This approach provides centralized state management for calculation history and other features.  

5. **Strategy Pattern**:    
- **Purpose**: Allows selection from multiple division algorithms, enhancing flexibility in division operations.  
- **Application**: The DivideCommand class employs the **Strategy** Pattern by allowing users to select between standard floating-point division and integer division. This approach enables different division behaviors to be used without changing the class’s core logic.  

6. **Encapsulation and Modular Design**:    
- **Purpose**: Segregates different aspects of functionality into specific modules, following modularity and encapsulation principles.  
- **Application**:   
   - The Calculator class encapsulates command execution and history management.
   - The Calculations class manages the history of calculations, isolating history operations from arithmetic logic.
   - The main.py file provides a single entry point to the program, encapsulating REPL interactions and exception handling.

7. **Parameterized Testing**:    
- **Purpose**: Enables dynamic test generation, increasing scalability and robustness of tests.  
- **Application**:Parameterized testing is integrated with Pytest using conftest.py. This allows for dynamic test case generation with Faker, providing a diverse set of test cases to ensure comprehensive and adaptable testing.  

8. **Error Handling and Input Validation**:    
- **Purpose**:Ensures the robustness of the REPL by handling various user errors (e.g., invalid numbers, division by zero, unknown operations)  
- **Application**:Error handling is centralized within the main.py REPL interface, where exception management is consolidated to promote modularity and ensure consistent error feedback.  
- **Error Handling and Design Principles: LBYL and EAFP**:  
In this project, error handling is implemented using two complementary principles:    

1.  **Look Before You Leap (LBYL)**:  
The LBYL approach is about pre-checking conditions before performing actions that could raise an error. In the main.py file, we apply this principle in areas such as input validation and command checking:  
- **Input Validation**: Before converting user input into a Decimal for calculations, we first ensure that the input is well-formed to avoid unnecessary exceptions.
- **Operation Checking**: The application verifies if the user input matches one of the available operations before attempting to execute it. This prevents attempts to execute unsupported operations and avoids triggering avoidable exceptions.
code snippet:
```bash
if user_input in self.operation_mappings:
    value1, value2 = self.prompt_for_numbers(user_input)
    if value1 and value2:  # Check values before calculation
        self.calculate_and_store(value1, value2, user_input)
```
2. **Easier to Ask for Forgiveness than Permission (EAFP)**:  
The EAFP principle is employed to handle errors as they arise, assuming the operations will succeed unless an exception indicates otherwise. This is evident in the calculate_and_store and prompt_for_numbers methods where exceptions like ZeroDivisionError and InvalidOperation are caught after attempting the operation:  
- **Exception Handling**: In calculate_and_store, we catch ZeroDivisionError during division and InvalidOperation for invalid numeric inputs, allowing the program to handle these errors gracefully.  
- **Generic Error Handling**: The program catches generic exceptions to ensure that any unexpected errors are logged and managed effectively without crashing the application.  
code snippet:
```bash
try:
    value1_decimal, value2_decimal = map(Decimal, [value1, value2])
    # Perform operation assuming it will work
    ...
except ZeroDivisionError:
    print("Error: Division by zero.")
except InvalidOperation:
    print("Invalid number input.")
except Exception as e:  # Fallback for unforeseen errors
    print(f"An error occurred: {e}")
```
By combining LBYL and EAFP, the project ensures robust error handling, optimizes performance by avoiding unnecessary operations, and maintains graceful handling for unexpected scenarios.  

## Additional Development Practices
1. **Enhanced Logging and Environment-Based Configuration**:   
- **Purpose**: Supports monitoring with configurable logging, tailored by environment.  
- **Application**: Logging settings are configured through .env variables, enabling detailed debugging in development mode and more concise logs in production.  

2. **PEP 8 Compliance with Pylint**:   
- **Purpose**: Ensures consistent code style and readability across all project files.  
- **Aplication**: The project is fully PEP 8 compliant. Pylint is used to enforce high-quality, maintainable code and to detect any deviations from the standards.  
## Concluding Note  
This documentation provides an overview of the design patterns implemented in the Advanced Python Calculator project, highlighting its commitment to clean code, modular architecture, and scalable design. By adhering to established design principles such as SOLID, DRY, and Separation of Concerns, this project demonstrates a robust and maintainable codebase that can effectively support complex functionalities.
