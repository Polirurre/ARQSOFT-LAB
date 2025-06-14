class Coordinate:
    def __init__(self, row, col):
        """
        Initializes a Coordinate with row and column numbers.

        Data Needed:
            - row (int): The row number of the cell (ex.: 1 for 'A1').
            - col (int): The column number of the cell (ex.: 1 for 'A').

        Exceptions:
            - ValueError: If row or col is invalid (ex.: non-positive integers).

        Returns:
            - None
        """

    def getRow(self):
        """
        Retrieves the row number of the coordinate.

        Data Needed:
            - None (uses self.row)

        Exceptions:
            - None

        Returns:
            - int: The row number of the coordinate.
        """

    def getCol(self):
        """
        Retrieves the column number of the coordinate.

        Data Needed:
            - None (uses self.col)

        Exceptions:
            - None

        Returns:
            - int: The column number of the coordinate.
        """

    def setRow(self, row):
        """
        Sets the row number of the coordinate.

        Data Needed:
            - row (int): The new row number to set.

        Exceptions:
            - ValueError: If row is invalid (ex.: non-positive integer).

        Returns:
            - None
        """

    def setCol(self, col):
        """
        Sets the column number of the coordinate.

        Data Needed:
            - col (int): The new column number to set.

        Exceptions:
            - ValueError: If col is invalid (ex.: non-positive integer).

        Returns:
            - None
        """

    @staticmethod
    def column_to_number(column):
        """
        Converts a column string into a number (ex.: 'A' to 1, 'AB' to 28).

        Data Needed:
            - column (str): The column string to convert (ex.: 'A', 'AB').

        Exceptions:
            - ValueError: If the column string is invalid (ex.: contains non-letters).

        Returns:
            - int: The column number.
        """

    @staticmethod
    def number_to_column(column_num):
        """
        Converts a column number into a spreadsheet-style column string (ex.: 1 to 'A', 28 to 'AB').

        Data Needed:
            - col_num (int): The column number to convert (ex.: 1 for 'A').

        Exceptions:
            - ValueError: If col_num is invalid (ex.: non-positive integer).

        Returns:
            - str: The spreadsheet-style column string (ex.: 'A', 'AB').
        """

    @staticmethod
    def coordinate_to_xy(coordinate):
        """
        Converts a spreadsheet coordinate string into a tuple of (row, col) numbers.

        Data Needed:
            - coordinate (str): The coordinate string (ex.: 'A1').

        Exceptions:
            - ValueError: If the coordinate string is invalid (ex.: incorrect format).

        Returns:
            - tuple: A tuple of (row, col) numbers (ex.: (1, 1) for 'A1').
        """

    @staticmethod
    def to_spreadsheet_format(row, col):
        """
        Converts row and column numbers back to spreadsheet-style format (ex.: 'A1').

        Data Needed:
            - row (int): The row number (ex.: 1).
            - col (int): The column number (ex.: 1 for 'A').

        Exceptions:
            - ValueError: If row or col is invalid (ex.: non-positive integers).

        Returns:
            - str: The spreadsheet-style coordinate (ex.: 'A1').
        """