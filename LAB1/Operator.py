import Operand

class Operator():
    
    def __init__(self, operation: str):
        if operation not in {"+", "-", "*", "/"}:
            raise ValueError("Invalid operation. Allowed operations are: '+', '-', '*', '/'")
        self.operation = operation
    
    def get_operation(self) -> str:
        return self.operation
    
    def set_operation(self, operation: str):
        if operation not in {"+", "-", "*", "/"}:
            raise ValueError("Invalid operation. Allowed operations are: '+', '-', '*', '/'")
        self.operation = operation
    
    def compute(self, first: Operand, second: Operand) -> float:
        first = first.get_value()
        second = second.get_value()

        if self.operation == "+":
            return first + second
        elif self.operation == "-":
            return first - second
        elif self.operation == "*":
            return first * second
        elif self.operation == "/":
            if second == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return first / second

 