from abc import ABC, abstractmethod


class FunctionOperand(ABC):
    # Enum for function types
    function_types = {"sum", "min", "max", "average"}

    def __init__(self, function_type: str, arguments: list):
        """
        Initializes a FunctionOperand with a function type and list of arguments.

        Data Needed:
            - type (str): The type of function ('sum', 'min', 'max', 'average').
            - arguments (list): A list of arguments (Component objects or other values).

        Exceptions:
            - ValueError: If the function_type is invalid or arguments are not valid.

        Returns:
            - None
        """
        self.type = function_type
        self.arguments = arguments
        pass

    @abstractmethod
    def getValue(self) -> float:
        """
        Evaluates the function based on its type and arguments.

        Returns:
            float: The evaluated result of the function.

        Raises:
            ValueError: If evaluation fails (ex.: invalid arguments).
        """
        pass