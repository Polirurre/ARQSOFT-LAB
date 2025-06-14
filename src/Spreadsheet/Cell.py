class Cell:
    def __init__(self, coordinate, content):
        """
        Initializes a Cell with a coordinate and content.

        Data Needed:
            - coordinate (Coordinate): The coordinate of the cell (ex.: 'A1').
            - content (Content): The content of the cell (ex.: an Operand or formula).

        Exceptions:
            - ValueError: If the coordinate or content is invalid.

        Returns:
            - None
        """
        pass

    def getValue(self):
        """
        Retrieves the evaluated value of the cell's content.

        Data Needed:
            - None (uses self.content)

        Exceptions:
            - ValueError: If the content cannot be evaluated (ex.: malformed formula).
            - RuntimeError: If evaluation depends on undefined dependencies.

        Returns:
            - float or int: The evaluated value of the cell's content.
        """
        pass

    def setValue(self, value):
        """
        Sets the value of the cell's content.

        Data Needed:
            - value (float or int): The value to set for the cell's content.

        Exceptions:
            - ValueError: If the value is invalid or incompatible with the content type.

        Returns:
            - None
        """
        pass

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