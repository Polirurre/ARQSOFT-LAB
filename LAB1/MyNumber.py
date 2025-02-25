from Operand import Operand

class MyNumber(Operand):

    def __init__(self, value: float):
        self.value = value
    
    def get_value(self) -> float:
        return self.value
    
    def set_value(self, value: float):
        self.value = value

