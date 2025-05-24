class Terminal:
    def __init__(self, controller):
        """
        Initializes the Terminal with a reference to the SpreadsheetController.

        Data Needed:
            - controller (SpreadsheetController): The controller to delegate command execution and spreadsheet display to.

        Exceptions:
            - None

        Returns:
            - None
        """
        self.controller = controller
        self.command_types = {'RF', 'C', 'E', 'L', 'S'}  # Valid command types
        self.command = ""  # Placeholder for the command string to be processed

    def process_command(self):
        """
        Parses and executes the current command (RF, C, E, L, S) stored in self.command, delegating to the appropriate function based on the command type.

        Data Needed:
            - None (uses self.command, set by read_commands)

        Exceptions:
            - InvalidCommandError: If the command is unrecognized or has incorrect arguments.
            - InvalidArgumentError: If the command arguments are invalid (e.g., wrong number of arguments or invalid format).
            - FileNotFoundError: If the RF command specifies a file that cannot be found.

        Returns:
            - None
        """

    def read_commands(self, command_input):
        """
        Sets the command string to be processed and triggers processing of the commands.

        Data Needed:
            - command_input (str): The input string containing one or more commands to process (e.g., "C" or "RF commands.txt").

        Exceptions:
            - FileNotFoundError: If the RF command specifies a file that cannot be found.
            - InvalidCommandError: If a command is unrecognized or malformed.
            - InvalidArgumentError: If a command has invalid arguments.

        Returns:
            - None
        """
        
    def validate_command(self, command):
        """
        Validates that the command syntax is correct for the specific command type (RF, C, E, L, S).

        Data Needed:
            - command (str): The command string to validate (ex.: "C", "E A1 5", "RF commands.txt").

        Exceptions:
            - InvalidCommandError: If the command type is unrecognized.

        Returns:
            - None
        """