from Spreadsheet.Coordinate import Coordinate
from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.FormulaContent import FormulaContent

class Cell:
    def __init__(self, coordinate=None, content=None):
        self.coordinate = coordinate
        self.setValue(content if content is not None else "")
        self.refCells = set()

    def getValue(self):
        return self.content

    def setValue(self, input: str):
        print(input) #TO DO
        try:
            # Try converting the string to a float
            # If successful, add Numbercontent
            self.content = NumericalContent(float(input))
        except ValueError:
            # If conversion fails, it's not a numeric string
            if input.startswith('='): # Check if it starts with '='
                self.content = FormulaContent(input)
            else:# Otherwise, it's a regular string
                self.content = TextContent(input)

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