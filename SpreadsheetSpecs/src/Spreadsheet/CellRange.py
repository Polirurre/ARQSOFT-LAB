class CellRange:
    def __init__(self, startingCoordinate, endingCoordinate, cells):
        """
        Initializes a CellRange with starting and ending coordinates and a cells dictionary.

        Data Needed:
            - startingCoordinate (Coordinate): The top-left coordinate of the range (ex.: 'A1').
            - endingCoordinate (Coordinate): The bottom-right coordinate of the range (ex.: 'C3').
            - cells (dict): A dictionary mapping Coordinate objects to Cell objects (ex.: Spreadsheet.cells).

        Exceptions:
            - ValueError: If the coordinates are invalid or the range is improperly defined.
            - KeyError: If a cell in the range does not exist in the cells dictionary.

        Returns:
            - None
        """
        pass

    def getValue(self):
        """
        Retrieves the numerical values of all cells within the range.

        Data Needed:
            - None (uses self.startingCoordinate, self.endingCoordinate, and self.cells)

        Exceptions:
            - ValueError: If the range contains empty or invalid cells.
            - RuntimeError: If evaluation fails (ex.: due to circular dependencies).

        Returns:
            - list: A list of numerical values (float or int) for all cells in the range.
        """
        pass