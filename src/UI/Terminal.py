# Custom exception classes TO DO
import os


class InvalidCommandError(Exception):
    pass

class InvalidArgumentError(Exception):
    pass
class Terminal:
    command_types = {'RF', 'C', 'E', 'L', 'S'}

    def __init__(self):
        """Initialize a Terminal with an empty command string."""
        self.command = ""

    def display(self):
        """Display available commands and prompt for user input."""
        print("Available Commands:")
        print("  RF <filename>  : Read commands from a file (ex.: RF commands.txt)")
        print("  C             : Create spreadsheet")
        print("  E <cell> <value> : Edit a cell with a value (ex.: E A1 5)")
        print("  L <SV2 file pathname>: Load spreadsheet (ex.: L spreadsheet.sv2)")
        print("  S <SV2 file pathname> : Save spreadsheet (ex.: S spreadsheet.sv2)")

        command_input = input("\nEnter a command: ").strip()
        return self.read_commands(command_input)

    def read_commands(self, command_input):
        if not command_input:
            raise InvalidCommandError("Empty command input.")
        
        self.command = command_input
        #self.command = command_input.upper()  # Normalize command to uppercase

        # Handle RF command (read from file)
        if self.command.startswith("RF "):
            parts = self.command.split(maxsplit=1)
            if len(parts) != 2:
                raise InvalidArgumentError("RF command requires a filename (ex.: RF commands.txt).")
            filename = parts[1]
            try:
                with open(filename, 'r') as file:
                    file_commands = file.read().strip()
                    if not file_commands:
                        raise InvalidCommandError(f"File {filename} contains no valid commands.")
                    self.command = file_commands.upper()  # Normalize file commands
            except FileNotFoundError:
                raise FileNotFoundError(f"File {filename} not found.")
            except IOError as e:
                raise IOError(f"Error reading file {filename}: {e}")

        # Validate the command
        self.validate_command(self.command)
        print("command validated successfully.")
        return self.command

    def validate_command(self, command):
        parts = command.split() # Split command into parts per whitespace
        print(f"Validating command parts: {parts}")
        if not parts:
            raise InvalidCommandError("No command provided.")

        cmd_type = parts[0]
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
            if not (len(cell) >= 2 and cell[0].isalpha() and cell[1:].isdigit()):
                raise InvalidArgumentError("Invalid cell coordinate format. Use format like A1.")

        elif cmd_type == "L":
            if len(parts) != 2:
                raise InvalidArgumentError("L command requires a single filename argument (ex.: L spreadsheet.sv2).")
            if not parts[1].endswith('.sv2'):
                raise InvalidArgumentError("L command expects a .sv2 file.")
            filename = parts[1]
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found.")

        elif cmd_type == "S":
            if len(parts) != 2:
                raise InvalidArgumentError("S command requires a single filename argument (ex.: S spreadsheet.sv2).")
            if not parts[1].endswith('.sv2'):
                raise InvalidArgumentError("S command expects a .sv2 file.")