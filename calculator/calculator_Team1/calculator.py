class SimpleCalculator:
    def __init__(self):
        self.operators = Operators()
        self.input = InputPrompt()
        self.result = Result()  # Already initialized to 0
        self.running = True

    def __str__(self):
        return str(self.result)

    def calculate(self):
        self.input.welcome()
        self.input.syntax()
        
        # Use running flag instead of result value for loop control
        while self.running:
            # Get user input
            user_input = self.get_input()
            
            # Check for exit command
            if user_input.lower() in ["exit", "quit", "q"]:
                self.input.exit()
                self.running = False
                continue
                
            # Process input
            try:
                parts = user_input.split()
                if len(parts) != 3:
                    self.input.error()
                    continue
                    
                a = float(parts[0])
                operator_symbol = parts[1].lower()
                b = float(parts[2])
                
                # Find operation type
                operation_type = self.find_operation(operator_symbol)
                
                if not operation_type or operation_type == "exit":
                    self.input.error()
                    continue
                
                # Perform calculation
                self.perform_operation(operation_type, a, b)
                
                # Show result
                print(f"{self.input.result_msg}{self.result}")
                
                # Ask to continue
                continue_calc = input(f"{self.input.again_msg} ")
                if continue_calc.lower() not in ["y", "yes"]:
                    self.input.exit()
                    self.running = False
                    
            except ValueError as e:
                print(f"Error: {e}")
                self.input.error()
            except Exception as e:
                print(f"Unexpected error: {e}")
                self.input.error()
    
    def get_input(self):
        return input("Enter your calculation: ")
        
    def find_operation(self, symbol):
        for op_name, symbols in self.operators.operators.items():
            if symbol in symbols:
                return op_name
        return None
            
    def perform_operation(self, operation, a, b):
        if operation == "addition":
            calculator = Addition()
            calculator.addition(a, b)
        elif operation == "subtraction":
            calculator = Subtraction()
            calculator.subtraction(a, b)
        elif operation == "multiplication":
            calculator = Multiplication()
            calculator.multiplication(a, b)
        elif operation == "division":
            calculator = Division()
            calculator.division(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")


class InputPrompt:
    def __init__(self):
        self.welcome_msg = "Welcome to the calculator. Please enter your calculation."
        self.syntax_msg = ">a< <operator> >b<"
        self.again_msg = "Do you want to calculate again? (y|n)"
        self.input_msg = ""
        self.exit_msg = "Thank you for using the calculator. Goodbye!"
        self.error_msg = "Invalid input. Please try again."
        self.result_msg = "Result: "
        self.version_msg = "Version 1.0.0"
        self.operators_msg = ""

    def __str__(self):
        return str(f"{self.version_msg}")
    
    def input_msg(self):
        self.input_msg = input("Enter your calculation: ")
        print(self.input_msg)

    def welcome(self):
        print(self.welcome_msg)

    def syntax(self):
        print(self.syntax_msg)

    def input(self):
        print(self.input_msg)

    def again(self):
        print(self.again_msg)

    def exit(self):
        print(self.exit_msg)

    def error(self):
        print(self.error_msg)

    def result(self):
        print(f"{self.result_msg} {Result().result}")

class Operators:
    def __init__(self):
        self.operators = {}
        self.setup_standard_operators()

    def __str__(self):
        return str(f"{self.operators}")
    
    def setup_standard_operators(self):
        self.operators = {
            "addition": ["+", "add", "plus"],
            "subtraction": ["-", "sub", "minus"],
            "multiplication": ["*", "mal", "times"],
            "division": ["/", "div", "divide", "durch"]
        }

    def add_operator(self, name, symbol):
        name = name.lower()
        symbol = symbol.lower()

        if name in self.operators:
            if symbol in self.operators[name]:
                print(f"Operator '{symbol}' already exists for '{name}'.")
            else:
                self.operators[name].append(symbol)
                print(f"Added '{symbol}' to '{name}'.")
        else:
            self.operators[name] = [symbol]
            print(f"Added new operation '{name}' with symbol '{symbol}'.")

        return self.operators

    def rem_operator(self, name, symbol):
        name = name.lower()
        symbol = symbol.lower()

        if name in self.operators:
            if symbol in self.operators[name]:
                self.operators[name].remove(symbol)
                print(f"Removed '{symbol}' from '{name}'.")
            else:
                print(f"Operator '{symbol}' not found for '{name}'.")
        else:
            print(f"Operation '{name}' not found.")

        return self.operators
    
class Result:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Result, cls).__new__(cls)
            cls._instance.result = 0
        return cls._instance

    def __str__(self):
        return str(f"{self.result}")

    def set_result(self, value):
        self.result = value
        return self.result
    
class Calculations:
    def __str__(self):
        return f"{Result().result}"
    
    def return_result(self, value):
        Result().set_result(value)


class Addition(Calculations):
    def addition(self, a, b):
        result = a + b
        self.return_result(result)
    
class Subtraction(Calculations):
    def subtraction(self, a, b):
        result = a - b
        self.return_result(result)
    
class Multiplication(Calculations):
    def multiplication(self, a, b):
        result = a * b
        self.return_result(result)
    
class Division(Calculations):
    def division(self, a, b):
        if b == 0:
            raise ValueError("Division by zero.")
        else:
            result = a / b
            self.return_result(result)


if __name__ == '__main__':
    calc = SimpleCalculator()
    calc.calculate()