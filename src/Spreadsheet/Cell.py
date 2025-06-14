from src.Spreadsheet.Coordinate import Coordinate

class Cell:
    def __init__(self, rowNumber, columnNumber, content=None, coordinate=None):
        self.coordinate = Coordinate(rowNumber, columnNumber)
        self.refCells = []
        self.content = content if content is not None else ""

    def getValue(self):
        return self.content

    def setValue(self, value):
        self.content = value

    def getDependentCells(self):
        """
        Retrieves a list of cells that depend on this cell.

        Data Needed:
            - None (uses internal dependency tracking)

        Exceptions:
            - None

        Returns:
            - list: A list of CellDependency objects representing dependent cells.
        """
        pass

    def addDependency(self, targetCell):
        """
        Adds a dependency on another cell to this cell's dependency list.

        Data Needed:
            - targetCell (Coordinate): The coordinate of the cell this cell depends on (ex.: 'A1').

        Exceptions:
            - ValueError: If the targetCell coordinate is invalid or identical to this cell's coordinate.

        Returns:
            - None
        """