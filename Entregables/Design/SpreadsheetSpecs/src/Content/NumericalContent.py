from Spreadsheet.Content import Content

class NumberContent(Content):
    def __init__(self, number: float):
        """
        Initializes a NumberContent object with a numeric value.

        Data Needed:
            - number (float): The numeric value to be stored in the content.

        Exceptions:
            - ValueError: If the provided number is not a valid float or int.

        Returns:
            - None
        """
        pass

    def getValue(self) -> float:
        """
        Retrieves the numeric value of the NumberContent.

        Data Needed:
            - None (uses self.value)

        Exceptions:
            - None

        Returns:
            - float: The stored numeric value.
        """
        pass

    def setValue(self, value: float) -> None:
        """
        Sets the numeric value of the NumberContent.

        Data Needed:
            - value (float): The new numeric value to set.

        Exceptions:
            - ValueError: If the provided value is not a valid float or int.

        Returns:
            - None
        """
        pass