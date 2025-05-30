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
        pass

    def save_file(self, spreadsheet, path):
        """
        Saves the spreadsheet data to a file at the specified path using a custom text format.

        Data Needed:
            - spreadsheet (Spreadsheet): The spreadsheet object containing cells to save.
            - path (str): The file path where the spreadsheet will be saved.

        Exceptions:
            - IOError: If there is an error writing to the file.

        Returns:
            - None
        """
        pass

    def load_file(self, spreadsheet, path):
        """
        Loads spreadsheet data from a file at the specified path into the provided spreadsheet object.

        Data Needed:
            - spreadsheet (Spreadsheet): The spreadsheet object to populate with loaded data.
            - path (str): The file path from which to load the spreadsheet data.

        Exceptions:
            - FileNotFoundError: If the specified file does not exist.
            - IOError: If there is an error reading the file.
            - ValueError: If the file format is invalid or incompatible because of the file being corrupted.

        Returns:
            - Spreadsheet: The updated spreadsheet object with loaded data.
        """
        pass
    def create_file(self, path):
        """
        Creates a new empty file at the specified path for spreadsheet data.

        Data Needed:
            - path (str): The file path where the new empty file will be created.

        Exceptions:
            - IOError: If there is an error creating the file (ex.: permission denied or invalid path).
            - FileExistsError: If a file already exists at the specified path.

        Returns:
            - None
        """
        pass