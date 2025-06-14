from Spreadsheet.Cell import Cell
class Spreadsheet:
    def __init__(self, path: str):
        self.path=path
        self.cells={}

    def set(self, coordinates, content):
        self.cells[coordinates] = Cell(coordinates, content)

    def get(self, coordinates):
        return self.cells.get(coordinates, None)