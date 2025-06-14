class Terminal:
    command_types = {'RF', 'C', 'E', 'L', 'S'}
    def __init__(self):
        """
        Initializes the Terminal.

        Data Needed:
            - None

        Exceptions:
            - None

        Returns:
            - None
        """
        self.command = ""  # Placeholder for the command string to be processed

    def read_commands(self, command_input):
        """
        Sets the command string to be processed and triggers processing of the commands.

        Data Needed:
            - command_input (str): The input string containing commands to process.

        Exceptions:
            - FileNotFoundError: If the RF command specifies a file that cannot be found.
            - InvalidCommandError: If a command is unrecognized or malformed.
            - InvalidArgumentError: If a command has invalid arguments.

        Returns:
            - command (str): The command string that was set for processing.
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