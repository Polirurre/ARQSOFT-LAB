class Argument:
    def __init__(self, value, arg_type):
        """
        Initializes an Argument with a value and its type.

        Data Needed:
            - value (Cell or CellRange or float or int): The value or object representing the argument (ex.: a Cell, CellRange, or literal).
            - arg_type (str): The type of the argument (ex.: 'CellReference', 'RangeCell', 'Literal').

        Exceptions:
            - ValueError: If the value or arg_type is invalid (ex.: unsupported type or empty arg_type).

        Returns:
            - None
        """
        pass

    def getValue(self):
        """
        Retrieves the evaluated value of the argument.

        Data Needed:
            - None (uses self.value and self.arg_type)

        Exceptions:
            - ValueError: If the argument type is invalid or the value cannot be evaluated.
            - RuntimeError: If evaluation fails (ex.: due to circular dependencies or missing dependencies).

        Returns:
            - float or int or list: The evaluated value (single number for Cell/Literal, list of numbers for RangeCell).
        """
        pass