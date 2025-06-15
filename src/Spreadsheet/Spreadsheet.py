from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate
class Spreadsheet:
    def __init__(self, path: str):
        self.path=path
        self.cells={}

    def set(self, coordinates, content):
        self.cells[coordinates] = Cell(coordinates, content)

    def get(self, coordinates):
        if coordinates in self.cells:
            return self.cells[coordinates].getValue()
        else:
            raise KeyError(f"Cell at coordinates '{coordinates}' does not exist.")
        
    def get_max_dimensions(self):
        if not self.cells:
            return (0, 0)
        
        max_row = 0
        max_col = 0
        
        for coord in self.cells:
            cell_coord = Coordinate(coord)
            row = cell_coord.getRowNum()
            col = cell_coord.getColNum()
            max_row = max(max_row, row)
            max_col = max(max_col, col)
        
        return (max_row, max_col)