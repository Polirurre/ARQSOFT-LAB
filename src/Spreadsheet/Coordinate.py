class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getRowNum(self):
        return self.row

    def getColNum(self):
        return self.col

    def setRow(self, row):
        self.row = row

    def setCol(self, col):
        self.col = col

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