import Operand
import Operator
from abc import ABC, abstractmethod

class SimpleExpression(ABC):

    def __init__ (self, first_operand: Operand, operator: Operator, second_operand: Operand):
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand
    
    def get_first_operand(self) -> float:
        return self.first_operand

    def get_second_operand(self) -> float:
        return self.second_operand
    
    def get_operator(self) -> str:
        return self.operator

    @abstractmethod
    def evaluate(self, memory):
        pass


    