## Implementation Status

The project currently supports basic arithmetic operations (addition, subtraction, multiplication, and division) and includes a history of calculations. These enhancements have been implemented in line with design principles such as SOLID, DRY, and Separation of Concerns. 

### Design Patterns Applied So Far

1. **Encapsulation and Modular Design**: 
   - Each arithmetic operation is encapsulated within a dedicated function, and operations are performed via the `Calculator` class.
   - A `Calculations` class manages the history of calculations, ensuring that history management is separate from the operation logic.
   
2. **Planned Patterns**:
   - **Command Pattern**: Future updates will incorporate the Command Pattern within a REPL interface, allowing each arithmetic operation to be encapsulated as a command.
   - **Facade Pattern**: Once data handling with Pandas is introduced, the Facade Pattern will simplify complex interactions.
   - **Singleton Pattern**: This may be applied for configuration management, particularly for global settings such as logging.
   - **Factory Method and Strategy Patterns**: These patterns will facilitate flexibility in the creation and execution of operations, supporting advanced functionality and user-defined commands.

Detailed descriptions and code examples for each pattern will be added as they are implemented in future steps.

