from SpreadsheetSpecs.src.Component.Operand.FunctionOperand import FunctionOperand


class Sum(FunctionOperand):
    def __init__(self, arguments: list):
        """
        Initializes a Sum function with a list of arguments.

        Data Needed:
            - arguments (list): A list of arguments (Component objects or other values).

        Exceptions:
            - ValueError: If arguments are not valid.

        Returns:
            - None
        """
    
    def getValue(self):
        """
        Calculates the sum of the arguments.

        Data Needed:
            - None

        Exceptions:
            - TypeError: If any argument is not a number or cannot be summed.

        Returns:
            - The sum of the arguments.
        """