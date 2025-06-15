import re
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate
from UI.UI import UI
from UI.Terminal import Terminal, InvalidCommandError, InvalidArgumentError
from Controller.FileController import FileController
from Spreadsheet.Spreadsheet import Spreadsheet

class SpreadsheetController:
    def __init__(self):
        self.spreadsheet = None
        self.file_controller = FileController()
        self.ui = None
        self.terminal = Terminal()
        self.formula_manager = None 

    def process_command(self, validated_command):
        # Validate command through Terminal
        parts = validated_command.split(maxsplit=2)
        print(f"Command parts: {parts}")
        cmd_type = parts[0]

        if cmd_type == "RF":
            # RF command is already handled by Terminal.read_commands
            # Process the commands from the file
            file_commands = validated_command.split('\n')
            for cmd in file_commands:
                if cmd.strip():
                    self.process_command(cmd.strip())

        elif cmd_type == "C":
            print("Creating a new spreadsheet...")
            self.spreadsheet = Spreadsheet("")
            self.ui = UI(self.spreadsheet)

        elif cmd_type == "E":
            print("Editing a cell...")
            if len(parts) != 3:
                raise InvalidArgumentError("E command requires a cell coordinate and value (ex.: E A1 5).")
            cell_id, content = parts[1], parts[2]
            self.update_cell(cell_id, content)

        elif cmd_type == "L":
            if len(parts) != 2:
                raise InvalidArgumentError("L command requires a single filename argument (ex.: L spreadsheet.s2v).")
            path = parts[1]
            # Create new spreadsheet if none exists
            if self.spreadsheet is None:
                self.spreadsheet = Spreadsheet(path)
            # Load data into the spreadsheet
            try:
                self.file_controller.load(path, self.spreadsheet)
            except Exception as e:
                raise ReadingSpreadsheetException(f"Failed to load spreadsheet from {path}: {str(e)}")

        elif cmd_type == "S":
            if len(parts) != 2:
                raise InvalidArgumentError("S command requires a single filename argument (ex.: S spreadsheet.sv2).")
            path = parts[1]
            print(f"Saving spreadsheet to {path}...")
            self.file_controller.save(path, self.spreadsheet)



    def update_cell(self, cell_id, content):
        try:
            # Validate cell_id format (e.g., A1, B2)
            if not re.match(r'^[A-Z]+[1-9]\d*$', cell_id):
                raise ValueError(f"Invalid cell_id format: {cell_id}")

            # Check if content is a formula (starts with '=')
            if content.startswith('='):
                if self.formula_manager:
                    # Delegate formula processing to FormulaManager (to be implemented)
                    raise NotImplementedError("FormulaManager not yet implemented.")
                else:
                    raise ValueError("Formula support not available: FormulaManager not initialized.")
            else:
                # Direct value update
                self.spreadsheet.set(cell_id, content)

        except ValueError as e:
            raise ValueError(f"Error updating cell {cell_id}: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error updating cell {cell_id}: {str(e)}")
        
    def display_spreadsheet(self):
        while(True):
            if self.spreadsheet is None:
                self.process_command(self.terminal.display())
            else:
                self.process_command(self.terminal.display())
                self.ui.display()