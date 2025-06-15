import csv
import os
import argparse
import re
from Spreadsheet.Coordinate import Coordinate
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from Spreadsheet.Cell import Cell

class FileController:
    def __init__(self):
        pass

    def save(self, filepath, spreadsheet):
        try:
            # Get maximum dimensions of the spreadsheet
            max_row, max_col = spreadsheet.get_max_dimensions()
            
            # If spreadsheet is empty, create an empty file
            if max_row == 0 and max_col == 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    return
            
            # Prepare lines for writing
            lines = []
            for row in range(1, max_row + 1):
                row_content = []
                for col in range(1, max_col + 1):
                    coord = Coordinate.to_spreadsheet_format(row, col)
                    try:
                        # Get cell value
                        value = spreadsheet.get(coord)
                        # Convert value to string, handling different types
                        if isinstance(value, (int, float)):
                            str_value = str(value)
                        else:
                            str_value = str(value)
                            # Replace commas with semicolons in formula arguments
                            if str_value.startswith('='):
                                str_value = str_value.replace(',', ';')
                        row_content.append(str_value)
                    except KeyError:
                        # Empty cell
                        row_content.append('')
                # Join row contents with semicolons, removing trailing empty cells
                while row_content and row_content[-1] == '':
                    row_content.pop()
                lines.append(';'.join(row_content))
            
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
                
        except IOError as e:
            raise SavingSpreadsheetException(f"Error writing to file {filepath}: {str(e)}")
        except Exception as e:
            raise SavingSpreadsheetException(f"Unexpected error while saving spreadsheet: {str(e)}")
        
    def load(self, filepath, spreadsheet):
        try:
            with open(filepath, 'r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                row_num = 1
                
                for row in reader:
                    col_num = 1
                    for content in row:
                        # Skip empty cells
                        if content:
                            # Convert function arguments from ',' back to ';' in formulas
                            if content.startswith('='):
                                content = re.sub(r'(?<=\w),(?=\w)', ';', content)
                            
                            # Convert column number to letter (1 -> A, 2 -> B, etc.)
                            col_letter = Coordinate.number_to_column(col_num)
                            # Create coordinate in spreadsheet format (e.g., A1)
                            coord_str = f"{col_letter}{row_num}"
                            
                            # Set the cell content in the provided spreadsheet
                            spreadsheet.set(coord_str, content)
                        
                        col_num += 1
                    row_num += 1
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filepath}' not found.")
        except Exception as e:
            raise ValueError(f"Error loading S2V file: {str(e)}")