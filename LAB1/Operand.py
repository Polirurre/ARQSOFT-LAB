from abc import ABC, abstractmethod

class Operand(ABC):

    @abstractmethod
    def get_value(self) -> float:
        """
        Abstract method to get the value of the operand.
        This will be implemented by concrete operand classes (e.g., MyNumber).
        """
        pass

