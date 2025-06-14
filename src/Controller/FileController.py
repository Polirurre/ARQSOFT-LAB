import os

from FormulaController.FormulaManager import FormulaManager

class FileController:
    def __init__(self, formulaManager):
        """
        Initializes the FileController with a FormulaManager instance for loading formulas.

        Data Needed:
            - formulaManager (FormulaManager): An instance to compute formula values during loading.

        Exceptions:
            - None

        Returns:
            - None
        """
        self.formulaManager = formulaManager

    def save_file(self, spreadsheet, path):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                for coord, cell in spreadsheet.cells.items():
                    content = cell.content
                    f.write(f"{coord}={content}\n")
        except IOError as e:
            raise IOError(f"Failed to save file: {e}")

    def load_file(self, spreadsheet, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File does not exist: {path}")

        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' not in line:
                        raise ValueError(f"Invalid line format: {line.strip()}")
                    coord, content = line.strip().split('=', 1)

                    if content.startswith('='):
                        try:
                            value = self.formula_manager.computeFormula(content[1:], spreadsheet)
                        except Exception as e:
                            raise ValueError(f"Error computing formula in cell {coord}: {e}")
                        spreadsheet.set_cell(coord, content, value)
                    else:
                        spreadsheet.set_cell(coord, content, content)

        except IOError as e:
            raise IOError(f"Failed to read file: {e}")
        except ValueError as ve:
            raise ValueError(f"File format is invalid or corrupted: {ve}")

        return spreadsheet
        pass

    def create_file(self, path):
        if os.path.exists(path):
            raise FileExistsError(f"The file already exist: {path}")
        try:
            open(path, 'x', encoding='utf-8').close()
        except IOError as e:
            raise IOError(f"Failed to create file: {e}")