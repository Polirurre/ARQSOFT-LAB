from SimpleExpression import SimpleExpression
from Operand import Operand
from Operator import Operator

class Computation(SimpleExpression):
    
    def __init__(self, first_operand: Operand, operator: Operator, second_operand: Operand):
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand
    
    def evaluate(self, memory):
        return self.operator.compute(self.first_operand, self.second_operand)