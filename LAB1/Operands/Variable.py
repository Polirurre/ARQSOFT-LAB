from .Operand import Operand

class Variable(Operand):

    def __init__(self, name: str):
        """
        One constructor of Variable: sets the name to the value of the argument and value to None.

        Parameters:
        name (str): The name of the variable.
        value (float, optional): The value of the variable. Defaults to None.
        """
        self.name = name
        self.value = None
    
    def __init__(self, name: str, value: float = None):
        """
        Constructor of Variable: sets the name to the value of the argument and value to None or a provided value.

        Parameters:
        name (str): The name of the variable.
        value (float): The value of the variable.
        """
        self.name = name
        self.value = value
    
    def get_name(self) -> str:
        return self.name

    def get_value(self) -> float:
        return self.value
    
    def set_name(self, name: str):
        self.name = name
    
    def set_value(self, value: float):
        self.value = value
