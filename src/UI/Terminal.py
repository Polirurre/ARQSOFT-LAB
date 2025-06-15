# Custom exception classes TO DO
class InvalidCommandError(Exception):
    pass

class InvalidArgumentError(Exception):
    pass

class Terminal:
    command_types = {'RF', 'C', 'E', 'L', 'S'}

    def __init__(self):
        self.command = ""  # Placeholder for the command string to be processed

    def display(self):
        # Display possible actions
        print("Available Commands:")
        print("  RF <filename>  : Read commands from a file (ex.: RF commands.txt)")
        print("  C             : Clear the spreadsheet")
        print("  E <cell> <value> : Edit a cell with a value (ex.: E A1 5)")
        print("  L             : Load the spreadsheet")
        print("  S             : Save the spreadsheet")

        # Query user for input
        command_input = input("\nEnter a command: ").strip()

        # Read and analyze the command
        return self.read_commands(command_input)

    def read_commands(self, command_input):
        if not command_input:
            raise InvalidCommandError("Empty command input.")

        self.command = command_input

        # If command is RF, attempt to read from file
        if command_input.startswith("RF "):
            parts = command_input.split(maxsplit=2)
            if len(parts) != 2:
                raise InvalidArgumentError("RF command requires a filename (ex.: RF commands.txt).")
            filename = parts[1]
            try:
                with open(filename, 'r') as file:
                    file_commands = file.read().strip()
                    if not file_commands:
                        raise InvalidCommandError(f"File {filename} is empty.")
                    self.command = file_commands
            except FileNotFoundError:
                raise FileNotFoundError(f"File {filename} not found.")

        # Validate the command
        self.validate_command(self.command)
        return self.command

    def validate_command(self, command):
        parts = command.split()
        if not parts:
            raise InvalidCommandError("No command provided.")

        cmd_type = parts[0].upper()
        if cmd_type not in self.command_types:
            raise InvalidCommandError(f"Unrecognized command: {cmd_type}")

        # Validate command-specific syntax
        if cmd_type == "RF":
            if len(parts) != 2:
                raise InvalidArgumentError("RF command requires a single filename argument (ex.: RF commands.txt).")
            if not parts[1].endswith('.txt'):
                raise InvalidArgumentError("RF command expects a .txt file.")
        
        elif cmd_type == "C":
            if len(parts) != 1:
                raise InvalidArgumentError("C command takes no arguments.")
        
        elif cmd_type == "E":
            if len(parts) != 3:
                raise InvalidArgumentError("E command requires a cell coordinate and value (ex.: E A1 5).")
            cell = parts[1]
            # Basic cell coordinate validation (ex.: A1, B2)
            if not (len(cell) >= 2 and cell[0].isalpha() and cell[1:].isdigit()):
                raise InvalidArgumentError("Invalid cell coordinate format. Use format like A1.")
        
        elif cmd_type == "L":
            if len(parts) != 1:
                raise InvalidArgumentError("L command takes no arguments.")
        
        elif cmd_type == "S":
            if len(parts) != 1:
                raise InvalidArgumentError("S command takes no arguments.")
        
        return None