class Computation():

    def __init__ (self, first_operand: float, operator: str, second_operand: float):
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand
    
    def evaluate(self) -> float:
        return self.operator.compute(self.first_operand, self.second_operand)