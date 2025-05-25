from SpreadsheetSpecs.src.Component.Operand.FunctionOperand import FunctionOperand

class Min(FunctionOperand):
    def __init__(self, arguments: list):
        """
        Initializes a Min function with a list of arguments.

        Data Needed:
            - arguments (list): A list of arguments (Component objects or other values).

        Exceptions:
            - ValueError: If arguments are not valid.

        Returns:
            - None
        """

    def getValue(self):
        """
        Calculates the minimum value from the arguments.

        Data Needed:
            - None

        Exceptions:
            - ValueError: If no valid arguments are provided.

        Returns:
            - The minimum value among the arguments.
        """