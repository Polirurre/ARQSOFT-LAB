from SpreadsheetSpecs.src.Component.Operand.FunctionOperand import FunctionOperand

class Average(FunctionOperand):
    def __init__(self, arguments: list):
        """
        Initializes an Average function with a list of arguments.

        Data Needed:
            - arguments (list): A list of arguments (Component objects or other values).

        Exceptions:
            - ValueError: If arguments are not valid.

        Returns:
            - None
        """
    
    def getValue(self):
        """
        Calculates the average of the provided arguments.

        Data Needed:
            - None

        Exceptions:
            - ValueError: If arguments are not valid for averaging.

        Returns:
            - float: The average of the arguments.
        """