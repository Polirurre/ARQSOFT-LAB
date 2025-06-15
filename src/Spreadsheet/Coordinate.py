class Coordinate:
    def __init__(self, coordinates):
        self.row, self.col = Coordinate.coordinate_to_xy(coordinates)

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
        if not column or not column.isalpha():
            raise ValueError("Column string must contain only letters")
        
        column = column.upper()
        result = 0
        for char in column:
            if not ('A' <= char <= 'Z'):
                raise ValueError("Column string must contain only letters A-Z")
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

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
        if not isinstance(column_num, int) or column_num <= 0:
            raise ValueError("Column number must be a positive integer")
        
        result = ""
        while column_num > 0:
            column_num -= 1
            result = chr(column_num % 26 + ord('A')) + result
            column_num //= 26
        return result

    @staticmethod
    def coordinate_to_xy(coordinate):
        if not coordinate or not isinstance(coordinate, str):
            raise ValueError("Coordinate must be a non-empty string")
        
        # Split coordinate into letters (column) and digits (row)
        col_str = ""
        row_str = ""
        for char in coordinate:
            if char.isalpha():
                col_str += char
            elif char.isdigit():
                row_str += char
            else:
                raise ValueError("Invalid coordinate format")
        
        if not col_str or not row_str:
            raise ValueError("Coordinate must contain letters and numbers")
        
        row = int(row_str)
        if row <= 0:
            raise ValueError("Row number must be positive")
        
        col = Coordinate.column_to_number(col_str)
        return (row, col)

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
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column must be integers")
        if row <= 0 or col <= 0:
            raise ValueError("Row and column numbers must be positive")
        
        col_str = Coordinate.number_to_column(col)
        return f"{col_str}{row}"