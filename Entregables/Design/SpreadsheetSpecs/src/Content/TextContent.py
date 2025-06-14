from Spreadsheet.Content import Content

class TextContent(Content):
    def __init__(self, string: str):
        """
        Initializes a TextContent object with a string value.

        Data Needed:
            - string (str): The string value to be stored in the content.

        Exceptions:
            - ValueError: If the provided string is not a valid string.

        Returns:
            - None
        """

    def getValue(self) -> str:
        """
        Retrieves the string value of the TextContent.

        Data Needed:
            - None (uses self.value)

        Exceptions:
            - None

        Returns:
            - str: The stored string value.
        """
        return self.value

    def setValue(self, value: str) -> None:
        """
        Sets the string value of the TextContent.

        Data Needed:
            - value (str): The new string value to set.

        Exceptions:
            - ValueError: If the provided value is not a valid string.

        Returns:
            - None
        """
        pass