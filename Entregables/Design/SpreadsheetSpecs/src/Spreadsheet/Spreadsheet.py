class Spreadsheet:
    def __init__(self):
        """
        Initializes an empty Spreadsheet with a dictionary to store cell data.

        Data Needed:
            - None

        Exceptions:
            - None

        Returns:
            - None
        """
        pass

    def setCellContent(self, coordinates, content):
        """
        Sets the content (value or formula) of a specified cell.

        Data Needed:
            - coordinate (str): The identifier of the cell (ex.: 'A1').
            - content (str): The value or formula to set (ex.: '5', '=A1+B2').

        Exceptions:
            - ValueError: If the coordinate is invalid (ex.: incorrect format).

        Returns:
            - None
        """
        pass

    def getCellContent(self, coordinates):
        """
        Retrieves the content of a specified cell.

        Data Needed:
            - coordinate (str): The identifier of the cell (ex.: 'A1').

        Exceptions:
            - ValueError: If the coordinate is invalid (ex.: incorrect format).
            - KeyError: If the cell does not exist.

        Returns:
            - str: The content of the cell (ex.: '5', '=A1+B2').
        """
        pass