from SpreadsheetSpecs.src.Component import Component

class Operator(Component):
    operator_types = {'add', 'subs', 'mult', 'div'}

    def __init__(self, operator_type: str):
        """
        Initializes an Operator object with a specific operator type.

        Data Needed:
            - operator_type (str): The type of operator (must be one of 'add', 'subs', 'mult', 'div').

        Exceptions:
            - ValueError: If the operator_type is not valid.

        Returns:
            - None
        """
        pass

    def getValue(self):
        """
        Retrieves the operator type as a string representation.

        Returns:
            - str: The operator type (ex.: 'add', 'subs', 'mult', 'div').
        """
        pass