class CellDependency:
    def __init__(self, sourceCell, targetCell):
        """
        Initializes a CellDependency representing a dependency between two cells.

        Data Needed:
            - sourceCell (Coordinate): The coordinate of the source cell (ex.: 'A1').
            - targetCell (Coordinate): The coordinate of the target cell (ex.: 'B1').

        Exceptions:
            - ValueError: If the sourceCell or targetCell coordinates are invalid.

        Returns:
            - None
        """
        pass

    def getSourceCell(self):
        """
        Retrieves the coordinate of the source cell.

        Data Needed:
            - None (uses self.sourceCell)

        Exceptions:
            - None

        Returns:
            - Coordinate: The coordinate of the source cell.
        """
        pass

    def getTargetCell(self):
        """
        Retrieves the coordinate of the target cell.

        Data Needed:
            - None (uses self.targetCell)

        Exceptions:
            - None

        Returns:
            - Coordinate: The coordinate of the target cell.
        """
        pass