import os
import csv
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
#from Spreadsheet.Actions.ShowContent import ShowContent
from Spreadsheet.Cell import Cell

class FileController:
    def __init__(self):
        self.show = ShowContent()
        self.supported_extensions = ['.csv', '.txt', '.s2v']

    def _validate_file_path(self, file_path):
        """Validate the file path and its extension."""
        if not file_path or file_path.strip() == "":
            raise ReadingSpreadsheetException("Invalid file path: None or empty")
        _, ext = os.path.splitext(file_path)
        if ext.lower() not in self.supported_extensions:
            raise ReadingSpreadsheetException(f"Unsupported file format: {ext}")
        return True

    def _validate_directory(self, directory_path):
        """Validate the directory path."""
        if not os.path.exists(directory_path):
            raise SavingSpreadsheetException(f"Invalid directory path: {directory_path}")
        return True

    def create(self, path):
        """Create a new empty spreadsheet file at the specified path."""
        try:
            directory, file_name = os.path.split(path)
            if not file_name:
                raise SavingSpreadsheetException("Invalid file name: None or empty")
            if not self._validate_file_path(path):
                return False
            if directory:
                self._validate_directory(directory)
            else:
                directory = os.getcwd()
            
            with open(path, 'w') as file:
                file.write("")  # Create an empty file
            print(f"Empty spreadsheet created successfully at {path}")
            return True
        except (ReadingSpreadsheetException, SavingSpreadsheetException) as e:
            print(f"Error creating file: {str(e)}")
            return False
        except Exception as e:
            print(f"Unexpected error creating file: {str(e)}")
            return False

    def load(self, path):
        """Load spreadsheet data from the specified file path."""
        try:
            if not self._validate_file_path(path):
                return None
            if not os.path.exists(path):
                raise ReadingSpreadsheetException(f"File does not exist: {path}")
            
            with open(path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                spreadsheet_data = list(reader)
                self.show.printContentSpreadsheet(spreadsheet_data)
                return spreadsheet_data
        except ReadingSpreadsheetException as e:
            print(f"Error loading file: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error loading file: {str(e)}")
            return None

    def save(self, path, spreadsheet):
        """Save spreadsheet data to the specified file path."""
        try:
            directory, file_name = os.path.split(path)
            if not file_name:
                raise SavingSpreadsheetException("Invalid file name: None or empty")
            if not self._validate_file_path(path):
                return False
            if directory:
                self._validate_directory(directory)
            else:
                directory = os.getcwd()

            # Convert spreadsheet cells to a grid format
            max_row = max(sorted(set(int(key[1:]) for key in spreadsheet.cells.keys())), default=0)
            if max_row == 0:
                raise SavingSpreadsheetException("No data to save: Spreadsheet is empty")
            
            letras = [chr(letra) for letra in range(ord('A'), ord('Z') + 1)]
            spreadsheet_data = [
                [
                    str(spreadsheet.cells.get(f"{col}{row}", Cell()).content.getValue()).replace(";", ",") + ";"
                    for col in letras
                ]
                for row in range(1, max_row + 1)
            ]

            with open(os.path.join(directory, file_name), 'w') as file:
                for row in spreadsheet_data:
                    file.write(''.join(map(str, row)) + '\n')
            
            print(f"File saved successfully at {path}")
            return True
        except (ReadingSpreadsheetException, SavingSpreadsheetException) as e:
            print(f"Error saving file: {str(e)}")
            return False
        except Exception as e:
            print(f"Unexpected error saving file: {str(e)}")
            return False