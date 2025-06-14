from SpreadsheetSpecs.src.Component import Component

class Operand(Component):
    def __init__(self, value):
        """
        Initializes an Operand object with a value.

        Data Needed:
            - value: The value of the operand (can be a number or other type as needed).

        Returns:
            - None
        """
        self.value = value

    def getValue(self):
        """
        Retrieves the value of the operand.

        Returns:
            - The stored value of the operand.
        """
        return self.value