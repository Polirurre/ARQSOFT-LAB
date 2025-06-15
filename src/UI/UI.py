from Spreadsheet.Coordinate import Coordinate


class UI:
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet  # Store the spreadsheet object

    def display(self):
        # Check if cells dictionary is empty
        if not self.spreadsheet.cells:
            print("No data to display.")
            return

        # Determine the dimensions of the spreadsheet
        max_row, max_col = self.spreadsheet.get_max_dimensions()
        
        if max_row < 1 or max_col < 1:
            print("No valid data to display.")
            return

        # Print column headers (A, B, C, ...)
        print("   ", end=" ")  # Space for row index column
        for col in range(1, max_col + 1):
            col_letter = Coordinate.number_to_column(col)  # Convert column number to letter
            print(f"{col_letter:^8}", end=" ")
        print()  # New line after headers

        # Print separator
        print("   " + "-" * (max_col * 9 + 1))

        # Print rows with row indices
        for row in range(1, max_row + 1):
            print(f"{row:<3}", end="|")  # Print row index
            for col in range(1, max_col + 1):
                # Convert row and col to spreadsheet coordinate (e.g., "A1")
                coord = Coordinate.to_spreadsheet_format(row, col)
                # Get cell value if it exists, otherwise use empty string
                try:
                    cell_value = self.spreadsheet.get(coord)
                except KeyError:
                    cell_value = ""
                print(f"{str(cell_value):^8}", end="|")  # Center-align cell value
            print()  # New line after each row

        print()  # Extra line for readability