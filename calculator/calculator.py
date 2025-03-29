class SimpleCalculator:
    def __init__(self):
        self.operators = Operators()
        self.input = InputPrompt()
        self.result = Result()

    def __str__(self):
        return str(f"{self.operators}")

    def calculate(self, operator, a, b):
        while self.result == 0:
            pass


class InputPrompt:
    pass

class Operators:
    def __init__(self):
        self.operators = {}

    def __str__(self):
        return str(f"{self.operators}")

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
    
class Calculations:
    pass

class Result(Calculations):
    def __init__(self):
        self._result = 0

    def __str__(self):
        return str(f"{self.result}")

    def result(self, result):
        self.result = result
        return self.result

class Addition(Calculations):
    def __init__(self):
        self._result = 0

    def __str__(self):
        return str(f"{self.result}")

    def addition(self, a, b):
        self.result = a + b
        Calculations.result(self, self.result)
        return self.result
    
class Subtraction(Calculations):
    def __init__(self):
        self.result = 0

    def __str__(self):
        return str(f"{self.result}")

    def subtraction(self, a, b):
        self.result = a - b
        Calculations.result(self, self.result)
        return self.result
    
class Multiplication(Calculations):
    def __init__(self):
        self.result = 0

    def __str__(self):
        return str(f"{self.result}")
    
    def multiplication(self, a, b):
        self.result = a * b
        Calculations.result(self, self.result)
        return self.result
    
class Division(Calculations):
    def __init__(self):
        self.result = 0

    def __str__(self):
        return str(f"{self.result}")
    
    def division(self, a, b):
        if b == 0:
            raise ValueError("Division by zero.")
        else:
            self.result = a / b
            Calculations.result(self, self.result)
        return self.result


if __name__ == '__main__':
    calc = SimpleCalculator()

    calc.operators.add_operator("addition", "+")
    calc.operators.add_operator("addition", "add")
    calc.operators.add_operator("addition", "plus")
    calc.operators.add_operator("subtraction", "-")
    calc.operators.add_operator("subtraction", "sub")
    calc.operators.add_operator("subtraction", "minus")
    calc.operators.add_operator("multiplication", "*")
    calc.operators.add_operator("multiplication", "mal")
    calc.operators.add_operator("multiplication", "times")
    calc.operators.add_operator("division", "/")
    calc.operators.add_operator("division", "div")
    calc.operators.add_operator("division", "divide")
    calc.operators.add_operator("division", "durch")
    calc.operators.add_operator("result", "enter")
    calc.operators.add_operator("result", "return")
    calc.operators.add_operator("result", "go")
    calc.operators.add_operator("result", "=")
    print(calc.operators)


