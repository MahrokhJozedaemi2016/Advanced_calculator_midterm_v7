## Implementation Status

The project currently supports core arithmetic operations (addition, subtraction, multiplication, and division), manages a robust history of calculations, and provides a user-friendly REPL command-line interface with error handling. Recent updates include Advanced Data Handling with Pandas, which enables efficient reading from and writing to CSV files for calculation history management. This addition allows users to load, save, clear, and delete history records in an optimized and streamlined manner. The project’s architecture follows fundamental design principles, such as SOLID, DRY, and Separation of Concerns, ensuring scalability and maintainability.

### Design Patterns Applied So Far

1. **Command Pattern**:
   **Purpose**: Encapsulates each arithmetic operation (Add, Subtract, Multiply, Divide) as a command, allowing for easy addition of new operations.
   **.Aplication**: Each arithmetic command inherits from a Command base class, ensuring a consistent interface. The Calculator clas   s uses these commands, promoting clean separation of concerns and enabling easy extensibility.
   
2. **Plugin System with Factory Pattern**
   **Purpose**: Provides a flexible structure to dynamically load and integrate new commands without modifying the core application code
   **Application**: Each plugin represents a separate command dynamically imported into the Calculator through the load_plugin method. This follows the Factory Pattern, where the Calculator acts as a factory that produces command objects based on the loaded plugins, enabling modular expansion.

3. **Facade Pattern**
**Purpose**:Simplifies interactions with complex data handling, especially with additional data management features introduced in this step, such as using Pandas for history operations.
**Application**:The Calculations class serves as a Facade for history management, offering a simplified interface for storing, loading, saving, and deleting calculation records. This implementation isolates Pandas-specific code within the class, creating a cleaner and more user-friendly interface.

4. **Singleton Pattern**
**Purpose**: Ensures only one instance of the Calculator class exists, providing a consistent calculator instance across the application.
**Application**: The Singleton Pattern is implemented by overriding the __new__ method in the Calculator class to prevent multiple instances from being created. This approach provides centralized state management for calculation history and other features.

5. **Strategy Pattern**
**Purpose**: Allows the application to select from multiple division algorithms or strategies, enhancing flexibility.
**Application**: The DivideCommand class employs the Strategy Pattern by allowing users to select between standard floating-point division and integer division. This approach enables different division behaviors to be used without changing the class’s core logic
6. **Encapsulation and Modular Design**
 **Purpose**: Segregates different aspects of functionality into specific modules, following modularity and encapsulation principles.
**Application**: 
   - The Calculator class encapsulates command execution and history management.
   - The Calculations class manages the history of calculations, isolating history operations from arithmetic logic.
   - The main.py file provides a single entry point to the program, encapsulating REPL interactions and exception handling.

5. **Parameterized Testing**
   **Purpose**: Enhances testing scalability and robustness through dynamic test generation.
   **Application**: Using conftest.py, parameterized testing is integrated with the pytest framework, allowing tests to dynamically generate test cases with Faker. This approach ensures a diverse set of test cases, making testing more comprehensive and adaptable to future changes.

6. **Error Handling and Input Validation**
**Purpose**:Ensures the robustness of the REPL by handling various user errors (e.g., invalid numbers, division by zero, unknown operations)
**.Application**:Error handling is centralized within the main.py REPL interface, which promotes modularity and separates exception management into one location.

## Concluding Note
This documentation provides an overview of the design patterns implemented in the Advanced Python Calculator project and outlines patterns planned for future development. As the project evolves, additional design patterns will be introduced to further enhance its functionality, scalability, and maintainability. Detailed descriptions and code examples for each new pattern will be added to this document as they are applied. By following these best practices in software design, this project aims to serve as a comprehensive example of clean code principles, modular architecture, and adaptable design.

This document will be updated continuously to reflect the ongoing enhancements and improvements, ensuring that the project remains a reliable and extensible tool for users and developers alike.
